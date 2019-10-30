import os
import time
import requests
import numpy as np

import airsim

import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

from drone_object_detection import object_detector

from util import spinSquare, oneSquare

# 기본 드론 정보
DRONE_INFOS = {
    "name":"Drone1",
    "type":"all"
}
# START_POS = {"x_val":60049.859375, "y_val":1822.984375, "z_val":13177.371094}
# MAIN_SPIN = {
#     "pos":[
#         [60049.859375, 1822.984375],
#         [60099.859375, 1822.984375],
#         [60099.859375, 1872.984375],
#         [60049.859375, 1872.984375]
#     ],
#     "max":20,
#     "gap":10
# }
START_POS = {"x_val":669.859375, "y_val":-31697.015625, "z_val":16057.371094}
MAIN_SPIN = {
    "pos":[
        [669.859375, -31697.015625],
        [719.859375, -31697.015625],
        [719.859375, -31647.015625],
        [669.859375, -31647.015625]
    ],
    "max":10,
    "gap":20
}

# 움직일 때 쓸 높이와 최대 이동 거리
MAIN_HEIGHT = 15
MAX_MOVE_LENGTH = 3

# 캡쳐에 쓰일 변수
CAMERA_NAME = '3' # 아래
TARGET = None

# Object Detect 객체 생성
detector = object_detector.Detector()

class Drone():
    def __init__(self, info, startPos, routeInfo):
        self.name = info["name"]
        self.number = info["name"][-1:]
        self.type = info["type"]
        self.spos = startPos
        self.npos = {"x_val":0., "y_val":0., "z_val":0.}
        self.isFind = False
        self.aiResult = None
        self.serverRes = []
        self.findCnt = 0

        self.mainRoute = spinSquare.square(routeInfo["pos"], routeInfo["max"], routeInfo["gap"]).makeRoute().getRoute()
        self.mainRouteLen = len(self.mainRoute)
        self.nowMainRouteNum = 1

        self.oneSquareService = oneSquare.square()
        self.subRoute = []
        self.subRouteLen = 0
        self.nowSubRouteNum = 0

        self.drone = airsim.MultirotorClient()
        self.drone.confirmConnection()
    
    def takeoff(self):
        self.drone.enableApiControl(True, vehicle_name=self.name)
        self.drone.armDisarm(True, vehicle_name=self.name)
        self.drone.takeoffAsync(vehicle_name=self.name)
        self.IMAGE_TYPE = airsim.ImageType.Scene

    def landing(self):
        print("Landing...")
        # landing 동안 sleep의 취해 안전하게 착륙시킨다
        # self.drone.landAsync(vehicle_name=self.name)
        # time.sleep(70)
        print("Landing Complete!")

        self.drone.armDisarm(False, vehicle_name=self.name)
        self.drone.enableApiControl(False, vehicle_name=self.name)
        self.drone.reset()

    def moveToV(self, x, y, z, c=1):
        self.drone.moveByVelocityAsync(x, y, z, c, vehicle_name=self.name).join()
        self.drone.moveByVelocityAsync(0, 0, 0, 1, vehicle_name=self.name).join()
        
    def doTracking(self, vAtFind, height):
        x = self.npos["x_val"]
        y = self.npos["y_val"]

        if self.aiResult["target_finded"]:
            if self.aiResult["drone_controller"]["x"] == "turn_left":
                y -= vAtFind
            elif self.aiResult["drone_controller"]["x"] == "turn_right":
                y += vAtFind

            if self.aiResult["drone_controller"]["y"] == "upwards":
                x += vAtFind
            elif self.aiResult["drone_controller"]["y"] == "downwards":
                x -= vAtFind
        z = self.h - height

        self.moveToV(x, y, z)

    def doMainPatrol(self, maxLen, height):
        _ = self.getNowPosition()

        dx = self.mainRoute[self.nowMainRouteNum][0] - self.npos["x_val"]
        dy = self.mainRoute[self.nowMainRouteNum][1] - self.npos["y_val"]
        if (dx**2) + (dy**2) < 10:
            self.nowMainRouteNum = 1 if self.mainRouteLen == self.nowMainRouteNum else self.nowMainRouteNum + 1

        x = min(dx, maxLen) if dx > 0 else max(dx, -(maxLen))
        y = min(dy, maxLen) if dy > 0 else max(dy, -(maxLen))
        z = self.h - height

        self.moveToV(x, y, z)

    def doSubPatrol(self, maxLen, height, x, y):
        _ = self.getNowPosition()
        self.subRoute, self.subRouteLen = self.oneSquareService.makeRoute(self.subRoute, [x, y], 50).getRoute()

        dx = self.subRoute[self.nowSubRouteNum][0] - self.npos["x_val"]
        dy = self.subRoute[self.nowSubRouteNum][1] - self.npos["y_val"]
        if (dx**2) + (dy**2) < 10:
            self.nowSubRouteNum = 1 if self.subRouteLen == self.nowSubRouteNum else self.nowSubRouteNum + 1

        x = min(dx, maxLen) if dx > 0 else max(dx, -(maxLen))
        y = min(dy, maxLen) if dy > 0 else max(dy, -(maxLen))
        z = self.h - height

        self.moveToV(x, y, z)
    
    def capture(self, iter, cameraNum, target):
        _ = self.getNowPosition()

        print("Now [x:{}, y:{}, z:{}]".format(self.npos["x_val"], self.npos["y_val"], self.h))

        response_image = self.drone.simGetImage(cameraNum, self.IMAGE_TYPE, vehicle_name = self.name)
        decoded_frame = imdecode(np.asarray(bytearray(response_image), dtype="uint8"), IMREAD_COLOR)

        resize_img = cv2.resize(decoded_frame, dsize=(256, 192), interpolation=cv2.INTER_CUBIC)
        encoded_resize_img = cv2.imencode(".png", resize_img)
        self.request_img = np.asarray(bytearray(encoded_resize_img[1]), dtype="uint8")

        self.aiResult = detector.run_object_detector(decoded_frame, target)

        if self.isFind:
            if self.aiResult["target_finded"]:
                self.findCnt = 0 if self.findCnt <= 0 else self.findCnt - 1
            else:
                self.findCnt += 1
                if self.findCnt == 5:   # n번 이상 놓치면 찾을 수 없는 상태
                    self.isFind = False
                    self.findCnt = 0
        else:
            if self.aiResult["target_finded"]:
                self.findCnt += 1
                if self.findCnt == 2:   # n번 이상 찾아야 제대로 찾은 상태
                    self.isFind = True
                    self.findCnt = 0
            else:
                self.findCnt = 0 if self.findCnt <= 0 else self.findCnt - 1

        # cv2.imwrite('./images/missingPerson/hanam{}.jpg'.format(iter), decoded_frame)
        
        cv2.imshow('cam', self.aiResult['image'])
        cv2.waitKey(1)
    
    def postServer(self, i):
        datas = {
            "name" : self.name,
            "number" : self.number,
            "x" : self.npos["x_val"],
            "y" : self.npos["y_val"],
            "z" : self.npos["z_val"],
            "img" : self.request_img,
            "isFind" : self.isFind,
            "timestamp":time.time(),
            "iter":i
        }

        res = requests.post('http://localhost:5000/api/droneUpdate', data=datas)
        self.serverRes = res.json()["list"]

    def getNowPosition(self):
        pos = self.drone.simGetGroundTruthKinematics(vehicle_name=self.name).position

        self.npos["x_val"] = self.spos["x_val"] + pos.x_val
        self.npos["y_val"] = self.spos["y_val"] + pos.y_val
        self.npos["z_val"] = self.spos["z_val"] - pos.z_val
        self.h = float(self.drone.getDistanceSensorData(vehicle_name=self.name, distance_sensor_name="Distance1").distance)

        return self.npos


def run():
    cv2.startWindowThread()
    d = Drone(DRONE_INFOS, START_POS, MAIN_SPIN)
    d.takeoff()
    i = 0

    while True:
        print("====================== " + str(i))
        if d.isFind:
            if len(d.serverRes) >= 2:
                # 내 근처에 나보다 빠른 번호가 target을 찾았다면 나는 Main 혹은 Sub 루트
                # 아니라면 추적
                pass
            else:
                # 추적(속도, 높이)
                d.doTracking(2, MAIN_HEIGHT - 2)
        else:
            if len(d.serverRes) >= 1:
                # 내 앞 번호가 찾았으면 sub
                # 아니라면 main 패트롤
                d.doSubPatrol(MAX_MOVE_LENGTH, MAIN_HEIGHT - 1, d.serverRes[0]["x"], d.serverRes[0]["y"])
                pass
            else:
                d.doMainPatrol(MAX_MOVE_LENGTH, MAIN_HEIGHT)

        d.capture(i, CAMERA_NAME, TARGET)
        d.postServer(i)
        i += 1

    d.landing()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

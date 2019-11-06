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
    "start":{
        "x_val":669.859375,
        "y_val":-31697.015625,
        "z_val":16057.371094
    }
}
# DRONE_INFOS = {
#     "name":"Drone2",
#     "start":{
#         "x_val":829.859375,
#         "y_val":-31697.015625,
#         "z_val":16057.371094
#     }
# }
# DRONE_INFOS = {
#     "name":"Drone3",
#     "start":{
#         "x_val":829.859375,
#         "y_val":-31537.015625,
#         "z_val":16057.371094
#     }
# }
MAIN_SPIN = {
    "pos":[
        [669.859375, -31697.015625],
        [829.859375, -31697.015625],
        [829.859375, -31537.015625],
        [669.859375, -31537.015625]
    ],
    "max":20,
    "gap":20
}

# 움직일 때 쓸 높이와 최대 이동 거리
MAIN_HEIGHT = 15
MAX_MOVE_LENGTH = 5

# 캡쳐에 쓰일 변수
CAMERA_NAME = '3' # 아래
TARGET = "missingPerson"

# Object Detect 객체 생성
detector = object_detector.Detector()

class Drone():
    def __init__(self, info, routeInfo):
        self.name = info["name"]
        self.number = info["name"][-1:]
        self.spos = info["start"]
        self.npos = {"x_val":0., "y_val":0., "z_val":0.}
        self.isFind = False
        self.aiResult = None
        self.serverRes = []
        self.findCnt = 0

        self.mainRoute = spinSquare.square(routeInfo["pos"], routeInfo["max"], routeInfo["gap"]).makeRoute().getRoute()
        self.mainRouteLen = len(self.mainRoute)
        minDiff = 100000
        minIndex = 0
        i = 0
        for route in self.mainRoute:
            diff = (self.spos["x_val"] - route[0])**2 + (self.spos["y_val"] - route[1])**2
            if minDiff > diff:
                minDiff = diff
                minIndex = i
            i += 1
        self.nowMainRouteNum = minIndex

        self.oneSquareService = oneSquare.square()
        self.subRoute = []
        self.subRouteLen = 0
        self.nowSubRouteNum = 0

        self.drone = airsim.MultirotorClient(ip="70.12.247.95")
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
        self.drone.rotateToYawAsync(0, vehicle_name=self.name).join()
        self.drone.moveByVelocityAsync(x, y, z, c, vehicle_name=self.name).join()
        self.drone.moveByVelocityAsync(0, 0, 0, 1, vehicle_name=self.name).join()
        
    def doTracking(self, vAtFind, height):
        x = 0
        y = 0

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
            self.nowMainRouteNum = 1 if self.mainRouteLen == self.nowMainRouteNum + 1 else self.nowMainRouteNum + 1

        x = min(dx, maxLen) if dx > 0 else max(dx, -(maxLen))
        y = min(dy, maxLen) if dy > 0 else max(dy, -(maxLen))
        z = self.h - height

        self.moveToV(x, y, z)

    def doSubPatrol(self, maxLen, height, x, y):
        _ = self.getNowPosition()
        self.subRoute, self.subRouteLen = self.oneSquareService.makeRoute(self.subRoute, [x, y], 20).getRoute()

        dx = self.subRoute[self.nowSubRouteNum][0] - self.npos["x_val"]
        dy = self.subRoute[self.nowSubRouteNum][1] - self.npos["y_val"]
        if (dx**2) + (dy**2) < 10:
            self.nowSubRouteNum = 0 if self.subRouteLen == self.nowSubRouteNum + 1 else self.nowSubRouteNum + 1

        x = min(dx, maxLen) if dx > 0 else max(dx, -(maxLen))
        y = min(dy, maxLen) if dy > 0 else max(dy, -(maxLen))
        z = self.h - height

        self.moveToV(x, y, z)
    
    def capture(self, iter, cameraNum, target):
        _ = self.getNowPosition()

        # print("Now [x:{}, y:{}, z:{}]".format(self.npos["x_val"], self.npos["y_val"], self.h))

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
                if self.findCnt == 3:   # n번 이상 놓치면 찾을 수 없는 상태
                    self.isFind = False
                    self.findCnt = 0
        else:
            if self.aiResult["target_finded"]:
                self.findCnt += 1
                if self.findCnt == 1:   # n번 이상 찾아야 제대로 찾은 상태
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

        res = requests.post('http://70.12.247.45:5000/api/droneUpdate', data=datas)
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
    d = Drone(DRONE_INFOS, MAIN_SPIN)
    d.takeoff()
    i = 0

    while True:
        # print("====================== " + str(i))
        if d.isFind:
            if len(d.serverRes) >= 2:
                nearByDrone = False
                imSub = False
                subIndex = 0
                j = 0
                for res in d.serverRes:
                    num = int(res["number"]) + 1
                    num = num if num <= 3 else num % 3
                    if num == int(d.number):
                        imSub = True
                        subIndex = j
                    if not int(res["number"]) == int(d.number):
                        diffx = float(res["x"]) - d.npos["x_val"]
                        diffy = float(res["y"]) - d.npos["y_val"]
                        if (diffx**2) + (diffy**2) < 500:
                            if int(res["number"]) < int(d.number):
                                nearByDrone = True
                        
                    j += 1
                
                if nearByDrone:
                    if imSub:
                        d.doSubPatrol(MAX_MOVE_LENGTH, MAIN_HEIGHT - 1, d.serverRes[subIndex]["x"], d.serverRes[subIndex]["y"])
                    else:
                        d.doMainPatrol(MAX_MOVE_LENGTH, MAIN_HEIGHT)
                else:
                    d.doTracking(2, MAIN_HEIGHT - 2)
            else:
                # 추적(속도, 높이)
                d.doTracking(2, MAIN_HEIGHT - 2)
        else:
            if len(d.serverRes) >= 1:
                imSub = False
                subIndex = 0
                j = 0
                for res in d.serverRes:
                    num = int(res["number"]) + 1
                    num = num if num <= 3 else num % 3
                    if num == int(d.number):
                        imSub = True
                        subIndex = j
                    j += 1

                if imSub:
                    d.doSubPatrol(MAX_MOVE_LENGTH, MAIN_HEIGHT - 1, d.serverRes[subIndex]["x"], d.serverRes[subIndex]["y"])
                else:
                    d.doMainPatrol(MAX_MOVE_LENGTH, MAIN_HEIGHT)
            else:
                d.doMainPatrol(MAX_MOVE_LENGTH, MAIN_HEIGHT)
        d.capture(i, CAMERA_NAME, TARGET)
        d.postServer(i)
        i += 1

    d.landing()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

import os
import time
import requests
import numpy as np

import airsim

import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

import spin as spinSquare

# START_POS = {"x_val":60049.859375, "y_val":1822.984375, "z_val":13177.371094}
# START_POS = {"x_val":60049.859375, "y_val":-800.0, "z_val":13177.371094}
START_POS = {"x_val":-260096.0, "y_val":-260096.0, "z_val":129462.992188}
# STD_SQUARE = [
#     [60049.859375, 1822.984375],
#     [60099.859375, 1822.984375],
#     [60099.859375, 1872.984375],
#     [60049.859375, 1872.984375]
# ]
# STD_SQUARE = [
#     [60049.859375, -800.0],
#     [60080.859375, -800.0],
#     [60080.859375, -765.0],
#     [60049.859375, -765.0]    
# ]
STD_SQUARE = [
    [-260096.0, -260096.0],
    [-260126.0, -260096.0],
    [-260126.0, -260136.0],
    [-260096.0, -260136.0]    
]
NAME = "Drone1"
MIN_HEIGHT = 13
MAX_HEIGHT = 15
MAX_MOVE_LENGTH = 1
CAMERA_NAME = '3' # 아래
TARGET = 'person'

# Object Detect 객체 생성
ss = spinSquare.square(STD_SQUARE, 20, 10)
ss.makeRoute()
print(ss.getRoute())

class Drone():
    def __init__(self, name, minh, maxh, maxLen, spos):
        self.name = name
        self.minh = minh
        self.maxh = maxh
        self.maxLen = maxLen
        self.spos = spos
        self.npos = {"x_val":0., "y_val":0., "z_val":0.}
        self.type = 1   # 1은 추적 드론, 2는 근처 수색 드론, 3은 전체 수색 드론
        self.mod = 1    # 1은 map 수색, 2는 근처 수색, 3은 추적 알고리즘 적용
        # self.drone = airsim.MultirotorClient(ip="70.12.247.95")
        self.drone = airsim.MultirotorClient()
        self.drone.confirmConnection()
        self.route = ss.getRoute()
        self.routeLen = len(self.route)
        self.nowRoute = 0
        self.isFind = False
    
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

    def fly(self):
        _ = self.getNowPosition()

        # 높이 자동 조절
        z = 0
        if self.minh > self.h:
            diff = self.minh - self.h
            z = -self.maxLen if diff > self.maxLen else -diff
        if self.maxh < self.h:
            diff = self.h - self.maxh
            z = self.maxLen if diff > self.maxLen else diff

        # 현재 가고자 하는 target 위치 = route[nowRoute]
        dx = self.route[self.nowRoute][0] - self.npos["x_val"]
        dy = self.route[self.nowRoute][1] - self.npos["y_val"]
        if (dx**2) + (dy**2) < 10:
            self.nowRoute += 1
            if self.routeLen == self.nowRoute:
                self.nowRoute = 0

        x = min(dx, self.maxLen) if dx > 0 else max(dx, -(self.maxLen))
        y = min(dy, self.maxLen) if dy > 0 else max(dy, -(self.maxLen))

        self.moveToV(x, y, z)
    
    def capture(self, cameraNum, iter):
        response_image = self.drone.simGetImage(cameraNum, self.IMAGE_TYPE)
        self.np_response_image = np.asarray(bytearray(response_image), dtype="uint8")

        decoded_frame = imdecode(self.np_response_image, IMREAD_COLOR)
        
        cv2.imshow('cam', decoded_frame)
        cv2.imwrite('./tensorflow/images/missingPerson/2_{}.jpg'.format(iter), decoded_frame)
        cv2.waitKey(1)
    
    def postServer(self, i):
        datas = {
            "name" : self.name,
            "x" : self.npos["x_val"],
            "y" : self.npos["y_val"],
            "z" : self.npos["z_val"],
            "img" : self.np_response_image,
            "isFind" : self.isFind,
            "timestamp":time.time(),
            "iter":i
        }
        response = requests.post('http://localhost:5000/api/droneUpdate', data=datas)

    def getNowPosition(self):
        pos = self.drone.simGetGroundTruthKinematics(vehicle_name=self.name).position

        self.npos["x_val"] = self.spos["x_val"] + pos.x_val
        self.npos["y_val"] = self.spos["y_val"] + pos.y_val
        self.npos["z_val"] = self.spos["z_val"] - pos.z_val
        self.h = float(self.drone.getDistanceSensorData(vehicle_name=self.name, distance_sensor_name="Distance1").distance)

        print("Now Position!")
        print(self.npos["x_val"])
        print(self.npos["y_val"])
        # print(self.npos["z_val"])
        print(self.h)

        return self.npos
    
    def getRoute(self):
        return self.nowRoute
    
    def getRouteLen(self):
        return self.routeLen

d = Drone(NAME, MIN_HEIGHT, MAX_HEIGHT, MAX_MOVE_LENGTH, START_POS)

def run():
    cv2.startWindowThread()
    d.takeoff()
    i = 0

    while True:
        print("====================== " + str(i))
        d.capture(CAMERA_NAME, i)
        d.fly()
        # if d.getRoute() == 3:
        # if d.getRoute() == (routeSize - 1):
        #     break
        i += 1
        if i == 200:
          break

    d.landing()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

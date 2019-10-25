import os
import time
import requests
import numpy as np

import airsim

import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

from drone_object_detection import object_detector

from util import spin_square

START_POS = {"x_val":60049.859375, "y_val":1822.984375, "z_val":13177.371094}
STD_SQUARE = [
    [60049.859375, 1822.984375],
    [60149.859375, 1822.984375],
    [60149.859375, 1922.984375],
    [60049.859375, 1922.984375],
]
NAME = "Drone1"
MIN_HEIGHT = 10
MAX_HEIGHT = 15
MAX_MOVE_LENGTH = 3
CAMERA_NAME = '3' # 아래
TARGET = 'person'

# Object Detect 객체 생성
detector = object_detector.Detector()
ss = spin_square.square(STD_SQUARE, 20, 5)

class Drone():
    def __init__(self, name, minh, maxh, max_len, spos):
        self.name = name
        self.minh = minh
        self.maxh = maxh
        self.max_len = max_len
        self.spos = spos
        self.npos = {"x_val":0., "y_val":0., "z_val":0.}
        self.type = 1   # 1은 추적 드론, 2는 근처 수색 드론, 3은 전체 수색 드론
        self.mod = 1    # 1은 map 수색, 2는 근처 수색, 3은 추적 알고리즘 적용
        self.drone = airsim.MultirotorClient()
        self.drone.confirmConnection()
        self.route = ss.getRoute()
        self.myroute = 0
        print(len(self.route))
    
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
            z = -self.max_len if diff > self.max_len else -diff
        if self.maxh < self.h:
            diff = self.h - self.maxh
            z = self.max_len if diff > self.max_len else diff

        response_image = self.drone.simGetImage(CAMERA_NAME, self.IMAGE_TYPE)
        np_response_image = np.asarray(bytearray(response_image), dtype="uint8")

        decoded_frame = imdecode(np_response_image, IMREAD_COLOR)
        result = detector.run_object_detector(decoded_frame, TARGET)
        
        cv2.imshow('cam', result['image'])
        cv2.waitKey(1)

        # print(self.npos)
        # print(self.target)
        print("Target Number = " + str(self.myroute))
        print("target_x= " + str(self.route[self.myroute][0]))
        print("target_t= " + str(self.route[self.myroute][1]))

        dx = self.route[self.myroute][0] - self.npos["x_val"]
        dy = self.route[self.myroute][1] - self.npos["y_val"]
        if (dx**2) + (dy**2) < 10:
            self.myroute += 1

        # x = self.route[self.myroute][0] - self.npos["x_val"]
        # y = self.route[self.myroute][1] - self.npos["y_val"]
        # x = self.target["x_val"] - self.npos["x_val"]
        # y = self.target["y_val"] - self.npos["y_val"]
        print(dx)
        print(dy)
        # print()

        x = min(dx, self.max_len) if dx > 0 else max(dx, -(self.max_len))
        y = min(dy, self.max_len) if dy > 0 else max(dy, -(self.max_len))
        print(x)
        print(y)
        # print()
        # print()

        self.moveToV(x, y, z)

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
        # print(self.h)

        return self.npos
    
    def getRoute(self):
        return self.myroute

d = Drone(NAME, MIN_HEIGHT, MAX_HEIGHT, MAX_MOVE_LENGTH, START_POS)

def run():
    cv2.startWindowThread()
    d.takeoff()
    i = 0

    while True:
        print("====================== " + str(i))
        d.fly()
        if d.getRoute() == 120:
            break
        i += 1

    d.landing()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()

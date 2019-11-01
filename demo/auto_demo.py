import os
import time
import requests

import airsim

START_POS = {"x_val":60049.859375, "y_val":1822.984375, "z_val":13177.371094}
NAME = "Drone1"
MIN_HEIGHT = 10
MAX_HEIGHT = 15
MAX_MOVE_LENGTH = 1

class Drone():
    def __init__(self, name, minh, maxh, max_len, spos):
        self.name = name
        self.minh = minh
        self.maxh = maxh
        self.max_len = max_len
        self.spos = spos
        self.npos = {"x_val":0., "y_val":0., "z_val":0.}
        self.target = {"x_val":0., "y_val":0.}
        self.type = 1   # 1은 추적 드론, 2는 근처 수색 드론, 3은 전체 수색 드론
        self.mod = 1    # 1은 map 수색, 2는 근처 수색, 3은 추적 알고리즘 적용
        self.drone = airsim.MultirotorClient()
        self.drone.confirmConnection()
    
    def takeoff(self):
        self.drone.enableApiControl(True, vehicle_name=self.name)
        self.drone.armDisarm(True, vehicle_name=self.name)
        self.drone.takeoffAsync(vehicle_name=self.name).join()

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
        if self.minh > self.h:
            diff = self.minh - self.h
            up_count = diff % self.max_len

            if diff > self.max_len:
                self.moveToV(0, 0, -(self.max_len), up_count + 1)
            else:
                self.moveToV(0, 0, -(diff))
        if self.maxh < self.h:
            diff = self.h - self.maxh
            up_count = diff % self.max_len

            if diff > self.max_len:
                self.moveToV(0, 0, (self.max_len), up_count + 1)
            else:
                self.moveToV(0, 0, (diff))

        # print(self.npos)
        # print(self.target)

        x = self.target["x_val"] - self.npos["x_val"]
        y = self.target["y_val"] - self.npos["y_val"]
        # print(x)
        # print(y)
        # print()

        x = min(x, self.max_len) if x > 0 else max(x, -(self.max_len))
        y = min(y, self.max_len) if y > 0 else max(y, -(self.max_len))
        # print(x)
        # print(y)
        # print()
        # print()

        self.moveToV(x, y, 0, 2)

    def getNowPosition(self):
        pos = self.drone.simGetGroundTruthKinematics(vehicle_name=self.name).position

        self.npos["x_val"] = self.spos["x_val"] + pos.x_val
        self.npos["y_val"] = self.spos["y_val"] + pos.y_val
        self.npos["z_val"] = self.spos["z_val"] - pos.z_val
        self.h = float(self.drone.getDistanceSensorData(vehicle_name=self.name, distance_sensor_name="Distance1").distance)
        print(self.npos["x_val"])
        print(self.npos["y_val"])
        print(self.npos["z_val"])
        print(self.h)

        return self.npos

d = Drone(NAME, MIN_HEIGHT, MAX_HEIGHT, MAX_MOVE_LENGTH, START_POS)

def run():
    d.takeoff()

    for i in range(20):
        print("====================== " + str(i))
        d.fly()
        d.target["x_val"] += 5

    d.landing()

if __name__ == "__main__":
    run()

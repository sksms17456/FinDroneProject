import os
import time
import requests

import airsim

START_POS = {"x_val":60049.859375, "y_val":1822.984375, "z_val":13177.371094}
NOW_POS = {"x_val":60049.859375, "y_val":1822.984375, "z_val":13177.371094}
NAME = "Drone1"
DEFAULT_HEIGHT_MIN = 20
DEFAULT_HEIGHT_MAX = 25
MOVE_CNT = 20

drone = airsim.MultirotorClient()
drone.confirmConnection()
drone.enableApiControl(True, vehicle_name=NAME)
drone.armDisarm(True, vehicle_name=NAME)

drone.takeoffAsync(vehicle_name=NAME).join()

# 속도로 조종(정확하지는 않으나 근접함)
def moveToV(x, y, z):
    drone.moveByVelocityAsync(x, y, z, 1, vehicle_name=NAME).join()
    drone.moveByVelocityAsync(0, 0, 0, 1, vehicle_name=NAME).join()

# 좌표로 조종(별로임)
def moveToP(x, y, z):
    drone.moveToPositionAsync(
        NOW_POS["x_val"] - START_POS["x_val"] + x
        , NOW_POS["y_val"] - START_POS["y_val"] + y
        , START_POS["z_val"] - NOW_POS["z_val"] + z
        , 5, vehicle_name=NAME)

for i in range(MOVE_CNT):
    print("============================= " + str(i))
    # 맵에서의 절대 좌표
    pos = drone.simGetGroundTruthKinematics(vehicle_name=NAME).position
    NOW_POS["x_val"] = START_POS["x_val"] + pos.x_val
    NOW_POS["y_val"] = START_POS["y_val"] + pos.y_val
    NOW_POS["z_val"] = START_POS["z_val"] - pos.z_val
    map_h = float(drone.getDistanceSensorData(vehicle_name=NAME, distance_sensor_name="Distance1").distance)

    print(NOW_POS["x_val"])
    print(NOW_POS["y_val"])
    print(NOW_POS["z_val"])
    print(map_h)

    if DEFAULT_HEIGHT_MIN > map_h:
        moveToV(0, 0, -(DEFAULT_HEIGHT_MIN - map_h))
    if DEFAULT_HEIGHT_MAX < map_h:
        moveToV(0, 0, (map_h - DEFAULT_HEIGHT_MAX))

    command = input("UP = w, DOWN = s, LEFT = a, RIGHT = d")

    if command == "w":
        moveToV(5, 0, 0)
    elif command == "s":
        moveToV(-5, 0, 0)
    elif command == "d":
        moveToV(0, 5, 0)
    elif command == "a":
        moveToV(0, -5, 0)

drone.armDisarm(False, vehicle_name=NAME)
drone.reset()
drone.enableApiControl(False, vehicle_name=NAME)
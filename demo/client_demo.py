import os
import time
import requests

import airsim

drone = airsim.MultirotorClient()
drone.confirmConnection()
drone.enableApiControl(True, vehicle_name="Drone1")
drone.armDisarm(True, vehicle_name="Drone1")

drone.takeoffAsync(vehicle_name="Drone1").join()

START_POS = {"x_val":600.49859375, "y_val":18.22984375, "z_val":131.77371094}
MOVE_CNT = 3

map_x = START_POS["x_val"]
map_y = START_POS["y_val"]
map_z = START_POS["z_val"]

for i in range(MOVE_CNT):
    print("============================= " + str(i))
    # 맵에서의 절대 좌표
    pos = drone.simGetGroundTruthKinematics(vehicle_name="Drone1").position
    map_x = START_POS["x_val"] + pos.x_val
    map_y = START_POS["y_val"] + pos.y_val
    map_z = START_POS["z_val"] - pos.z_val
    # print('x = %.10f' % map_x)
    # print('y = %.10f' % map_y)
    # print('z = %.10f' % map_z)

    # drone.getDistanceSensorData()

    # print(drone.getMagnetometerData())
    # print()
    # print(drone.getBarometerData())

    # x 속도, y 속도, z 속도, 지속
    drone.moveByVelocityAsync(0, 0, -2, 1, vehicle_name="Drone1").join()
    drone.moveByVelocityAsync(0, 0, 0, 1, vehicle_name="Drone1").join()
    # 각도, 횟수
    # drone.rotateByYawRateAsync(20., 1).join()



    # req = requests.get('http://localhost:5000/coordinate', data=datas)
    # print(req)
    # print(req.text)

# drone.moveByVelocityAsync(0, 0, 0, 1).join()
time.sleep(5)
print("============================= last")
pos = drone.simGetGroundTruthKinematics(vehicle_name="Drone1").position
map_x = START_POS["x_val"] + pos.x_val
map_y = START_POS["y_val"] + pos.y_val
map_z = START_POS["z_val"] - pos.z_val
# print('x = %.10f' % map_x)
# print('y = %.10f' % map_y)
# print('z = %.10f' % map_z)
# print(drone.getMultirotorState())

drone.reset()
drone.enableApiControl(False, vehicle_name="Drone1")

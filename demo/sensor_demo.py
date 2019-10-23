import os
import time
import requests

import airsim

drone = airsim.MultirotorClient()
drone.confirmConnection()
drone.enableApiControl(True)
drone.armDisarm(True)

drone.takeoffAsync().join()

START_POS = {"x_val":600.49859375, "y_val":18.22984375, "z_val":131.77371094}
MOVE_CNT = 3

for i in range(MOVE_CNT):
    print("============================= " + str(i))
    # 맵에서의 절대 좌표
    pos = drone.simGetGroundTruthKinematics().position
    map_x = START_POS["x_val"] + pos.x_val
    map_y = START_POS["y_val"] + pos.y_val
    map_z = START_POS["z_val"] - pos.z_val
    # print('x = %.10f' % map_x)
    # print('y = %.10f' % map_y)
    # print('z = %.10f' % map_z)


    # 지형지물? 아래 지형(그냥 맵 그자체)의 정보를 가져오는 듯
    # print(drone.simGetCollisionInfo())
    # print()

    # 위도 경도 높이? 정보랑 중력 정보, 시작 위치에서의 정보를 가짐
    # print(drone.simGetGroundTruthEnvironment())
    # print()

    # 시작 위치에서의 상대 값, 속도와 가속도 정보를 가짐
    # print(drone.simGetGroundTruthKinematics())
    # print()

    # 시작 위치에서의 상대 값
    # print(drone.simGetPose())
    # print()

    # 그냥 카메라의 정보일 뿐. 시작 위치 상대 값은 나옴
    # print(drone.getCameraInfo("0"))
    # print()

    # 이래 저래 바꾸고 settings에 sensor 달고 실행중... 아래 센서를 모르겠다...
    print(drone.getDistanceSensorData("Distance1").distance)
    print()

    # 얘도 에러남... lidar name을 지정해야할듯한데 어떤걸로?
    # print(drone.getLidarData("Distance1"))
    # print()

    # x 속도, y 속도, z 속도, 지속
    drone.moveByVelocityAsync(0, 0, -1, 1).join()
    drone.moveByVelocityAsync(0, 0, 0, 1).join()
    # 각도, 횟수
    # drone.rotateByYawRateAsync(20., 1).join()
    time.sleep(2)

drone.armDisarm(False)
drone.reset()
drone.enableApiControl(False)

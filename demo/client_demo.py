import os
import time
import requests
import threading

import airsim

# drone.enableApiControl(True, vehicle_name="Drone1")
# drone.armDisarm(True, vehicle_name="Drone1")
# drone.enableApiControl(True, vehicle_name="Drone2")
# drone.armDisarm(True, vehicle_name="Drone2")

# drone.takeoffAsync(vehicle_name="Drone1").join()
# drone.takeoffAsync(vehicle_name="Drone2").join()
START_POS = {}

START_POS["Drone1"] = {"x_val":604.49859375, "y_val":18.22984375, "z_val":131.77371094}
START_POS["Drone2"] = {"x_val":608.49859375, "y_val":18.22984375, "z_val":131.77371094}

def start_drone(name=""):
    drone = airsim.MultirotorClient()
    drone.confirmConnection()

    drone.enableApiControl(True, vehicle_name=name)
    drone.armDisarm(True, vehicle_name=name)

    drone.takeoffAsync(vehicle_name=name).join()

    MOVE_CNT = 3

    for i in range(MOVE_CNT):
        print("============================= " + str(i))
        # 맵에서의 절대 좌표
        pos = drone.simGetGroundTruthKinematics(vehicle_name="Drone2").position
        map_x = START_POS[name]["x_val"] + pos.x_val
        map_y = START_POS[name]["y_val"] + pos.y_val
        map_z = START_POS[name]["z_val"] - pos.z_val
        # print('x = %.10f' % map_x)
        # print('y = %.10f' % map_y)
        # print('z = %.10f' % map_z)

        datas = {
            "name":name,
            "x":map_x,
            "y":map_y,
            "z":map_z,
        }

        _ = requests.get('http://localhost:5000/coordinate', data=datas)

        # x 속도, y 속도, z 속도, 지속
        drone.moveByVelocityAsync(0, 0, -2, 1, vehicle_name=name).join()
        drone.moveByVelocityAsync(0, 0, 0, 1, vehicle_name=name).join()
        # 각도, 횟수
        # drone.rotateByYawRateAsync(20., 1).join()
        
    drone.landAsync(vehicle_name=name)
    time.sleep(70)  

# drone.moveByVelocityAsync(0, 0, 0, 1).join()
# time.sleep(5)
# print("============================= last")
# pos = drone.simGetGroundTruthKinematics(vehicle_name="Drone2").position
# map_x = START_POS["x_val"] + pos.x_val
# map_y = START_POS["y_val"] + pos.y_val
# map_z = START_POS["z_val"] - pos.z_val
# print('x = %.10f' % map_x)
# print('y = %.10f' % map_y)
# print('z = %.10f' % map_z)
# print(drone.getMultirotorState())

# drone.landAsync(vehicle_name="Drone1")
# drone.landAsync(vehicle_name="Drone2")

# time.sleep(100)

threading.Thread(target=start_drone, args=("Drone1",)).start()
threading.Thread(target=start_drone, args=("Drone2",)).start()

# drone.reset()
# drone.enableApiControl(False, vehicle_name="Drone1")
# drone.enableApiControl(False, vehicle_name="Drone2")


"""
For connecting to the AirSim drone environment and testing API functionality
"""

import os
import sys
import tempfile
import pprint
import numpy as np
import time
import math
import requests
import airsim
import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

# from drone_object_detection import object_detector

# Object Detect 객체 생성
# detector = object_detector.Detector()

# connect to the AirSim simulator
# client = airsim.MultirotorClient(ip='70.12.247.45')
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

airsim.wait_key('Press any key to takeoff')
client.takeoffAsync()
time.sleep(0.8)

# take Video
# CAMERA_NAME = '0' # 정면
CAMERA_NAME = '3' # 아래
IMAGE_TYPE = airsim.ImageType.Scene
target_class = 'person'

cv2.startWindowThread()
def frame_generator(sec):
  x = 1
  y = 1
  z = -1.0
  v = 0.3
  x_base = 0
  y_base = 0
  z_base = 0
  temp = 1
  for i in range(sec):
      response_image = client.simGetImage(CAMERA_NAME, IMAGE_TYPE)
      np_response_image = np.asarray(bytearray(response_image), dtype="uint8")

      # decoded_frame = imdecode(np_response_image, IMREAD_COLOR)
      # result = detector.run_object_detector(decoded_frame, target_class)

      # cv2.imwrite('images/output{}.jpg'.format(i), result['image'])
      # cv2.imwrite('frontend/dist/img/output.af79af48.jpg', result['image'])
      # cv2.imwrite('frontend/src/assets/output.jpg', result['image'])
      
      # cv2.imshow('cam', result['image'])
      # cv2.imshow('cam', decoded_frame)
      datas = {
          "name":"Drone_2",
          "x":1,
          "y":2,
          "z":3,
          "img": np_response_image,
          "timestamp":time.time(),
          "iter":i
      }
      requests.post('http://70.12.247.73:5000/api/droneUpdate', data=datas)
      client.moveToPositionAsync(x_base, y_base, z_base, v)
      time.sleep(0.2)
      x_base = x_base + x
      y_base = y_base + y
      z_base = z_base + z

      # print(result['drone_controller'])
      print("iter ", i)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

frame_generator(25)
client.reset()
client.enableApiControl(False)
 
# Closes all the frames
cv2.destroyAllWindows()
# detector.closeDetector()
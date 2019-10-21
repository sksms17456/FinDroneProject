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

import airsim
import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

from drone_object_detection import object_detector
# import object_detection.object_detector as object_detector

detector = object_detector.Detector()

# connect to the AirSim simulator
# client = airsim.MultirotorClient(ip='70.12.247.95')
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

airsim.wait_key('Press any key to takeoff')
client.takeoffAsync().join()
time.sleep(0.5)

# take Video
CAMERA_NAME = '3'
IMAGE_TYPE = airsim.ImageType.Scene

cv2.startWindowThread()
def frame_generator(sec):
  x = 0
  y = 0
  z = -1
  v = 0.3
  x_base = 0
  y_base = 0
  z_base = 0
  for i in range(sec):
      response_image = client.simGetImage(CAMERA_NAME, IMAGE_TYPE)
      np_response_image = np.asarray(bytearray(response_image), dtype="uint8")
      decoded_frame = imdecode(np_response_image, IMREAD_COLOR)
      # result = imdecode(np_response_image, IMREAD_COLOR)
      result = detector.run_object_detector(decoded_frame)
      cv2.imwrite('images/output{}.jpg'.format(i), result)
      cv2.imshow('cam', result)
      client.moveToPositionAsync(x_base, y_base, z_base, v)
      time.sleep(0.09)
      x_base = x_base + x
      y_base = y_base + y
      z_base = z_base + z

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

frame_generator(400)
client.reset()
client.enableApiControl(False)
 
# Closes all the frames
cv2.destroyAllWindows()
detector.closeDetector()
"""
For connecting to the AirSim drone environment and testing API functionality
"""

import os
import tempfile
import pprint
import numpy as np
import time
import math

import airsim
import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

from flask import Flask, render_template_string, Response
import matplotlib.pyplot as plt

from object_detector import start_object_detector

import csv

# connect to the AirSim simulator
client = airsim.MultirotorClient(ip='70.12.247.95')
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

airsim.wait_key('Press any key to takeoff')
client.takeoffAsync().join()
time.sleep(0.5)

# take Video
CAMERA_NAME = ''
IMAGE_TYPE = airsim.ImageType.Scene
DECODE_EXTENSION = '.jpg'

# out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (256, 128))

frame_array = []
cv2.startWindowThread()
def frame_generator(sec):
  x = 0
  y = 0
  z = -1
  v = 0.5
  x_base = 0
  y_base = 0
  z_base = 0
  for i in range(sec):
      response_image = client.simGetImage(CAMERA_NAME, IMAGE_TYPE)
      np_response_image = np.asarray(bytearray(response_image), dtype="uint8")
      decoded_frame = imdecode(np_response_image, IMREAD_COLOR)
      # result = start_object_detector(decoded_frame)
      # out.write(decoded_frame)
      cv2.imwrite('images/output{}.jpg'.format(i), decoded_frame)
      cv2.imshow('cam', decoded_frame)
      client.moveToPositionAsync(x_base, y_base, z_base, v)
      time.sleep(1)
      x_base = x_base + x
      y_base = y_base + y
      z_base = z_base + z

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

      # cv2.imshow('cam', result)
      # cv2.waitKey(1)
      # plt.imshow(decoded_frame)
      # plt.show()

frame_generator(20)
# out.release()
client.reset()
client.enableApiControl(False)
 
# Closes all the frames
cv2.destroyAllWindows()
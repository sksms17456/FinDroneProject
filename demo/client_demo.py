import os
import tempfile
import pprint
import numpy as np

import airsim
import requests


airsim_client = airsim.MultirotorClient()
airsim_client.confirmConnection()
airsim_client.enableApiControl(True)
airsim_client.armDisarm(True)

state = airsim_client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to takeoff')
airsim_client.takeoffAsync().join()

state = airsim_client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

datas = {
    "x":50,
    "y":100,
    "z":1002
}
req = requests.get('http://localhost:5000/coordinate', data=datas)
print(req)
print(req.text)
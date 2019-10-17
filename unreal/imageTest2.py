"""
For connecting to the AirSim drone environment and testing API functionality
"""

import os
import tempfile
import pprint
import numpy as np

import airsim


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)

airsim.wait_key('Press any key to takeoff')
client.takeoffAsync().join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

# responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])
# response = responses[0]

# # get numpy array
# img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) 

# # reshape array to 4 channel image array H X W X 4
# img_rgb = img1d.reshape(response.height, response.width, 3)

# # original image is fliped vertically
# img_rgb = np.flipud(img_rgb)

# # write to png 
# airsim.write_png(os.path.normpath("filename" + '.png'), img_rgb) 
# airsim.write_file("test1.png", response.image_data_uint8)
# # airsim.write_png("test2.png", response.image_data_uint8)
# airsim.write_pfm("test2.pfm", airsim.get_pfm_array(response))


# take images
responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.DepthVis), 
    airsim.ImageRequest("1", airsim.ImageType.DepthPlanner, True)])
print('Retrieved images: %d', len(responses))

# do something with the images
for response in responses:
    if response.pixels_as_float:
        print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
        airsim.write_pfm(os.path.normpath('py1.pfm'), airsim.get_pfm_array(response))
    else:
        print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
        airsim.write_file(os.path.normpath('py1.png'), response.image_data_uint8)

airsim.wait_key('Press any key to reset to original state')
client.reset()

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)
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

airsim.wait_key('Press any key to move vehicle to (-10, 10, -10) at 5 m/s')
client.moveToPositionAsync(-10, 10, -10, 5)

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to take images')
# get camera images from the car
# responses = client.simGetImages([
#     airsim.ImageRequest(0, airsim.ImageType.DepthVis),  #depth visualiztion image
#     airsim.ImageRequest(1, airsim.ImageType.DepthPerspective, True), #depth in perspective projection
#     airsim.ImageRequest(1, airsim.ImageType.Scene), #scene vision image in png format
#     airsim.ImageRequest(1, airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGBA array
# print('Retrieved images: %d' % len(responses))

# tmp_dir = os.path.join(tempfile.gettempdir(), "airsim_drone")
# print ("Saving images to %s" % tmp_dir)
# try:
#     os.makedirs(tmp_dir)
# except OSError:
#     if not os.path.isdir(tmp_dir):
#         raise

# for idx, response in enumerate(responses):

#     filename = os.path.join(tmp_dir, str(idx))

#     if response.pixels_as_float:
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
#         airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.getPfmArray(response))
#         pass
#     elif response.compress: #png format
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#         airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
#     else: #uncompressed array
#         print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
#         img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
#         img_rgba = img1d.reshape(response.height, response.width, 3) #reshape array to 4 channel image array H X W X 4
#         img_rgba = np.flipud(img_rgba) #original image is fliped vertically
#         img_rgba[:,:,1:2] = 100 #just for fun add little bit of green in all pixels
#         airsim.write_png(os.path.normpath("tester" + '.greener.png'), img_rgba) #write to png

responses = client.simGetImages([airsim.ImageRequest("2", airsim.ImageType.Scene, False, False)])
response = responses[0]

# get numpy array
img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) 

# reshape array to 4 channel image array H X W X 4
img_rgb = img1d.reshape(response.height, response.width, 3)

# original image is fliped vertically
img_rgb = np.flipud(img_rgb)

# write to png 
airsim.write_png(os.path.normpath("filename" + '.png'), img_rgb) 


airsim.wait_key('Press any key to reset to original state')
client.reset()

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)
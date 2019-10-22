# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os
import numpy as np

# connect to the AirSim simulator 
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()

filename = "first"

# png_image = client.simGetImage("0", airsim.ImageType.Scene)
responses = client.simGetImages([
    # png format
    airsim.ImageRequest(0, airsim.ImageType.Scene), 
    # uncompressed RGBA array bytes
    airsim.ImageRequest(1, airsim.ImageType.Scene, False, False),
    # floating point uncompressed image
    airsim.ImageRequest(1, airsim.ImageType.DepthPlanner, True)])
# responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])

response = responses[0]
# get numpy array
img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) 
# reshape array to 4 channel image array H X W X 4
img_rgba = img1d.reshape(response.height, response.width, 3)  
# original image is fliped vertically
img_rgba = np.flipud(img_rgba)
# just for fun add little bit of green in all pixels
img_rgba[:,:,1:2] = 100
# write to png 
airsim.write_png(os.path.normpath(filename + '.greener.png'), img_rgba)


client.moveToPositionAsync(-10, 10, -10, 5).join()

# take images
responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.DepthVis), 
    airsim.ImageRequest("1", airsim.ImageType.DepthPlanner, True)])
print('Retrieved images: %d', len(responses))

# do something with the images
for response in responses:
    if response.pixels_as_float:
        # print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
        # airsim.write_pfm(os.path.normpath('/temp/py1.pfm'), airsim.getPfmArray(response))
        print("this is!!!!")
    else:
        print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
        airsim.write_file(os.path.normpath('/temp/py1.png'), response.image_data_uint8)
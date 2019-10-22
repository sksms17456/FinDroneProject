# Drone Controller
import numpy as np

# direction controll
def direction_controll(box, shape):
    return_dir = {}
    return_dir['x'] = None
    return_dir['y'] = None

    ymin, xmin, ymax, xmax = box
    center = [(xmax+xmin)/2., (ymax+ymin)/2.]
    area = (ymax-ymin) * (xmax-xmin)

    # 좌우
    if center[0] > 0.6:
        return_dir['x'] = "turn_right"
    elif center[0] < 0.4:
        return_dir['x'] = "turn_left"
    
    # 상하
    if center[1] > 0.6:
        return_dir['y'] = "downwards"
    elif center[1] < 0.4:
        return_dir['y'] = "upwards"
    
    # 앞뒤
    if area > 0.15:
        return_dir['moving'] = "backwards"
    elif area < 0.12:
        return_dir['moving'] = "ahead"
    
    return return_dir
import os
from flask import Flask, render_template, jsonify, request
from random import *
from flask_cors import CORS
import time

import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.normpath(os.path.join(ROOT_PATH,'frontend','dist'))
app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

drone = {
            "name" : "myDrone",
            "x":1,
            "y":2,
            "z":3,
            "img":'output.jpg',
            "timestamp":time.time()
        }
temp = 1
@app.route('/api/droneUpdate')
def update_drone():
    result = request.form
    global drone
    global temp
    print(result.getlist('img')[0])
    if temp == 1:
        cv2.imwrite('frontend/dist/img/output.af79af48.jpg', result.getlist('img')[0])
        cv2.imwrite('frontend/src/assets/output.jpg', result.getlist('img')[0])
        drone.__setitem__('img','output.jpg')
        temp = 0
    else :
        cv2.imwrite('frontend/dist/img/output1.fbb7be38.jpg', result.getlist('img')[0])
        cv2.imwrite('frontend/src/assets/output1.jpg', result.getlist('img')[0])
        drone.__setitem__('img','output1.jpg')
        temp = 1
        
    
    return drone.get('img')


@app.route('/api/getImg')
def get_Img():
    response = {
        'ImgUrl' : drone.get('img')
    }
    print(drone.get('img'))
    return jsonify(response)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()

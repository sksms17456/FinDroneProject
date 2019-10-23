import os
from flask import Flask, render_template, jsonify, request, send_file
from random import *
from flask_cors import CORS
import time

from PIL import Image
import numpy as np
import cv2
from cv2 import imdecode, imencode, IMREAD_COLOR

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.normpath(os.path.join(ROOT_PATH, 'frontend', 'dist'))
app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
drone = [
    {
        "name": "myDrone",
        "x": 1,
        "y": 2,
        "z": 3,
        "timestamp": time.time(),
        "iter": 0
    },
    {
        "name": "myDrone",
        "x": 1,
        "y": 2,
        "z": 3,
        "timestamp": time.time(),
        "iter": 0
    },
    {
        "name": "myDrone",
        "x": 1,
        "y": 2,
        "z": 3,
        "timestamp": time.time(),
        "iter": 0
    }
]

@app.route('/api/droneUpdate', methods=['GET', 'POST'])
def update_drone():
    result = request.form
    frame = np.array(result.getlist('img')).astype('uint8')
    decoded_frame = np.asarray(bytearray(frame), dtype="uint8")
    decoded_frame = imdecode(decoded_frame, IMREAD_COLOR)
    name =  result.getlist('name')[0][-1]
    cv2.imwrite("drone_output/output"+name+".jpg", decoded_frame)

    global drone
    drone[int(name)].__setitem__('iter', request.form.get('iter'))
    return name


@app.route('/api/getImg')
def get_Img():
    response = {
        'iter0': drone[0].get('iter'),
        'iter1': drone[1].get('iter'),
        'iter2': drone[2].get('iter')
    }
    return jsonify(response)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/getDroneImg')
def get_drone_img():
    drone = request.args.get('drone')
    num_img = request.args.get('num_img')

    filename = 'drone_output/output'+drone+'.jpg'
    return send_file(filename, mimetype='image/jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

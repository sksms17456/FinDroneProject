import os
import cv2
import time
import numpy as np

from PIL import Image
from cv2 import imdecode, imencode, IMREAD_COLOR
from flask import Flask, render_template, jsonify, request, send_file
from random import *
from flask_cors import CORS

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.normpath(os.path.join(ROOT_PATH, 'frontend', 'dist'))
app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

drones = [
    {
        "number" : 1,
        "x" : 0,
        "y" : 0,
        "z" : 0,
        "timestamp": time.time(),
        "iter": 0,
        "isFind": False
    },
    {
        "number" : 2,
        "x" : 0,
        "y" : 0,
        "z" : 0,
        "timestamp": time.time(),
        "iter": 0,
        "isFind": False
    },
    {
        "number" : 3,
        "x" : 0,
        "y" : 0,
        "z" : 0,
        "timestamp": time.time(),
        "iter": 0,
        "isFind": False
    }
]

@app.route('/api/getFindArea')
def get_find_area():
    for drone in drones :
        if drone["isFind"]:
            drone.__setitem__("isFind",True)
            return jsonify(drone)
    # drones[1].__setitem__("isFind", True)
    # return jsonify(drones[1])
    return jsonify({"isFind": False})

@app.route('/api/droneUpdate', methods=['GET', 'POST'])
def update_drone():
    result = request.form
    number = int(result.get('number'))

    frame = np.array(result.getlist('img')).astype('uint8')
    decoded_frame = np.asarray(bytearray(frame), dtype="uint8")
    decoded_frame = imdecode(decoded_frame, IMREAD_COLOR)
    cv2.imwrite("drone_output/output"+str(number)+".jpg", decoded_frame)

    global drones
    drones[number-1].__setitem__('iter', result.get('iter'))
    drones[number-1].__setitem__('x', float(result.get('x')))
    drones[number-1].__setitem__('y', float(result.get('y')))
    drones[number-1].__setitem__('z', float(result.get('z')))

    if result.get('isFind') == "True":
        drones[number-1].__setitem__('isFind', True)
    else :
        drones[number-1].__setitem__('isFind', False)
    
    response = []
    for drone in drones:
        if drone["isFind"]:
            response.append(drone)

    return jsonify({"list": response})


@app.route('/api/getInfo')
def get_Info():
    # response = {
    #     'iter0': drones[0].get('iter'),
    #     'iter1': drones[1].get('iter'),
    #     'iter2': drones[2].get('iter'),
    #     'pos0' : [drones[0].get('x'), drones[0].get('y'), drones[0].get('z')],
    #     'pos1' : [drones[1].get('x'), drones[1].get('y'), drones[1].get('z')],
    #     'pos2' : [drones[2].get('x'), drones[2].get('y'), drones[2].get('z')],
    #     'find0' : drones[0].get('isFind'),
    #     'find1' : drones[1].get('isFind'),
    #     'find2' : drones[2].get('isFind')        
    # }
    response = {}
    for i in range(0, 3) :
        response.__setitem__('iter{}'.format(i), drones[i].get('iter'))
        response.__setitem__('pos{}'.format(i), [drones[i].get('x'), drones[i].get('y'), drones[i].get('z')])
        response.__setitem__('find{}'.format(i), drones[i].get('isFind'))
        
    return jsonify(response)


@app.route('/api/getDroneImg')
def get_drone_img():
    drone = request.args.get('drone')
    num_img = request.args.get('num_img')

    filename = 'drone_output/output'+str(int(drone)+1)+'.jpg'
    return send_file(filename, mimetype='image/jpg')


@app.route('/')
@app.route('/central')
@app.route('/home')
@app.route('/service')
@app.route('/about')
@app.route('/rootmap')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.config["CACHE_TYPE"] = "null"
    app.run(host='0.0.0.0',port=5000)

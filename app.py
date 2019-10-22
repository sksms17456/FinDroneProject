import os
from flask import Flask, render_template, jsonify, request
from random import *
from flask_cors import CORS
import time

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

@app.route('/api/droneUpdate')
def update_drone():
    result = request.form
    print(result)
    print()
    global drone
    drone.__setitem__('img',result.getlist('img')[0])
    return drone.get('img')


@app.route('/api/getImg')
def get_Img():
    response = {
        'ImgUrl' : drone.get('img')
    }
    return jsonify(response)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()

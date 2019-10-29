from flask import Flask, request, jsonify
import time
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Drone"

@app.route('/api/droneUpdate', methods=['GET', 'POST'])
def update_drone():
    start = time.time()

    result = request.form
    # print(result.getlist('name'))
    # print(result.getlist('x'))
    # print(result.getlist('y'))
    # print(result.getlist('z'))
    # print(result.getlist('isFind'))
    # print(result.getlist('img'))
    # print(result.getlist('timestamp'))
    # print(result.getlist('iter'))

    frame = np.array(result.getlist('img')).astype('uint8')
    decoded_frame = np.asarray(bytearray(frame), dtype="uint8")
    decoded_frame = cv2.imdecode(decoded_frame, cv2.IMREAD_COLOR)
    cv2.imwrite("dd.jpg", decoded_frame)

    response = {
        "name":3,
        "x":300,
        "y":200,
        "isFind":False
    }
    end = time.time()
    print("{}번째 iter 서버 내부 걸린 시간 : {}".format(result.getlist('iter'), (end - start)))

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
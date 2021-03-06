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



    datas = [
        {
            "number":int(result.get('number')),
            "x":float(result.get('x')),
            "y":float(result.get('y')),
            "isFind":False
        },
        {
            "number":2,
            "x":5689.6681594848633,
            "y":-31701.806481838226,
            "isFind":True
        },
        {
            "number":3,
            "x":689.6681594848633,
            "y":-31701.806481838226,
            "isFind":False
        }
    ]

    if result.get('isFind') == "True":
        datas[0]["isFind"] = True

    response = []
    for data in datas:
        if data["isFind"]:
            response.append(data)

    end = time.time()
    print("{}번째 iter 서버 내부 걸린 시간 : {}".format(result.getlist('iter'), (end - start)))

    return jsonify({"list":response})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
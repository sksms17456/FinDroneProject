from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Drone"

@app.route('/coordinate')
def get_only_coordinate():
    # result = request.get_data()
    # dd =request.data
    result = request.form
    print(result.getlist('name'))
    print(result.getlist('x'))
    print(result.getlist('y'))
    print(result.getlist('z'))

    # time.sleep(5)
    # for key in result.keys():
    #     print(key)
    # print(result.keys())
    # print(result[0])

    x = {
        "command":"1",
        "distance":"100"
    }
    return str(x)

if __name__ == "__main__":
    app.run()
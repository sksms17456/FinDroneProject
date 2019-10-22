import os
import time
import requests
datas = {
            "name":"testName",
            "x":1,
            "y":2,
            "z":3,
            "img":"output2.jpg",
            "timestamp":time.time()
        }

_ = requests.get('http://localhost:5000/api/droneUpdate', data=datas)

print(_)
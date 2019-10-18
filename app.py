import os
from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS

# app = Flask(__name__,
#             static_folder="../dist/static",
#             template_folder="../dist")

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.normpath(os.path.join(ROOT_PATH,'frontend','dist'))
app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber' : randint(1, 100)
    }
    return jsonify(response)

# @app.route('/', defaults={'path':''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()

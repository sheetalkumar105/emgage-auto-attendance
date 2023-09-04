
import json
import os
import sys
from utils import Utils
from flask_cors import CORS
from flask import Flask, request, jsonify, send_from_directory
from flask import send_file
import pandas as pd



app = Flask(__name__, static_folder='public')
CORS(app)


@app.route('/runscript', methods=['POST'])
def runscript():
    data = request.json
    u = Utils()
    url = u.runScript(data)
    return jsonify({'status': 1, 'message': '', 'url': ''})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

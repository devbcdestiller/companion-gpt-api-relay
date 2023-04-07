from flask import Flask, request, jsonify
import os
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World! Flask App Deployed using Docker-Compose '

# Comment out code below in production
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai_api.api import OpenAI, list_models, create_completion
import os

VERSION = os.getenv('APP_VER')
ORG_ID = os.getenv('ORG_ID')
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
openai_API = OpenAI(ORG_ID, SECRET_KEY)


@app.route('/')
def index():
    return jsonify(version=VERSION)


@app.route(f'/api/{VERSION}/models', methods=['GET'])
def models():
    return jsonify(models=list_models(), version=VERSION)


@app.route(f'/api/{VERSION}/completion', methods=['POST'])
def completion():
    supported_models = ['text-davinci-003', 'text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001', 'davinci', 'curie', 'babbage', 'ada']
    input_prompt = request.json['input_prompt']
    model = request.json['model']
    if model not in supported_models:
        return jsonify(error=f'Requested model not supported in v1/completion. Supported models {supported_models}'), 400

    return create_completion(input_prompt, model=model)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8081')

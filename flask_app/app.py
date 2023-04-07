from flask import Flask, request, jsonify
from flask_cors import CORS
from openai_api.api import OpenAI, list_models, create_completion, create_chat_completion
import os

VERSION = os.getenv('APP_VER')
ORG_ID = os.getenv('ORG_ID')
SECRET_KEY = os.getenv('SECRET_KEY')
SYSTEM_PROMPT = 'You are CompanionGPT aka ChatGPT. Your task is to be a helpful assistant.'

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


@app.route(f'/api/{VERSION}/chat-completion', methods=['POST'])
def chat_completion():
    supported_models = ['gpt-4', 'gpt-4-0314', 'gpt-4-32k', 'gpt-4-32k-0314', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0301']
    user_input = request.json['user']
    model = request.json['model']
    if model not in supported_models:
        return jsonify(error=f'Requested model not supported in v1/chat-completion. Supported models {supported_models}'), 400

    return create_chat_completion(SYSTEM_PROMPT, user_input, model=model)


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port='8081')

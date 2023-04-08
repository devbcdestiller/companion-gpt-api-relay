from fastapi import FastAPI, Response
from openai_api.api import OpenAI, list_models, create_completion, create_chat_completion
from schemas.request.models import CompletionRq, ChatCompletionRq
import os

VERSION = os.getenv('APP_VER')
ORG_ID = os.getenv('ORG_ID')
SECRET_KEY = os.getenv('SECRET_KEY')
SYSTEM_PROMPT = 'You are CompanionGPT. Your task is to be a helpful assistant.'

app = FastAPI()
openai_API = OpenAI(ORG_ID, SECRET_KEY)


@app.get('/')
async def root():
    return {'message': f'Hi! My name is CompanionGPT {VERSION}! '}


@app.get(f'/api/{VERSION}/models')
async def models():
    return {'models': list_models(), 'version': VERSION}


@app.post(f'/api/{VERSION}/chat-completion')
async def chat_completion(payload: ChatCompletionRq, response: Response):
    supported_models = ['gpt-4', 'gpt-4-0314', 'gpt-4-32k', 'gpt-4-32k-0314', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0301']
    body = payload.dict()
    if body['model'] not in supported_models:
        response.status_code = 400
        return {'error': f'Requested model not supported in v1/chat-completion. Supported models {supported_models}'}

    return create_chat_completion(SYSTEM_PROMPT, body['user'], model=body['model'])


@app.post(f'/api/{VERSION}/completion')
def completion(payload: CompletionRq, response: Response):
    supported_models = ['text-davinci-003', 'text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001', 'davinci', 'curie', 'babbage', 'ada']
    body = payload.dict()

    if body['model'] not in supported_models:
        response.status_code = 400
        return {'error': f'Requested model not supported in v1/completion. Supported models {supported_models}'}

    return create_completion(body['input_prompt'], model=body['model'])

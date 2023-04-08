import openai


def list_models():
    return openai.Model.list()


def create_completion(prompt: str, model='text-davinci-003', max_tokens=500):
    return openai.Completion.create(model=model, prompt=prompt, max_tokens=max_tokens)


def create_chat_completion(system_prompt: str, user_prompt: str, model='gpt-3.5-turbo'):
    messages = [
        {
            'role': 'system', 'content': system_prompt
        },
        {
            'role': 'user', 'content': user_prompt
        }
    ]
    return openai.ChatCompletion.create(model=model, messages=messages)


class OpenAI:
    def __init__(self, org_id: str, secret_key: str):
        openai.organization = org_id
        openai.api_key = secret_key

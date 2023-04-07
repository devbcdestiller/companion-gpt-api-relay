import openai


def list_models():
    return openai.Model.list()


def create_completion(prompt: str, model='text-davinci-003', max_tokens=500):
    return openai.Completion.create(model=model, prompt=prompt, max_tokens=max_tokens)


class OpenAI:
    def __init__(self, org_id: str, secret_key: str):
        openai.organization = org_id
        openai.api_key = secret_key

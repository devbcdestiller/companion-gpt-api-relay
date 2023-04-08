from pydantic import BaseModel


class CompletionRq(BaseModel):
    input_prompt: str
    model: str


class ChatCompletionRq(BaseModel):
    user: str
    model: str

from pydantic import BaseModel, Field

class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message] = Field(..., min_length=1)
    model: str 



class ChatResponse(BaseModel):
    content: str
    tokens_in: int
    tokens_out: int 
    provider_name: str
    model: str 




from .base import Provider
from app.schemas import ChatResponse, ChatRequest


class FakeProvider(Provider):
    async def complete(self, request:ChatRequest) -> ChatResponse:
        return ChatResponse(
            content="This is canned response",   
            tokens_in=0, 
            tokens_out=0, 
            provider_name="fake",
            model=request.model
        )
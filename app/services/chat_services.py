from app.schemas import ChatResponse, ChatRequest
from app.providers.base import Provider

async def handle_chat(request:ChatRequest, provider:Provider) -> ChatResponse:
    return await provider.complete(request=request)
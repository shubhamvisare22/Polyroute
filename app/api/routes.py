from fastapi import APIRouter
from app.schemas import ChatResponse, ChatRequest
from app.providers.fake import FakeProvider
from app.services.chat_services import handle_chat

router = APIRouter()

@router.post("/v1/chat", response_model=ChatResponse)
async def chat(request:ChatRequest) -> ChatResponse:
    provider = FakeProvider()
    return await handle_chat(request, provider)
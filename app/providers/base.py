from abc import ABC, abstractmethod
from app.schemas import ChatRequest, ChatResponse

class Provider(ABC):
    @abstractmethod
    async def complete(self, request:ChatRequest) -> ChatResponse:
        """Send a chat request to LLM and get Normalized response"""
        raise NotImplementedError



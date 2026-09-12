import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_chat_returns_fake_response():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/v1/chat",
            json={"messages": [{"role": "user", "content": "hi"}], "model": "gpt-4"},
        )
    assert response.status_code == 200
    body = response.json()
    assert body["provider_name"] == "fake"
    assert body["model"] == "gpt-4"
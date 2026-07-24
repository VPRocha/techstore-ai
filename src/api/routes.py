from fastapi import APIRouter

from src.api.schemas import ChatRequest, ChatResponse
from src.services.chat_service import chat

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok"
    }


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    answer = chat(request.question)

    return ChatResponse(
        answer=answer
    )
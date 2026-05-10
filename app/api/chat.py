from fastapi import APIRouter, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import simple_chat
router = APIRouter()

@router.post('', response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(reply=simple_chat(request.message))
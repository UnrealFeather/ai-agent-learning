from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.tool_agent_service import tool_chat

router = APIRouter()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = tool_chat(request.message)
    return ChatResponse(reply=reply)
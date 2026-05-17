from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import simple_chat
from app.services.llm_service import stream_llm

router = APIRouter()


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = simple_chat(request.message, request.conversation_id)

    return ChatResponse(reply=reply)


@router.post("/stream")
def stream_chat(request: ChatRequest):
    def event_generator():
        for chunk in stream_llm(request.message):
            yield f"data: {chunk}\n\n"

        yield "data: END\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )

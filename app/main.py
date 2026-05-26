from fastapi import FastAPI
from app.api import chat, order, agent, interview, tool_chat

app = FastAPI(title="AI Agent Learning Backend")

app.include_router(order.router, prefix="/orders", tags=["order"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(agent.router, prefix="/agent", tags=["agent"])
app.include_router(interview.router, prefix="/interview", tags=["interview"])
app.include_router(tool_chat.router, prefix="/tool-chat", tags=["Tool Chat"])


@app.get("/health")
def health_check():
    return {"status": "ok"}

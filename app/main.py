from fastapi import FastAPI
from app.api import chat, order, agent, interview

app = FastAPI(title="AI Agent Learning Backend")

app.include_router(order.router, prefix="/orders", tags=["order"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(agent.router, prefix="/agent", tags=["agent"])
app.include_router(interview.router, prefix="/interview", tags=["interview"])


@app.get("/health")
def health_check():
    return {"status": "ok"}

from fastapi import FastAPI
from app.api import chat, order

app = FastAPI(title="AI Agent Learning Backend")

app.include_router(order.router, prefix="/orders", tags=["order"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])


@app.get("/health")
def health_check():
    return {"status": "ok"}

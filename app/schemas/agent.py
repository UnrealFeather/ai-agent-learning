from pydantic import BaseModel
from typing import Literal


class AgentRequest(BaseModel):
    message: str


class AgentResponse(BaseModel):
    reply: str
    tool_called: bool
    tool_name: str | None = None


class IntentResult(BaseModel):
    intent: Literal["chat", "query_order", "interview"]
    need_tool: bool
    tool_name: str | None = None
    order_id: str | None = None
    reason: str

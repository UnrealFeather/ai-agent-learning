from pydantic import BaseModel

class AgentRequest(BaseModel):
    message: str

class AgentResponse(BaseModel):
    reply: str
    tool_called: bool
    tool_name: str | None = None
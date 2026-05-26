from pydantic import BaseModel
from typing import Any

class ToolParameter(BaseModel):
    type: str
    description: str


class ToolDefinition(BaseModel):
    name: str
    description: str
    parameters: dict[str, ToolParameter]


class ToolCallRequest(BaseModel):
    name: str
    arguments: dict[str, Any]


class ToolResult(BaseModel):
    tool_name: str
    success: bool
    result: Any
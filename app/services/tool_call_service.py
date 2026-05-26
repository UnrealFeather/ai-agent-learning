import json
from openai import OpenAI

from app.core.config import settings
from app.tools.registry import get_openai_tools

client = OpenAI(
    api_key=settings.api_key,
    base_url=settings.base_url,
)


def request_tool_call(message: str):
    response = client.chat.completions.create(
        model=settings.model,
        messages=[{"role": "user", "content": message}],
        tools=get_openai_tools(),
        tool_choice="auto",
    )

    return response

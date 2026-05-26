import json
from openai import OpenAI

from app.core.config import settings
from app.tools.registry import get_openai_tools
from app.services.tool_executor import execute_tool_calls

client = OpenAI(
    api_key=settings.api_key,
    base_url=settings.base_url,
)


def tool_chat(message: str):
    response = client.chat.completions.create(
        model=settings.model,
        messages=[{"role": "user", "content": message}],
        tools=get_openai_tools(),
        tool_choice="auto",
    )

    assistant_message = response.choices[0].message

    # 没有工具调用
    if not assistant_message.tool_calls:
        return assistant_message.content

    # 执行工具
    tool_results = execute_tool_calls(assistant_message.tool_calls)

    # 构建第二次 messages
    messages = [{"role": "user", "content": message}, assistant_message.model_dump()]

    # 添加 tool response
    for tool_call, tool_result in zip(assistant_message.tool_calls, tool_results):
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result, ensure_ascii=False),
            }
        )

    # 第二次模型调用
    final_response = client.chat.completions.create(
        model=settings.model, messages=messages
    )

    return final_response.choices[0].message.content

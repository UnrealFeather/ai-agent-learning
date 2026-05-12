import json
from openai import OpenAI
from app.core.config import settings
from app.schemas.agent import IntentResult
from app.services.prompt_service import build_intent_prompt

client = OpenAI(
    api_key=settings.api_key,
    base_url=settings.base_url,
)


def detect_intent(message: str) -> IntentResult:

    prompt = build_intent_prompt(message) + """
    请只返回 JSON，不要返回 Markdown，不要使用 ```json 包裹。

    JSON 格式如下：
    {
    "intent": "chat | query_order | interview",
    "need_tool": true,
    "tool_name": "query_order 或 null",
    "order_id": "订单号或 null",
    "reason": "判断原因"
    }
    """
    response = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": "你是一个严格输出 JSON 的意图识别模块。"},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content
    data = json.loads(content)

    return IntentResult(**data)

from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=settings.api_key,
    base_url=settings.base_url,
)


def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=settings.model,
        messages=[
            {"role": "system", "content": "你是一个 Python Agent 开发学习助手。"},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )
    print("settings.model", settings.model, settings.api_key, settings.base_url)
    return response.choices[0].message.content

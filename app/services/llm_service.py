import time
import random

from openai import OpenAI
from app.core.config import settings
from app.core.logger import logger

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


def ask_llm_messages(messages: list[dict]) -> str:
    response = client.chat.completions.create(
        model=settings.model,
        messages=messages,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )
    return response.choices[0].message.content


def ask_llm_safe(prompt: str, max_retries=3) -> str:
    for attempt in range(max_retries):
        try:
            return ask_llm(prompt)
        except Exception as error:
            logger.exception(f"LLM 调用失败，尝试 {attempt+1} 次， {error}")

            if attempt == max_retries - 1:
                return "抱歉，AI 服务暂时不可用，请稍后再试。"

            sleep_seconds = 1 + random.random()
            time.sleep(sleep_seconds)

        return "抱歉，AI 服务暂时不可用，请稍后再试。"


def ask_llm_messages_safe(messages: list[dict], max_retries=3) -> str:
    for attempt in range(max_retries):
        try:
            return ask_llm_messages(messages)
        except Exception as error:
            logger.exception(f"LLM 多轮对话调用失败，第 {attempt + 1} 次")

            if attempt == max_retries - 1:
                return "抱歉，AI 服务暂时不可用，请稍后再试。"

            sleep_seconds = 1 + random.random()
            time.sleep(sleep_seconds)

    return "抱歉，AI 服务暂时不可用，请稍后再试。"


def stream_llm(prompt: str):
    try:
        stream = client.chat.completions.create(
            model=settings.model,
            messages=[
                {
                    "role": "system",
                    "content": "你是一个 Python Agent 开发学习助手。请用中文回答。",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            stream=True,
        )

        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
                
    except Exception as error:
        logger.exception("LLM 流式调用失败")
        yield "抱歉，AI 服务暂时不可用，请稍后再试。"
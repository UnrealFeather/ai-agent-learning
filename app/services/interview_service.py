import json
from openai import OpenAI
from pydantic import ValidationError

from app.core.config import settings
from app.core.logger import logger
from app.schemas.interview import InterviewQuestionResponse, EvaluateAnswerResponse
from app.services.prompt_service import (
    build_interview_question_prompt,
    build_evaluate_answer_prompt,
)

client = OpenAI(
    api_key=settings.api_key,
    base_url=settings.base_url,
)


def _load_json(content: str) -> dict:
    """
    将模型返回内容转换为 dict。
    理论上 response_format=json_object 会返回纯 JSON，
    这里做一层兼容，避免模型偶尔返回 Markdown 包裹。
    """

    content = content.strip()
    if content.startswith("```json"):
        content = content.removeprefix("```json").removesuffix("```").strip()

    if content.startswith("```"):
        content = content.removeprefix("```").removesuffix("```").strip()
    data = json.loads(content)
    return data


def generate_interview_questions(
    resume: str, job: str, count: int = 3
) -> InterviewQuestionResponse:
    prompt = build_interview_question_prompt(resume, job, count)

    response = client.chat.completions.create(
        model=settings.model,
        messages=[
            {
                "role": "system",
                "content": "你是一个严格输出 JSON 的技术面试官。",
            },
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        stream=False,
    )

    content = response.choices[0].message.content

    try:
        data = _load_json(content)
        return InterviewQuestionResponse(**data)
    except ValidationError:
        logger.error("JSON 解析错误: %s", content)
        raise ValidationError("JSON 解析错误")


def evalute_answer(question: str, answer: str) -> EvaluateAnswerResponse:
    prompt = build_evaluate_answer_prompt(question, answer)

    response = client.chat.completions.create(
        model=settings.model,
        messages=[
            {
                "role": "system",
                "content": "你是一个严格输出 JSON 的技术面试官。",
            },
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        stream=False,
    )
    content = response.choices[0].message.content

    try:
        data = _load_json(content)
        return EvaluateAnswerResponse(**data)
    except ValidationError:
        logger.error("JSON 解析错误: %s", content)
        raise ValidationError("JSON 解析错误")

from app.services.prompt_service import (
    build_chat_prompt,
    build_intent_prompt,
    build_interview_question_prompt,
    build_evaluate_answer_prompt,
)


def test_build_chat_prompt():
    prompt = build_chat_prompt("什么是 Agent？")

    assert "什么是 Agent" in prompt
    assert "中文" in prompt


def test_build_intent_prompt():
    prompt = build_intent_prompt("帮我查订单 1001")

    assert "query_order" in prompt
    assert "订单" in prompt


def test_build_interview_questions_prompt():
    prompt = build_interview_question_prompt(
        resume="熟悉 React 和 AI 辅助研发",
        job="前端开发工程师",
        count=3,
    )

    assert "3" in prompt
    assert "前端开发工程师" in prompt
    assert "React" in prompt


def test_build_evaluate_answer_prompt():
    prompt = build_evaluate_answer_prompt(
        question="什么是 React 组件化？",
        answer="把页面拆成组件。",
    )

    assert "React 组件化" in prompt
    assert "把页面拆成组件" in prompt

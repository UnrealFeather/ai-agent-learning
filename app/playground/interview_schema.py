from app.schemas.interview import (
    InterviewQuestionRequest,
    InterviewQuestion,
    InterviewQuestionResponse,
    EvaluateAnswerRequest,
    EvaluateAnswerResponse,
)

request = InterviewQuestionRequest(
    resume="熟悉 React、Vue、TypeScript，有 AI 辅助研发经验。",
    job="前端开发工程师",
    count=3,
)

print(request.model_dump())

response = InterviewQuestionResponse(
    question=[
        InterviewQuestion(
            question="你在项目中如何使用 AI 编程工具提升研发效率？",
            difficulty="中等",
            point="考察 AI 辅助研发理解和实践能力",
            reference_answer="可以从 Prompt 设计、代码生成、代码 Review、测试用例生成等方面回答。",
        ),
    ],
)

print(response.model_dump())

evaluate_request = EvaluateAnswerRequest(
    question="你如何理解 React 组件化？",
    answer="我会把页面拆成多个组件。",
)

print(evaluate_request.model_dump())

evaluate_response = EvaluateAnswerResponse(
    score=80,
    strengths=["回答方向正确", "能体现基础理解"],
    weaknesses=["缺少复杂业务场景", "缺少工程化细节"],
    improved_answer="React 组件化是将页面拆分为可复用、可维护的 UI 单元...",
)

print(evaluate_response.model_dump())

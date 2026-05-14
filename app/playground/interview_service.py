from app.services.interview_service import generate_interview_questions, evalute_answer

resume = """
前端开发工程师，熟悉 React、Vue、TypeScript。
参与过后台管理系统、动态表单、数据可视化项目。
熟练使用 Claude Code、Codex 等 AI 编程工具，
能够通过结构化 Prompt 进行代码生成、组件逻辑补全、代码 Review 和测试用例生成
"""

result = generate_interview_questions(
    resume=resume,
    job="前端开发工程师",
    count=1,
)

print("生成面试题")
print(result.model_dump())


evalute_result = evalute_answer(
    question="你在项目中如何使用 AI 工具提升研发效率？",
    answer="我会用 AI 帮我生成代码，也会让它帮我检查问题。",
)

print("评估回答")
print(evalute_result.model_dump())

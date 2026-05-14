def build_chat_prompt(message: str) -> str:
    return f"""
    你是一个 Python Agent 开发学习助手。
    请用中文、简洁、清晰地回答用户问题。
    回答要求：
    1. 使用中文
    2. 适合初学者
    3. 解释清楚
    4. 涉及代码时给出简单示例

    用户问题：
    {message}
    """


def build_intent_prompt(message: str) -> str:
    return f"""
   你是一个 Agent 意图识别模块。

    请判断用户输入属于哪种类型：
    - chat：普通聊天或技术问答
    - query_order：查询订单
    - interview：生成面试题、参考答案或面试建议

    要求：
    - 如果是查询订单，请提取订单号
    - 不要编造订单号
    - 简短说明判断原因

    用户输入：
    {message}
    """


def build_interview_question_prompt(resume: str, job: str, count: int) -> str:
    return f"""
    你是一名资深技术面试官。

    请根据候选人的简历和目标岗位，生成 {count} 个面试问题。
    
    要求：
    1. 问题必须贴合简历内容
    2. 覆盖技术基础、项目经验、工程能力、AI 辅助研发
    3. 每个问题包含：问题、难度、考察点、参考答案
    4. 不要编造简历中没有的项目经历
    5. 必须只返回 JSON，不要返回 Markdown，不要使用 ```json 包裹
    
    返回 JSON 格式必须是：
    {{
    "questions": [
        {{
        "question": "问题内容",
        "difficulty": "简单/中等/困难",
        "point": "考察点",
        "reference_answer": "参考答案"
        }}
    ]
    }}

    候选人简历：
    {resume}

    目标岗位：
    {job}
    """
    
def build_evaluate_answer_prompt(question: str, answer: str) -> str:
    return f"""
    你是一名技术面试官。

    请评估候选人对面试问题的回答。

    评分标准：
    1. 技术准确性
    2. 表达清晰度
    3. 是否结合项目经验
    4. 是否体现工程化思维
    5. 是否有 AI 辅助研发理解，若问题相关

    要求：
    1. 分数范围是 0 到 100
    2. strengths 至少 2 条
    3. weaknesses 至少 2 条
    4. improved_answer 要像真实面试参考答案
    5. 必须只返回 JSON，不要返回 Markdown，不要使用 ```json 包裹

    返回 JSON 格式必须是：
    {{
    "score": 80,
    "strengths": ["优点1", "优点2"],
    "weaknesses": ["不足1", "不足2"],
    "improved_answer": "优化后的参考回答"
    }}

    面试问题：
    {question}

    候选人回答：
    {answer}
    """

from pydantic import BaseModel, Field


class InterviewQuestionRequest(BaseModel):
    resume: str = Field(description="候选人的简历内容")
    job: str = Field(description="目标岗位，例如：前端开发工程师")
    count: int = Field(default=5, description="面试问题数量，默认5个")


class InterviewQuestion(BaseModel):
    question: str = Field(description="面试问题")
    difficulty: str = Field(description="问题难度，例如：简单、中等、困难")
    point: str = Field(description="考察点")
    reference_answer: str = Field(description="参考答案")

class InterviewQuestionResponse(BaseModel):
    question: list[InterviewQuestion] = Field(description="面试问题列表")

class EvaluateAnswerRequest(BaseModel):
    question: str = Field(description="面试问题")
    answer: str = Field(description="候选人的回答")


class EvaluateAnswerResponse(BaseModel):
    score: int = Field(description="评分，0 到 100")
    strengths: list[str] = Field(description="回答中的优点")
    weaknesses: list[str] = Field(description="回答中的不足")
    improved_answer: str = Field(description="优化后的参考回答")
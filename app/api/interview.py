from fastapi import APIRouter, HTTPException

from app.schemas.interview import (
    InterviewQuestionRequest,
    InterviewQuestion,
    InterviewQuestionResponse,
    EvaluateAnswerRequest,
    EvaluateAnswerResponse,
)

from app.services.interview_service import (
    generate_interview_questions,
    evalute_answer,
)

router = APIRouter()


@router.post("/questions", response_model=InterviewQuestionResponse)
def create_questions(request: InterviewQuestionRequest):
    try:
        return generate_interview_questions(
            resume=request.resume,
            job=request.job,
            count=request.count,
        )
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )


@router.post("/evaluate", response_model=EvaluateAnswerResponse)
def evaluate(request: EvaluateAnswerRequest):
    try:
        return evalute_answer(
            question=request.question,
            answer=request.answer,
        )
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error),
        )
from fastapi import APIRouter, Depends
from app.schemas.agent import AgentRequest, AgentResponse
from app.services.agent_service import run_agent

router = APIRouter();

@router.post('/run', response_model=AgentResponse)
def run_agent_api(request: AgentRequest):
    result = run_agent(request.message)
    return AgentResponse(**result)

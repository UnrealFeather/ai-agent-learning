from app.services.llm_service import ask_llm
from app.services.prompt_service import build_chat_prompt, build_intent_prompt


def simple_chat(message: str) -> str:
    prompt = build_chat_prompt(message)
    return ask_llm(prompt)

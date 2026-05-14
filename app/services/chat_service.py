from app.services.llm_service import ask_llm, ask_llm_messages
from app.services.prompt_service import build_chat_prompt, build_intent_prompt
from app.services.conversation_service import add_message, get_messages


def simple_chat(message: str, conversation_id: str = "default") -> str:
    add_message(conversation_id, "user", message)
    messages = [
        {
            "role": "system",
            "content": "你是一个 Python Agent 开发学习助手。请用中文回答，适合初学者理解。",
        },
        *get_messages(conversation_id),
    ]

    reply = ask_llm_messages(messages)
    add_message(conversation_id, "assistant", reply)
    
    return reply

from app.services.llm_service import ask_llm

reply = ask_llm("用一句话解释什么是 AI Agent")
print(reply)

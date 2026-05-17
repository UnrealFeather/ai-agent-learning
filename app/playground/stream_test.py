from app.services.llm_service import stream_llm

for chunk in stream_llm("请解释 RAG 的完整流程"):
    print(chunk, end="", flush=True)

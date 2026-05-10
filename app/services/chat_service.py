def simple_chat(message: str) -> str:
    if "你好" in message:
        return "你好，我是 Mini Agent."
    else:
        return f"你说的是：{message}"
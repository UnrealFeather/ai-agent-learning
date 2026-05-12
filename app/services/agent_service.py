import re
from app.core.logger import logger
from app.services.intent_service import detect_intent
from app.services.order_service import query_order
from app.services.chat_service import simple_chat


def run_agent(message: str) -> dict:
    logger.info(f"收到用户消息：{message}")
    intent = detect_intent(message)
    
    logger.info(f"识别到意图：{intent.model_dump()}")
    
    if intent.intent == "query_order" and intent.order_id:
        result = query_order(intent.order_id)
        if not result["success"]:
            return {
                "reply": result["message"],
                "tool_called": True,
                "tool_name": "query_order",
            }

        order = result["data"]
        return {
            "reply": f"订单{intent.order_id} 当前状态是：{order['status']}, 订单金额是：{order['amount']}元",
            "tool_called": True,
            "tool_name": "query_order",
        }

    return {"reply": simple_chat(message), "tool_called": False, "tool_name": None}



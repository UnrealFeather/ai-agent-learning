import re
from app.services.order_service import query_order
from app.services.chat_service import simple_chat
from app.core.logger import logger


def run_agent(message: str) -> dict:
    order_match = re.search(r"\d+", message)

    if "订单" in message and order_match:
        order_id = order_match.group()
        logger.info(f"查询订单{order_id} 准备调用工具 query_order")
        result = query_order(order_id)
        if not result["success"]:
            return {
                "reply": result["message"],
                "tool_called": True,
                "tool_name": "query_order",
            }

        order = result["data"]
        return {
            "reply": f"订单{order_id} 当前状态是：{order['status']}, 订单金额是：{order['amount']}元",
            "tool_called": True,
            "tool_name": "query_order",
        }

    return {"reply": simple_chat(message), "tool_called": False, "tool_name": None}

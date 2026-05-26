from app.tools.base import BaseTool
from app.services.order_service import query_order


class QueryOrderTool(BaseTool):
    name = "query_order"
    description = "查询订单状态"

    def execute(self, **kwargs):
        order_id = kwargs.get("order_id")
        return query_order(order_id)

    def to_openai_tool(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "订单号"}
                    },
                    "required": ["order_id"],
                },
            },
        }

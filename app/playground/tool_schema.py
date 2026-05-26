from app.schemas.tool import ToolDefinition

tool = ToolDefinition(
    name="query_order",
    description="查询订单状态",
    parameters={
        "order_id": {
            "type": "string",
            "description": "订单号"
        }
    }
)

print(tool.model_dump())
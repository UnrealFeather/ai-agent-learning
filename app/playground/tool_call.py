from app.services.tool_call_service import request_tool_call

response = request_tool_call("帮我查订单 1001")

print(response)
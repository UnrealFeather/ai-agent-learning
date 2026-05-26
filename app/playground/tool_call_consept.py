def simulate_tool_call(user_message: str):
    print(f"用户输入: {user_message}")

    if "订单" in user_message:
        tool_call = {
            "name": "query_order",
            "arguments": {
                "order_id": "1001"
            }
        }

        print("LLM 决定调用工具:")
        print(tool_call)

        result = {
            "order_id": "1001",
            "status": "已发货"
        }

        print("工具执行结果:")
        print(result)

        final_answer = f"订单 {result['order_id']} 当前状态是：{result['status']}"

        print("最终回答:")
        print(final_answer)


simulate_tool_call("帮我查订单 1001")
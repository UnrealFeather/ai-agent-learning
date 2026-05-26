import json

from app.tools.registry import get_tool


def execute_tool_calls(tool_calls):
    results = []

    for call in tool_calls:
        name = call.function.name
        arguments = json.loads(call.function.arguments)

        tool = get_tool(name)

        if tool:
            result = tool.execute(**arguments)

            results.append({"tool_name": name, "result": result})

    return results

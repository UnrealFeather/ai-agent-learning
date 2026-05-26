from app.tools.order_tools import QueryOrderTool
from app.tools.weather_tools import WeatherTool


TOOLS = {
    "query_order": QueryOrderTool(),
    "get_weather": WeatherTool(),
}


def get_tool(name: str):
    return TOOLS.get(name)


def get_openai_tools():
    return [
        tool.to_openai_tool() for tool in TOOLS.values()
    ]
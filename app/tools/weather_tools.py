from app.tools.base import BaseTool


class WeatherTool(BaseTool):
    name = "get_weather"
    description = "查询城市天气"

    def execute(self, **kwargs):
        city = kwargs.get("city")

        weather_data = {
            "北京": "晴 26°C",
            "上海": "多云 24°C",
            "深圳": "小雨 29°C"
        }

        return weather_data.get(city, "暂无天气数据")

    def to_openai_tool(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string"
                        }
                    },
                    "required": ["city"]
                }
            }
        }
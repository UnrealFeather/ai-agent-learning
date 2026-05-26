from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str
    description: str

    @abstractmethod
    def execute(self, **kwargs):
        pass

    @abstractmethod
    def to_openai_tool(self):
        pass
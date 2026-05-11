import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    api_key: str = os.getenv("API_KEY")
    model: str = os.getenv("MODEL")
    base_url: str = os.getenv("BASE_URL")


settings = Settings()

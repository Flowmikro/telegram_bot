import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

load_dotenv(verbose=True)


class Settings(BaseSettings):
    """
    Настройки проекта
    """
    # TG
    TOKEN: str = os.getenv("BOT_TOKEN")


settings = Settings()

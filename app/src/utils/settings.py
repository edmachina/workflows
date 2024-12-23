import os
from typing import Optional

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Env
    APP_ENV: str = os.getenv('APP_ENV')
    APP_PATH: Optional[str] = os.getenv('APP_PATH')

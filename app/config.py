import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_URL: str = "https://api.trello.com/1"
    KEY_AUTH: str = os.environ.get("KEY_AUTH")
    TOKEN_AUTH: str = os.environ.get("TOKEN_AUTH")


settings = Settings()

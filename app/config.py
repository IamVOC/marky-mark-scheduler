from pydantic_settings import BaseSettings, SettingsConfigDict

from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')

    REDIS_DB: str
    REDIS_HOST: str
    REDIS_PORT: int
    TIMEZONE: str
    GROUP_IDS: List[int]

    @property
    def REDIS_URL(self) -> str:
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}'

@lru_cache
def get_settings() -> Settings:
    return Settings()


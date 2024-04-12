from pydantic_settings import BaseSettings, SettingsConfigDict

from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    REDIS_NAME: str
    REDIS_HOST: str
    REDIS_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    TOKEN: str
    TIMEZONE: str

    @property
    def REDIS_URL(self) -> str:
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_NAME}'

    @property
    def DB_URL(self) -> str:
        return f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def TELEGRAM_URL(self) -> str:
        return f'https://api.telegram.org/bot{self.TOKEN}'

@lru_cache
def get_settings() -> Settings:
    return Settings()


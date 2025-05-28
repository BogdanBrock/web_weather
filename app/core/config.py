"""Модуль для настройки приложения."""

from pathlib import Path

from httpx import AsyncClient
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс для настройки переменных окружения."""

    POSTGRES_DB: str = 'postgres_db'
    POSTGRES_USER: str = 'postgres_user'
    POSTGRES_PASSWORD: str = 'password12345'
    POSTGRES_HOST: str = '127.0.0.1'
    POSTGRES_PORT: int = 5432
    SECRET_KEY: str = 'ASD2S31SDJH213JSFJSJQWEASDJ3J12JSD4J12'
    ALGHORITM: str = 'HS256'
    TOKEN_EXPIRATION: int = 3600

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent / '.env'
    )

    @property
    def postgres_url(self):
        """Атрибут для подключения postgresql."""
        return (
            'postgresql+asyncpg://'
            f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'
        )


settings = Settings()

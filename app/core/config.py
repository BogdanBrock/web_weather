"""Модуль для настройки приложения."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Класс для настройки переменных окружения."""

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXPIRATION: int

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

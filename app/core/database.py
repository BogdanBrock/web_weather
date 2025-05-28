"""Модуль для настройки БД."""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncAttrs,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .config import settings

async_engine = create_async_engine(settings.postgres_url, echo=True)

async_session_maker = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Функция для создания сессий."""
    async with async_session_maker() as session:
        yield session


class Base(AsyncAttrs, DeclarativeBase):
    """Базовая модель Base."""

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

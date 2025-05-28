"""Модуль для создания CRUD-операций для пользователя."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User

from .base import CRUDBase


class CRUDUser(CRUDBase):
    """Класс для создания CRUD-операций для пользователя."""

    async def get_user_by_username(
        self,
        username: str,
        session: AsyncSession
    ) -> User:
        """Метод для получения пользователя по имени пользователя."""
        user = await session.execute(
            select(User).where(User.username == username)
        )
        return user.scalar()


crud_user = CRUDUser(User)

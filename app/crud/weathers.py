"""Модуль для создания CRUD операций для погоды."""

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User, Weather

from .base import CRUDBase


class CRUDWeather(CRUDBase):
    """Класс для создания CRUD-операций для погоды."""

    async def get_last_name_city_for_user(
        self,
        user: User,
        session: AsyncSession
    ) -> Weather:
        """Метод для получения название города по последнему прогнозу."""
        subquery = (
            select(func.max(Weather.id)).
            where(Weather.user_id == user.id).
            scalar_subquery()
        )
        city = await session.execute(
            select(Weather.city).
            where(Weather.id == subquery)
        )
        return city.scalar()

    async def get_cities_and_count_queries(self, session: AsyncSession):
        """Метод для получения общего количества запросов для городов."""
        result = await session.execute(
            select(Weather.city, func.count()).
            group_by(Weather.city)
        )
        return result.mappings().all()


crud_weather = CRUDWeather(Weather)

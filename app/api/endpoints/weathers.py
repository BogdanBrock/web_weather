"""Маршрут для создания endpoints."""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import weather_service
from app.core.database import db_session
from app.core.security import get_current_user
from app.crud import crud_weather
from app.models import User
from app.schemas import WeatherQueryCountReadSchema, WeatherReadSchema

router = APIRouter()


@router.get('/home/', response_model=str)
async def get_home(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для получения главное страницы."""
    return await weather_service.get_home(user, session)


@router.get('/weather/', response_model=WeatherReadSchema)
async def get_weather(
    city: str = Query(
        description=(
            'Поиск работает регистронезависимо и по частичному совпадению. '
            'Так же, если в названии города присутствуют символы, надо их '
            'соблюдать. Пример: "Ростов-на-Дону".'
        )
    ),
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для получения погоды."""
    return await weather_service.get_weather(city, user, session)


@router.get('/history/', response_model=list[WeatherReadSchema])
async def get_history(user: User = Depends(get_current_user)):
    """Маршрут для получения истории погоды для пользователя."""
    return await user.awaitable_attrs.weathers


@router.get(
    '/count-queries/',
    response_model=list[WeatherQueryCountReadSchema]
)
async def get_count_queries(session: AsyncSession = Depends(db_session)):
    """Маршрут для получения общего количества запросов для разных городов."""
    return await crud_weather.get_cities_and_count_queries(session)

"""Маршрут для создания endpoints."""

from fastapi import APIRouter, Query

from app.api.services import weather_service

router = APIRouter()


@router.get('/')
async def home():
    """Маршрут для получения главное страницы."""
    return 'Здравствуйте, это главная страница'


@router.get('/weather/')
async def get_weather(city: str = Query()):
    """Маршрут для получения погода."""
    return await weather_service.get_weather(city)

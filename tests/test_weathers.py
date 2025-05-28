"""Модуль создания тестов для продуктов."""

from http import HTTPStatus

import pytest
from httpx import AsyncClient
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Weather
from .fixtures.fixture_weathers import WEATHER_URL
from .utils import check_db_fields


@pytest.mark.asyncio
async def test_auth_user_can_get_home(user_client: AsyncClient):
    """Тест для проверки получения главной страницы."""
    url = WEATHER_URL + 'home/'
    response = await user_client.get(url)
    assert response.status_code == HTTPStatus.OK, response.json()


@pytest.mark.asyncio
async def test_auth_user_can_get_weather(
    user_client: AsyncClient,
    test_db_session: AsyncSession
):
    """Тест для проверки получения прогноза погоды."""
    url = WEATHER_URL + 'weather/'
    response = await user_client.get(url, params={'city': 'Ростов-на-Дону'})
    assert response.status_code == HTTPStatus.OK, response.json()
    count = await test_db_session.scalar(
        select(func.count()).select_from(Weather)
    )
    assert count == 1


@pytest.mark.asyncio
async def test_auth_user_can_get_history(user_client: AsyncClient):
    """Тест для проверки маршрута получения истории."""
    response = await user_client.get(WEATHER_URL + 'history/')
    assert response.status_code == HTTPStatus.OK, response.json()


@pytest.mark.asyncio
async def test_anon_user_can_get_count_queries(client: AsyncClient):
    """Тест для проверки маршрута получения количества запросов."""
    response = await client.get(WEATHER_URL + 'count-queries/')
    assert response.status_code == HTTPStatus.OK, response.json()


def test_model_weather():
    expected_fields = {
        'id', 'city', 'country', 'time', 'temperature', 'windspeed', 'user_id'
    }
    check_db_fields(expected_fields, Weather)

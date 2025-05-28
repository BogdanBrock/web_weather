"""Модуль создания фикстур для пользователей."""

from httpx import AsyncClient, ASGITransport
import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.models import User
from app.core.security import bcrypt_context, get_current_user
from app.main import app
from ..utils import create_db_obj
from ..conftest import BASE_URL

AUTH_URL = f'{BASE_URL}/auth/'
USER_URL = f'{BASE_URL}/users/'
ME_URL = f'{USER_URL}me/'
PASSWORD = 'qwerty12345'


@pytest.fixture
def user_request():
    """Фикстура для запроса."""
    return dict(
        first_name='user',
        last_name='user',
        username='user',
        email='user@yandex.ru',
        password='password12345',
    )


@pytest.fixture
def user_response(user_request):
    """Фикстура для ответа."""
    return dict(
        id=1,
        first_name=user_request['first_name'],
        last_name=user_request['last_name'],
        username=user_request['username'],
        email=user_request['email']
    )


@pytest_asyncio.fixture
async def user(test_db_session):
    """Фикстура для пользователя."""
    data = dict(
        first_name='user',
        last_name='user',
        username='user',
        email='user@yandex.ru',
        password=bcrypt_context.hash(PASSWORD),
    )
    return await create_db_obj(test_db_session, User(**data))


@pytest_asyncio.fixture
async def client():
    """Фикстура для создания анонимного клиента."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url='https://test') as client:
        yield client


@pytest_asyncio.fixture
async def user_client(user):
    """Фикстура создания клиента для пользователя."""
    app.dependency_overrides[get_current_user] = lambda: user
    async with AsyncClient(transport=ASGITransport(app=app), base_url='https://test') as client:
        yield client

"""Модуль создания тестов для продуктов."""

from http import HTTPStatus

import pytest
from httpx import AsyncClient
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import bcrypt_context
from app.models import User
from .fixtures.fixture_users import AUTH_URL, ME_URL, PASSWORD, USER_URL
from .utils import check_db_data, check_db_fields, check_json_data


@pytest.mark.asyncio
async def test_anon_user_can_login(client: AsyncClient, user: User):
    """Тест для проверки авторизации пользователя."""
    url = AUTH_URL + 'login/'
    data = {'username': user.username, 'password': PASSWORD}
    response = await client.post(url, data=data)
    assert response.status_code == HTTPStatus.CREATED, response.json()


@pytest.mark.asyncio
async def test_anon_user_can_registration(
    client: AsyncClient,
    user_request: dict,
    user_response: dict,
    test_db_session: AsyncSession
):
    """Тест для проверки регистрации пользователя."""
    url = USER_URL + 'registration/'
    response = await client.post(url, json=user_request)
    assert response.status_code == HTTPStatus.CREATED, response.json()
    users = (await test_db_session.scalars(select(User))).all()
    assert len(users) == 1
    check_json_data(response, user_response)
    user = users[0]
    assert bcrypt_context.verify(user_request['password'], user.password)
    check_db_data(response, user_response, user)


async def test_auth_user_can_get_own_profile(user_client: AsyncClient):
    """Тест для проверки получения личного профиля."""
    response = await user_client.get(ME_URL)
    assert response.status_code == HTTPStatus.OK, response.json()


@pytest.mark.asyncio
async def test_auth_user_can_update_own_profile(
    user_client: AsyncClient,
    user_request: dict,
    user_response: dict,
    test_db_session: AsyncSession
):
    """Тест для проверки обновления личного профиля."""
    response = await user_client.patch(ME_URL, json=user_request)
    assert response.status_code == HTTPStatus.OK, response.json()
    users = (await test_db_session.scalars(select(User))).all()
    assert len(users) == 1
    check_json_data(response, user_response)
    user = users[0]
    assert bcrypt_context.verify(user_request['password'], user.password)
    check_db_data(response, user_response, user)


@pytest.mark.asyncio
async def test_auth_user_can_delete_own_profile(
    user_client: AsyncClient,
    test_db_session: AsyncSession
):
    """Тест для проверки удаления личного профиля."""
    response = await user_client.delete(ME_URL)
    assert response.status_code == HTTPStatus.NO_CONTENT, response.json()
    count = await test_db_session.scalar(
        select(func.count()).select_from(User)
    )
    assert count == 0


def test_model_user():
    expected_fields = {
        'id', 'first_name', 'last_name', 'username', 'email', 'password'
    }
    check_db_fields(expected_fields, User)

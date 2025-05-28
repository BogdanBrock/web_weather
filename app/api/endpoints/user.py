"""Модуль для создания endpoints для пользователей."""

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import user_service
from app.core.database import db_session
from app.core.security import get_current_user
from app.models import User
from app.schemas import UserCreateSchema, UserUpdateSchema, UserReadSchema

auth_router = APIRouter()
user_router = APIRouter()


@auth_router.post('/login/', status_code=status.HTTP_201_CREATED)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для авторизации пользователя."""
    return await user_service.login(form_data, session)


@user_router.post(
    '/registration/',
    response_model=UserReadSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    schema: UserCreateSchema,
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для регистрации пользователя."""
    return await user_service.create_user(schema, session)


@user_router.get('/me/', response_model=UserReadSchema)
async def get_me(user: User = Depends(get_current_user)):
    """Маршрут для получения личной страницы пользователя."""
    return user


@user_router.patch('/me/', response_model=UserReadSchema)
async def update_me(
    schema: UserUpdateSchema,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_session),
):
    """Маршрут для обновления личной страницы пользователя."""
    return await user_service.update_me(user, schema, session)


@user_router.delete(
    '/me/',
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_me(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_session)
):
    """Маршрут для удаления личной страницы пользователя."""
    return await user_service.delete_me(user, session)

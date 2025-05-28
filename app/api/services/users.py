"""Модуль для создания сервиса для пользователей."""

from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.security import (
    authenticate_user,
    bcrypt_context,
    create_access_token
)
from app.crud import crud_user
from app.models import User
from app.schemas import UserCreateSchema, UserUpdateSchema


class UserService:
    """Класс UserService для создания сервиса."""

    async def create_user(
        self,
        schema: UserCreateSchema,
        session: AsyncSession
    ) -> User:
        """Метод для создания пользователя."""
        hashed_password = bcrypt_context.hash(schema.password)
        schema.password = hashed_password
        return await crud_user.create(schema, session)

    async def login(
        self,
        form_data: OAuth2PasswordRequestForm,
        session: AsyncSession
    ):
        """Метод для авторизации пользователя."""
        user = await authenticate_user(
            form_data.username,
            form_data.password,
            session
        )
        token = await create_access_token(
            user.id,
            settings.TOKEN_EXPIRATION
        )
        return {
            'access_token': token,
            'token_type': 'bearer'
        }

    async def update_me(
        self,
        user: User,
        schema: UserUpdateSchema,
        session: AsyncSession,
    ):
        """Метод для обновления личной страницы пользователя."""
        if schema.password:
            schema.password = bcrypt_context.hash(schema.password)
        return await crud_user.update(user, schema, session)

    async def delete_me(self, user: User, session: AsyncSession):
        """Метод для удаления личной страницы пользователя."""
        return await crud_user.delete(user, session)


user_service = UserService()

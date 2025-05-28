"""Модуль для реализации авторизации пользователей."""

from datetime import datetime, timezone, timedelta

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import db_session
from app.core.exceptions import UnauthorizedError, ValidationError
from app.crud import crud_user
from app.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/auth/login/')
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def authenticate_user(
    username: str,
    password: str,
    session: AsyncSession = Depends(db_session)
) -> User:
    """Функция для аутентификации пользователя."""
    user = await crud_user.get_user_by_username(username, session)
    is_password_hashed = bcrypt_context.verify(password, user.password)
    if not (user and is_password_hashed):
        raise ValidationError('Проверьте введенные вами данные.')
    return user


async def create_access_token(user_id: int, expiration_time: str) -> str:
    """Функция для создания токена."""
    time = datetime.now(timezone.utc) + timedelta(minutes=expiration_time)
    payload = {
        'sub': user_id,
        'exp': int(time.timestamp())
    }
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGHORITM
    )


async def decode_token(token):
    """Функция для декодирования токена."""
    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=(settings.ALGHORITM,)
        )
    except jwt.ExpiredSignatureError:
        raise UnauthorizedError('Проверьте введенные вами данные.')
    except jwt.PyJWTError:
        raise UnauthorizedError('Недействительный токен.')


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(db_session)
) -> User | None:
    """Функция для получения текущего пользователя."""
    payload = await decode_token(token)
    user = await crud_user.get(payload.get('sub'), session)
    if not user:
        raise UnauthorizedError('Проверьте, что вы авторизованы.')
    return user

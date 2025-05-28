"""Файл для инициализации пакета."""

from .users import auth_router, user_router
from .weathers import router as weather_router

__all__ = ('auth_router', 'user_router', 'weather_router')

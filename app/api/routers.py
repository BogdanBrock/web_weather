"""Модуль для создания маршрутов."""

from fastapi import APIRouter

from app.api.endpoints import auth_router, user_router, weather_router


main_router = APIRouter(prefix='/api/v1')

main_router.include_router(auth_router, prefix='/auth', tags=['Auth'])
main_router.include_router(user_router, prefix='/users', tags=['Users'])
main_router.include_router(
    weather_router,
    prefix='/weathers',
    tags=['Weathers']
)
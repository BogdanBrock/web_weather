"""Модуль для создания CRUD операций для погоды."""

from .base import CRUDBase

from app.models import Weather


class CRUDWeather(CRUDBase):
    """Класс для создания CRUD-операций для погоды."""


crud_weather = CRUDWeather(Weather)

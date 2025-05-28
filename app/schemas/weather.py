"""Модуль для создания схем для погоды."""

from pydantic import BaseModel


class WeatherReadSchema(BaseModel):
    """Схема WeatherReadSchema для чтения данных."""

    id: int
    city: str
    country: str
    time: str
    temperature: str
    windspeed: str

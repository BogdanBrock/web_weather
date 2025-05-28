"""Модуль для создания схем для погоды."""

from pydantic import BaseModel, PositiveInt


class WeatherCreateSchema(BaseModel):
    """Схема WeatherReadSchema для чтения данных."""

    city: str
    country: str
    time: str
    temperature: str
    windspeed: str
    user_id: PositiveInt


class WeatherReadSchema(BaseModel):
    """Схема WeatherReadSchema для чтения данных."""

    id: int
    city: str
    country: str
    time: str
    temperature: str
    windspeed: str


class WeatherQueryCountReadSchema(BaseModel):
    city: str
    count: int

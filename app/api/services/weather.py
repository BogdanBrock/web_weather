"""Модуль для создания сервиса для погоды."""

from datetime import datetime
from zoneinfo import ZoneInfo

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.crud import crud_weather
from app.schemas import WeatherCreateSchema
from app.models import User, Weather


class WeatherService:
    """Класс WeatherService для создания сервиса."""

    GEO_URL = 'https://geocoding-api.open-meteo.com/v1/search'
    WEATHER_URL = 'https://api.open-meteo.com/v1/forecast'

    async def get_home(
        self,
        user: User,
        session: AsyncSession
    ) -> str:
        """Метод для получения главной страницы."""
        city = await crud_weather.get_last_name_city_for_user(user, session)
        message = (
            'Добро пожаловать, вы можете посмотреть '
            'прогноз погоды для любого города.'
        )
        if not city:
            return message
        return message + (
            ' Так же можно посмотреть прогноз погоды для города, '
            f'который вы смотрели раннее: `{city}`.'
        )

    async def get_time(self, geo_data: dict, weather_data: dict) -> str:
        """Метод для получения времени."""
        utc_time_now = datetime.now(ZoneInfo(geo_data['timezone']))
        utc_offset = utc_time_now.utcoffset()
        utc_offset_str = utc_time_now.strftime('%z')
        formatted_utc_str = f'{utc_offset_str[:3]}:{utc_offset_str[3:]}'
        time = datetime.fromisoformat(weather_data['time']) + utc_offset
        return time.strftime('%d-%m-%Y %H:%M') + f' UTC{formatted_utc_str}'

    async def get_geo_data(self, client: AsyncClient, city: str) -> dict:
        """Метод для получения гео-данных."""
        response = await client.get(
            self.GEO_URL,
            params={'language': 'ru', 'name': city}
        )
        try:
            return response.json()['results'][0]
        except KeyError:
            raise HTTPException(
                detail='Такого города не существует',
                status_code=status.HTTP_404_NOT_FOUND
            )

    async def get_weather_data(
        self,
        client: AsyncClient,
        latitude: str,
        longitude: str
    ) -> dict:
        """Метод для получения данных о погоде."""
        response = await client.get(
            self.WEATHER_URL,
            params={'latitude': latitude,
                    'longitude': longitude,
                    'current_weather': True}
        )
        return response.json()['current_weather']

    async def get_weather(
        self,
        city: str,
        user: User,
        session: AsyncSession
    ) -> Weather:
        """Метод для получения результата о погоде."""
        async with AsyncClient() as client:
            geo_data = await self.get_geo_data(client, city)
            weather_data = await self.get_weather_data(
                client,
                geo_data['latitude'],
                geo_data['longitude']
            )
            time = await self.get_time(geo_data, weather_data)
            temperature = round(weather_data["temperature"])
            schema_weather = WeatherCreateSchema(
                city=geo_data['name'],
                country=geo_data['country'],
                time=time,
                temperature=f'{temperature} °C',
                windspeed=f'{weather_data["windspeed"]} км/ч',
                user_id=user.id
            )
            return await crud_weather.create(schema_weather, session)


weather_service = WeatherService()

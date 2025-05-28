"""Модуль для создания модели для погоды."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Weather(Base):
    """Класс для создания модели Weather."""

    __tablename__ = 'weathers'

    city: Mapped[str]
    country: Mapped[str]
    time: Mapped[str]
    temperature: Mapped[str]
    windspeed: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped['User'] = relationship('User', back_populates='weathers')

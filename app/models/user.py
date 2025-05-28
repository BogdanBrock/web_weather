"""Модуль для создания модели для пользователя."""

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class User(Base):
    """Класс для создания модели User."""

    __tablename__ = 'users'

    first_name: Mapped[str]
    last_name: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]

    weathers: Mapped[list['Weather']] = relationship(
        'Weather',
        back_populates='user',
        cascade='all, delete-orphan'
    )

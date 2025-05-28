"""Модуль для создания схем для пользователя."""

from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    """Схема UserCreateSchema для создания данных."""

    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str


class UserUpdateSchema(BaseModel):
    """Схема UserUpdateSchema для обновления данных."""

    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    username: str = Field(default=None)
    email: str = Field(default=None)
    password: str = Field(default=None)


class UserReadSchema(BaseModel):
    """Схема для UserReadSchema для чтения данных."""

    id: int
    first_name: str
    last_name: str
    username: str
    email: str

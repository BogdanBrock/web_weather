"""Модуль для создания исключений."""

from fastapi import HTTPException, status


class AlreadyExistsError(HTTPException):
    """Класс для ошибки с уже существующим объектом."""

    def __init__(self, detail: str | None = None):
        """Метод для инициализации исключения ValidationError."""
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )


class ValidationError(HTTPException):
    """Класс для ошибки с неправильными введеными данными."""

    def __init__(self, detail: str | None = None):
        """Метод для инициализации исключения ValidationError."""
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )


class UnauthorizedError(HTTPException):
    """Класс для ошибки с неавторизированным пользователем."""

    def __init__(self, detail: str | None = None):
        """Метод для инициализации исключения UnauthorizedError."""
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail
        )


class NotFoundError(HTTPException):
    """Класс для ошибки с несуществующим объектом."""

    def __init__(self, detail: str | None = None):
        """Метод для инициализации исключения ValidationError."""
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )

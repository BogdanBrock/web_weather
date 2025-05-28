"""Модуль для создания CRUD-операций."""

from typing import TypeVar, Generic

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import Base

ModelType = TypeVar('ModelType', bound=Base)
SchemaType = TypeVar('SchemaType', bound=BaseModel)


class CRUDBase(Generic[ModelType, SchemaType]):
    """Класс для создания базовых CRUD-операций."""

    def __init__(self, model: ModelType) -> None:
        """Метод для иницилазации атрибутов объекта класса CRUDBase."""
        self.model = model

    async def get_all(self, session: AsyncSession) -> list[ModelType]:
        """Метод для получения объектов."""
        objs = await session.execute(select(self.model))
        return objs.scalars().all()

    async def get(self, id: int, session: AsyncSession) -> ModelType:
        """Метод для получения объекта."""
        obj = await session.execute(
            select(self.model).where(self.model.id == id)
        )
        return obj.scalar()

    async def create(
        self,
        schema: SchemaType,
        session: AsyncSession
    ) -> ModelType:
        """Метод для создания объекта."""
        model_obj = self.model(**schema.model_dump())
        session.add(model_obj)
        await session.commit()
        await session.refresh(model_obj)
        return model_obj

    async def update(
        self,
        model_obj: ModelType,
        schema: SchemaType,
        session: AsyncSession
    ) -> ModelType:
        """Метод для обновления объекта."""
        data = schema.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(model_obj, key, value)
        await session.commit()
        await session.refresh(model_obj)
        return model_obj

    async def delete(
        self,
        model_obj: ModelType,
        session: AsyncSession
    ) -> None:
        """Метод для удаления объекта."""
        await session.delete(model_obj)
        await session.commit()

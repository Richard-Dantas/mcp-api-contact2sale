from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List
from src.application.usecases.base.ibase_usecase import IBaseUseCase
from src.domain.repositories.base_repository import BaseRepository
from src.domain.entities.base import Base

T = TypeVar('T', bound=Base)

class BaseUseCase(IBaseUseCase[T],Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    def get(self, id: int) -> T:
        return self.repository.get(id)

    def get_all(self) -> List[T]:
        return self.repository.get_all()

    def create(self, obj_in: T) -> T:
        return self.repository.create(obj_in)

    def update(self, obj_in: T) -> T:
        return self.repository.update(obj_in)

    def delete(self, id: int) -> None:
        self.repository.delete(id)
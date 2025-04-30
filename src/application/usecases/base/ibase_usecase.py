from typing import Generic, List, TypeVar

from src.domain.entities.base import Base

T = TypeVar('T', bound=Base)

class IBaseUseCase(Generic[T]):
    def get(self, id: int) -> T:
        raise NotImplementedError

    def get_all(self) -> List[T]:
        raise NotImplementedError

    def create(self, obj_in: T) -> T:
        raise NotImplementedError

    def update(self, obj_in: T) -> T:
        raise NotImplementedError

    def delete(self, id: int) -> None:
        raise NotImplementedError
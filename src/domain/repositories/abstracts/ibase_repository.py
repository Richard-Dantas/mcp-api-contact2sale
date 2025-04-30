from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')

class IBaseRepository(Generic[T], ABC):
    @abstractmethod
    async def get(self, id: int) -> T:
        """
        Obtém um objeto do tipo T pelo seu ID.

        :param id: O ID do objeto.
        :return: O objeto do tipo T.
        :raises NotImplementedError: Se o método não estiver implementado.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[T]:
        """
        Obtém todos os objetos do tipo T.

        :return: Uma lista de objetos do tipo T.
        :raises NotImplementedError: Se o método não estiver implementado.
        """
        raise NotImplementedError

    @abstractmethod
    async def create(self, obj_in: T) -> T:
        """
        Cria um novo objeto do tipo T.

        :param obj_in: O objeto a ser criado.
        :return: O objeto criado.
        :raises NotImplementedError: Se o método não estiver implementado.
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, obj_in: T) -> T:
        """
        Atualiza um objeto do tipo T existente.

        :param obj_in: O objeto a ser atualizado.
        :return: O objeto atualizado.
        :raises NotImplementedError: Se o método não estiver implementado.
        """
        raise NotImplementedError

    @abstractmethod
    async def delete(self, id: int) -> None:
        """
        Deleta um objeto do tipo T pelo seu ID.

        :param id: O ID do objeto a ser deletado.
        :raises NotImplementedError: Se o método não estiver implementado.
        """
        raise NotImplementedError

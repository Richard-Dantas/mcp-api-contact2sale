from abc import ABC, abstractmethod
from typing import List, Optional, Union
from src.domain.entities.vehicle import Vehicle

class IVehicleRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[Vehicle]:
        pass

    @abstractmethod
    async def get_by_filters(
        self,
        brand: Optional[str] = None,
        model: Optional[str] = None,
        year: Optional[int] = None,
        engine: Optional[str] = None,
        fuel_type: Optional[str] = None,
        color: Optional[str] = None,
        mileage: Optional[Union[int, dict]] = None,
        doors: Optional[int] = None,
        transmission: Optional[str] = None,
        price: Optional[Union[int, dict]] = None,
        limit: Optional[int] = None,
    ) -> List[Vehicle]:
        pass

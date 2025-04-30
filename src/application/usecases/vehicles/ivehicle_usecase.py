from typing import List, Optional, Union
from src.application.usecases.base.ibase_usecase import IBaseUseCase
from src.domain.entities.vehicle import Vehicle

class IVehicleUseCase(IBaseUseCase[Vehicle]):
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
        raise NotImplementedError

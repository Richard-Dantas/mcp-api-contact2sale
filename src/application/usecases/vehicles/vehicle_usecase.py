from typing import List, Optional, Union
from src.application.usecases.base.base_usecase import BaseUseCase
from src.application.usecases.vehicles.ivehicle_usecase import IVehicleUseCase
from src.domain.entities.vehicle import Vehicle
from src.domain.repositories.abstracts.ivehicle_repository import IVehicleRepository

class VehicleUseCase(BaseUseCase[Vehicle], IVehicleUseCase):
    def __init__(self, repository: IVehicleRepository):
        super().__init__(repository)
        self.repository = repository  

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
        return await self.repository.get_by_filters(
            brand=brand,
            model=model,
            year=year,
            engine=engine,
            fuel_type=fuel_type,
            color=color,
            mileage=mileage,
            doors=doors,
            transmission=transmission,
            price=price,
            limit=limit
        )

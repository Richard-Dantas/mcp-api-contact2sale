from typing import List, Optional, Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.vehicle import Vehicle
from src.domain.repositories.base_repository import BaseRepository
from src.domain.repositories.abstracts.ivehicle_repository import IVehicleRepository

class VehicleRepository(BaseRepository[Vehicle], IVehicleRepository):
    def __init__(self, db: AsyncSession):
        super().__init__(Vehicle, db)

    async def get_all(self) -> List[Vehicle]:
        query = select(Vehicle)
        async with self.db.begin():
            result = await self.db.execute(query)
            return result.scalars().all()

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
        query = select(Vehicle)

        if brand:
            query = query.filter(Vehicle.brand.ilike(f"%{brand}%"))
        if model:
            query = query.filter(Vehicle.model.ilike(f"%{model}%"))
        if year:
            query = query.filter(Vehicle.year == year)
        if engine:
            query = query.filter(Vehicle.engine == engine)
        if fuel_type:
            query = query.filter(Vehicle.fuel_type.ilike(f"%{fuel_type}%"))
        if color:
            query = query.filter(Vehicle.color.ilike(f"%{color}%"))
        if doors:
            query = query.filter(Vehicle.doors == doors)
        if transmission:
            query = query.filter(Vehicle.transmission.ilike(f"%{transmission}%"))

        if isinstance(price, dict):
            if "$lt" in price:
                query = query.filter(Vehicle.price < price["$lt"])
            if "$lte" in price:
                query = query.filter(Vehicle.price <= price["$lte"])
            if "$gt" in price:
                query = query.filter(Vehicle.price > price["$gt"])
            if "$gte" in price:
                query = query.filter(Vehicle.price >= price["$gte"])
            if "$eq" in price:
                query = query.filter(Vehicle.price == price["$eq"])
        elif price is not None:
            query = query.filter(Vehicle.price == price)

        if isinstance(mileage, dict):
            if "$lt" in mileage:
                query = query.filter(Vehicle.mileage < mileage["$lt"])
            if "$lte" in mileage:
                query = query.filter(Vehicle.mileage <= mileage["$lte"])
            if "$gt" in mileage:
                query = query.filter(Vehicle.mileage > mileage["$gt"])
            if "$gte" in mileage:
                query = query.filter(Vehicle.mileage >= mileage["$gte"])
            if "$eq" in mileage:
                query = query.filter(Vehicle.mileage == mileage["$eq"])
        elif mileage is not None:
            query = query.filter(Vehicle.mileage == mileage)

        if limit:
            query = query.limit(limit)

        result = await self.db.execute(query)
        return result.scalars().all()

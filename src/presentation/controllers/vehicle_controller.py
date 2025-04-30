from typing import List, Optional, Union
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.database.database import get_db
from src.domain.repositories.vehicle_repository import VehicleRepository
from src.application.usecases.vehicles.vehicle_usecase import VehicleUseCase
import traceback

router = APIRouter()

def get_vehicle_usecase(db: AsyncSession = Depends(get_db)) -> VehicleUseCase:
    repository = VehicleRepository(db)
    return VehicleUseCase(repository)

@router.get("/api/v1/vehicles", response_model=List[str])
async def list_vehicles(
    brand: Optional[str] = Query(None),
    model: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    engine: Optional[str] = Query(None),
    fuel_type: Optional[str] = Query(None),
    color: Optional[str] = Query(None),
    mileage: Optional[str] = Query(None),
    doors: Optional[int] = Query(None),
    transmission: Optional[str] = Query(None),
    price: Optional[str] = Query(None),
    limit: Optional[int] = Query(None),
    usecase: VehicleUseCase = Depends(get_vehicle_usecase),
) -> List[str]:
    try:
        vehicles = await usecase.get_by_filters(
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

        return [
            f"marca:{v.brand} modelo:{v.model} ano:{v.year} - motor:{v.engine} - preço:{v.price}"
            for v in vehicles
        ]
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Erro interno ao buscar veículos.")

@router.get("/health")
async def health():
    return {"status": "ok"}
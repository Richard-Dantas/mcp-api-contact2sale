from fastmcp import FastMCP
import sys

sys.path.append('/app')

from src.infrastructure.database.database import SessionLocal
from src.domain.entities.vehicle import Vehicle

mcp = FastMCP("vehicles")

@mcp.tool()
def get_vehicle_by_attributes(
    brand: str = None,
    model: str = None,
    year: int = None,
    engine: str = None,
    fuel_type: str = None,
    color: str = None,
    mileage: dict = None,
    doors: int = None,
    transmission: str = None,
    price: dict = None,
    limit: int = None 
) -> str:
    """Filtra veículos usando múltiplos atributos, com suporte a limite."""
    session = SessionLocal()
    query = session.query(Vehicle)

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

    if limit is not None:
        query = query.limit(limit)

    vehicles = query.all()
    session.close()

    if not vehicles:
        return "Nenhum veículo encontrado com os filtros especificados."

    results = [
        f"marca:{v.brand} modelo:{v.model} ano:{v.year} - motor:{v.engine} - preço:{v.price}"
        for v in vehicles
    ]
    return "\n".join(results)



if __name__ == "__main__":
    mcp.run()

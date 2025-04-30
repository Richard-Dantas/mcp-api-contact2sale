import httpx
import os
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://mcp-api-app:8000/api/v1/vehicles")

if not API_URL:
    raise RuntimeError("❌ API_URL não configurada e nenhum valor padrão foi definido.")

mcp = FastMCP("vehicles")

@mcp.tool()
async def get_vehicle_by_attributes(
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
    """Filtra veículos usando múltiplos atributos via chamada HTTP para o serviço FastAPI."""
    params = {
        "brand": brand,
        "model": model,
        "year": year,
        "engine": engine,
        "fuel_type": fuel_type,
        "color": color,
        "doors": doors,
        "transmission": transmission,
        "limit": limit,
    }

    if mileage is not None:
        params["mileage"] = str(mileage)
    if price is not None:
        params["price"] = str(price)

    params = {k: v for k, v in params.items() if v is not None}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URL, params=params, timeout=20)
            response.raise_for_status()
            return response.text
    except Exception as e:
        return f"Erro ao buscar veículos pela API: {str(e)}"

if __name__ == "__main__":
    mcp.run()

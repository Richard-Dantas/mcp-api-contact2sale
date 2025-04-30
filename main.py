from fastapi import FastAPI
from src.presentation.controllers.vehicle_controller import router
from src.infrastructure.database.database import async_engine, Base

async def lifespan(app: FastAPI):
    print("🚀 Lifespan started")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("📦 Tabelas verificadas")
    yield
    print("🧹 Lifespan encerrado")

app = FastAPI(lifespan=lifespan)
app.include_router(router)

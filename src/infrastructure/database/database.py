import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from src.domain.entities.base import Base

POSTGRES_USER = os.getenv('DB_USER', 'user')
POSTGRES_PASSWORD = os.getenv('DB_PASSWORD', 'password')
POSTGRES_DB = os.getenv('DB_NAME', 'cars_db')
POSTGRES_HOST = os.getenv('DB_HOST', 'db')
POSTGRES_PORT = os.getenv('DB_PORT', '5432')

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = async_sessionmaker(bind=async_engine , expire_on_commit=False, class_=AsyncSession)

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

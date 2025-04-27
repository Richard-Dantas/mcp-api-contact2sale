import os
from src.domain.entities.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


POSTGRES_USER = os.getenv('DB_USER', 'user')
POSTGRES_PASSWORD = os.getenv('DB_PASSWORD', 'password')
POSTGRES_DB = os.getenv('DB_NAME', 'cars_db')
POSTGRES_HOST = os.getenv('DB_HOST', 'db')
POSTGRES_PORT = os.getenv('DB_PORT', '5432')

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

print(f"Conectando no banco: {DATABASE_URL}")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

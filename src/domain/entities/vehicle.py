from sqlalchemy import Column, Integer, String
from .base import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    engine = Column(String, nullable=False)
    fuel_type = Column(String, nullable=False)
    color = Column(String, nullable=False)
    mileage = Column(Integer, nullable=False)
    doors = Column(Integer, nullable=False)
    transmission = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Vehicle(brand={self.brand}, model={self.model}, year={self.year})>"

    def full_description(self):
        return f"{self.brand} {self.model} {self.year} ({self.color}) - {self.mileage}km - R${self.price}"
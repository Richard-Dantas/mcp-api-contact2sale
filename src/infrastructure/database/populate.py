from faker import Faker
from src.domain.entities.vehicle import Vehicle
from src.infrastructure.database.database import SessionLocal

fake = Faker()

def populate_vehicles(count=100):
    session = SessionLocal()

    for _ in range(count):
        vehicle = Vehicle(
            brand=fake.company(),
            model=fake.word(),
            year=int(fake.year()),
            engine=fake.random_element(elements=["1.0", "1.4", "2.0", "3.0"]),
            fuel_type=fake.random_element(elements=["Gasolina", "Diesel", "Elétrico", "Flex"]),
            color=fake.color_name(),
            mileage=fake.random_int(min=0, max=200000),
            doors=fake.random_element(elements=[2, 4]),
            transmission=fake.random_element(elements=["Manual", "Automático"]),
            price=fake.random_int(min=30000, max=250000)
        )
        session.add(vehicle)

    session.commit()
    session.close()

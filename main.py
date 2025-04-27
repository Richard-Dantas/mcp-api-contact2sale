from src.infrastructure.database.database import Base, engine
from src.infrastructure.database.populate import populate_vehicles
from src.domain.entities.vehicle import Vehicle  # <<<<<< IMPORTANTE

def setup_database():
    print(f"Conectando no banco: {engine.url}")
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

def seed_data():
    print("Populando banco de dados com veículos fictícios...")
    populate_vehicles(count=100)
    print("Banco populado com sucesso!")

if __name__ == "__main__":
    setup_database()
    seed_data()

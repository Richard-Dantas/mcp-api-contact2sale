import asyncio
from src.infrastructure.database.database import Base, engine
from src.infrastructure.database.populate import populate_vehicles
from src.application.usecases.mcp.mcp_service import MCPService

def setup_database():
    print(f"Conectando no banco: {engine.url}")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

def seed_data():
    print("Populando banco de dados com veículos fictícios...")
    populate_vehicles(count=100)
    print("Banco populado com sucesso!")

async def start_terminal_agent():
    print("\nIniciando agente virtual via MCP + HuggingFace...")

    service = MCPService()

    print("\nPergunte algo ao seu agente! (digite 'sair' para encerrar)\n")

    while True:
        user_input = input("Você: ")
        if user_input.lower() in ("sair", "exit", "quit"):
            print("Encerrando agente virtual. Até mais!")
            break

        try:
            resposta = await service.call_agent(user_input)
            print(f"Agente: {resposta}\n")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}")

if __name__ == "__main__":
    setup_database()
    seed_data()
    asyncio.run(start_terminal_agent())

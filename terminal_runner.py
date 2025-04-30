import asyncio
from src.infrastructure.database.database import Base, async_engine
from src.infrastructure.database.populate import populate_vehicles
from src.application.usecases.mcp.mcp_service import MCPService

async def setup_database():
    print(f"Conectando no banco: {async_engine.url}")
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tabelas criadas com sucesso!")

async def seed_data():
    print("Populando banco de dados com veículos fictícios...")
    await populate_vehicles(count=100)
    print("Banco populado com sucesso!")

async def start_terminal_agent():
    print("\nIniciando agente virtual via MCP")

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

async def main():
    await setup_database()
    await seed_data()

    await start_terminal_agent()

if __name__ == "__main__":
    asyncio.run(main())

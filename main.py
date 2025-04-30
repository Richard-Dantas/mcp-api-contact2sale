# import asyncio
# from fastapi import FastAPI
# import uvicorn
# from src.infrastructure.database.database import Base, async_engine
# from src.infrastructure.database.populate import populate_vehicles
# from src.application.usecases.mcp.mcp_service import MCPService
# from src.presentation.controllers.vehicle_controller import router

# async def setup_database():
#     print(f"Conectando no banco: {async_engine.url}")
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     print("Tabelas criadas com sucesso!")

# async def seed_data():
#     print("Populando banco de dados com veículos fictícios...")
#     await populate_vehicles(count=100)
#     print("Banco populado com sucesso!")

# async def start_terminal_agent():
#     print("\nIniciando agente virtual via MCP + HuggingFace...")

#     service = MCPService()

#     print("\nPergunte algo ao seu agente! (digite 'sair' para encerrar)\n")

#     while True:
#         user_input = input("Você: ")
#         if user_input.lower() in ("sair", "exit", "quit"):
#             print("Encerrando agente virtual. Até mais!")
#             break

#         try:
#             resposta = await service.call_agent(user_input)
#             print(f"Agente: {resposta}\n")
#         except Exception as e:
#             print(f"Erro ao processar a pergunta: {e}")

# async def lifespan(app: FastAPI):
#     print("🚀 Lifespan started")
#     # Aqui você pode configurar banco, logger, caches, etc.
#     # Por exemplo: db = setup_database(); app.state.db = db
#     yield
#     print("🧹 Lifespan shutdown")

# app = FastAPI(lifespan=lifespan)
# app.include_router(router)

# async def main():
#     await setup_database()
#     await seed_data()

#     # Cria tarefa do agente terminal
#     terminal_task = asyncio.create_task(start_terminal_agent())

#     # Roda o servidor FastAPI (uvicorn) como tarefa asyncio também
#     config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, reload=False, loop="asyncio", log_level="debug")
#     server = uvicorn.Server(config)

#     server_task = asyncio.create_task(server.serve())

#     await asyncio.gather(terminal_task, server_task)

# if __name__ == "__main__":
#     asyncio.run(main())


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

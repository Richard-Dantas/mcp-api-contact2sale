# Desafio Técnico - Desenvolvedor Python | C2S

Este projeto é uma aplicação de demonstração para um sistema de assistente virtual de veículos utilizando FastAPI, SQLAlchemy assíncrono, PostgreSQL, e integração com o modelo LLM via Ollama e FastMCP.

## Tecnologias Utilizadas
- Python 3.12
- FastAPI
- SQLAlchemy 2.0 (assíncrono)
- PostgreSQL 15
- Docker & Docker Compose
- Ollama (modelo LLM local)
- FastMCP (Model Context Protocol)

## Como Rodar o Projeto

### 1. Clone o Repositório
```bash
git clone <repo_url>
cd <repo>
```

### 2. Execute com Docker Compose
```bash
docker compose up --build
```
Esse comando sobe os seguintes containers:
- `db`: banco de dados PostgreSQL
- `ollama`: servidor LLM local
- `api`: serviço FastAPI na porta 8000
- `terminal`: interface de terminal para interação com o agente virtual

> ✅ Aguarde a saída "Banco populado com sucesso!" no terminal para garantir que a aplicação está pronta para uso.

### 3. Acesse um terminal
```bash
docker attach mcp-terminal
```

## Acessando a API
A API FastAPI estará disponível em:
```
http://localhost:8000/api/v1/vehicles
```

### Exemplo de requisição via Postman:
```
GET http://localhost:8000/api/v1/vehicles?engine=2.0&limit=2
```

### Endpoint de Health Check:
```
GET http://localhost:8000/health
```

## Usando o Agente Virtual via Terminal
Você pode conversar com o agente. Exemplo:
```
Você: quero um carro com motor 2.0 e preço acima de 200 mil
```

O agente utilizará o modelo LLM para interpretar sua pergunta e consultar a API internamente.

## Estrutura do Projeto
```
/app
|-- main.py                # Servidor FastAPI (API)
|-- terminal_runner.py     # Interface de terminal (Agente)
|-- Dockerfile             # Docker para API e Terminal
|-- docker-compose.yml
|-- src/
    |-- application/
    |-- domain/
    |-- infrastructure/
    |-- presentation/
```

## Variáveis de Ambiente
Configure no `.env` na raiz do projeto (veja .env.example):
```env
DB_USER=user
DB_PASSWORD=password
DB_NAME=cars_db
DB_HOST=db
DB_PORT=5432

OLLAMA_API_URL=http://ollama:11434/api/generate
OLLAMA_MODEL_NAME=llama3
API_URL=http://mcp-api-app:8000/api/v1/vehicles
```

## Considerações Finais
- O banco é populado automaticamente com 100 veículos fictícios na primeira execução.
- As requisições do agente são feitas via HTTP para a API, e não diretamente ao banco.

---


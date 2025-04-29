# Dockerfile (na raiz do app)
FROM python:3.12-slim

# Instala dependências básicas
RUN apt-get update && apt-get install -y gcc

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

# Comando para rodar
CMD ["python", "main.py"]

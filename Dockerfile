FROM python:3.12-slim

# Cria diretório de trabalho
WORKDIR /app

# Copia requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Comando padrão ao iniciar o container
CMD ["python", "main.py"]

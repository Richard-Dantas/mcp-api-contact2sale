FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

CMD ["python", "main.py"]

# Используем официальный образ Python
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
from contextlib import asynccontextmanager

from fastapi import FastAPI
from backend.api.handler import router
import uvicorn
from backend.logger import status_logger

from fastapi.middleware.cors import CORSMiddleware

import os

# Контекстный менеджер для логирования старта и остановки приложения
@asynccontextmanager
async def app_logger(application):
    # Логируем запуск приложения
    status_logger.info("Starting my new application")
    yield  # Здесь FastAPI выполняет всю работу приложения
    # Логируем завершение работы приложения
    status_logger.info("Shutting down application")


# Создаем объект FastAPI, передаем lifespan для логирования старта и завершения
app = FastAPI(lifespan=app_logger)  # можно отключить документацию через docs_url=None, redoc_url=None

# Настройка CORS (разрешение кросс-доменных запросов)
app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=["*"],             # Разрешаем запросы с любых доменов
    allow_credentials=True,          # Разрешаем использование cookies и авторизации
    allow_methods=["GET", "POST"],   # Разрешаем указанные HTTP-методы
    allow_headers=["Content-Type"],  # Разрешаем указанные заголовки
)

# Подключение роутера с префиксом "/api"
app.include_router(router, prefix="/api")


# Точка входа для запуска приложения через uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

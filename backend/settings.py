import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Конфигурация подключения к базе данных Postgres
DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB"),        # Имя базы данных
    "user": os.getenv("POSTGRES_USER"),        # Имя пользователя
    "password": os.getenv("POSTGRES_PASSWORD"),# Пароль
    "host": os.getenv("POSTGRES_HOST"),        # Хост/сервер базы данных
    "port": os.getenv("POSTGRES_PORT"),        # Порт
}

# Размеры пула соединений с базой данных
# Если в .env не указаны, используются значения по умолчанию
POOL_SIZE = int(os.getenv("POOL_SIZE", 10))       # Минимальное число соединений
POOL_MAX_SIZE = int(os.getenv("POOL_MAX_SIZE", 20)) # Максимальное число соединений

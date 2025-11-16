import logging
import sys
from logging import Formatter
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Формат логов: время, имя логгера, уровень, сообщение
LOG_FORMAT_APP = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# Папка для хранения файлов логов
LOG_DIR = Path("./logs")


class Configs:
	@staticmethod
	def _create_logger(name: str, file_name: str, level: int):
		# Создаем директорию для логов, если ее нет
		LOG_DIR.mkdir(parents=True, exist_ok=True)
		
		# Получаем логгер по имени
		log = logging.getLogger(name)
		log.setLevel(logging.DEBUG)  # Логгер принимает все уровни, фильтр будет на хендлерах
		
		# Проверяем, есть ли уже хендлеры, чтобы не добавлять их повторно
		if not log.handlers:
			log_file = LOG_DIR / file_name  # Полный путь к файлу лога
			# Ротация логов: максимум 1 MB, сохраняется 1 резервная копия
			handler = RotatingFileHandler(
				filename=log_file,
				maxBytes=2 ** 20,  # 1 MB
				backupCount=1,
				encoding="utf-8"
			)
			# Форматируем сообщения в логе
			handler.setFormatter(Formatter(LOG_FORMAT_APP))
			handler.setLevel(level)  # Уровень логирования для файла
			log.addHandler(handler)
		
		return log
	
	@staticmethod
	def config_status_logger(name: str = "src"):
		# Создаем логгер для статусных сообщений (INFO)
		log = Configs._create_logger(f"{name}_status", f"{name}.log", logging.INFO)
		
		# Добавляем вывод в консоль
		console_handler = logging.StreamHandler(sys.stdout)
		console_handler.setFormatter(Formatter(LOG_FORMAT_APP))
		console_handler.setLevel(logging.INFO)  # Можно поставить DEBUG для более подробного вывода
		log.addHandler(console_handler)
		
		return log
	
	@staticmethod
	def config_error_logger(name: str = 'src'):
		# Создаем логгер для ошибок (ERROR)
		log = Configs._create_logger(f"{name}_error", f"errors_{name}.log", logging.ERROR)
		return log


# Глобальные объекты логгеров для приложения
status_logger = Configs.config_status_logger()  # Для информационных сообщений
error_logger = Configs.config_error_logger()  # Для ошибок

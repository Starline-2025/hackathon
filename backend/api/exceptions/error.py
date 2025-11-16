from fastapi import HTTPException

from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from backend.api.exceptions.error_messages import NotFoundErrorMessage, InternalServerErrorMessage

from backend.domain.errors import CardsNotFoundException

from backend.logger import status_logger


class Error:
	@staticmethod
	def handle(
			exc: Exception,
	) -> HTTPException:
		# Логируем ошибку, чтобы затем можно было посмотреть в логах
		status_logger.info(f"Error occurred: \n{exc}")
		
		# Проверяем, относится ли полученная ошибка к типу CardsNotFoundException
		# isinstance позволяет определить, является ли ошибка экземпляром указанного класса
		if isinstance(exc, (
				CardsNotFoundException,
		)):
			# Если ошибка связана с отсутствием карточек — возвращаем 404
			raise HTTPException(
				status_code=HTTP_404_NOT_FOUND,
				detail=NotFoundErrorMessage  # Сообщение для клиента
			)
		
		# Если ошибка не является известной — возвращаем 500
		# Это общий обработчик для всех непредвиденных исключений
		raise HTTPException(
			status_code=HTTP_500_INTERNAL_SERVER_ERROR,
			detail=InternalServerErrorMessage  # Сообщение для клиента
		)

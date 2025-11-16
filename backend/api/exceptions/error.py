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
		status_logger.info(f"Error occurred: \n{exc}")
		
		if isinstance(exc, (
			CardsNotFoundException,
		)):
			raise HTTPException(
				status_code=HTTP_404_NOT_FOUND,
				detail=NotFoundErrorMessage
			)
		
		raise HTTPException(
			status_code=HTTP_500_INTERNAL_SERVER_ERROR,
			detail=InternalServerErrorMessage
		)

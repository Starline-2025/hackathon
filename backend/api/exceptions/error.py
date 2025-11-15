from fastapi import HTTPException

from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from error_messages import BadRequestErrorMessage, InternalServerErrorMessage

from ...domain.errors import CardsNotFoundException

from ...logger import status_logger

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
				status_code=HTTP_400_BAD_REQUEST,
				detail=BadRequestErrorMessage
			)
		
		raise HTTPException(
			status_code=HTTP_500_INTERNAL_SERVER_ERROR,
			detail=InternalServerErrorMessage
		)

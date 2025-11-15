from ...infra.repo import CardRepoImpl
from ...app.usecase import CardNKOService
from ...app.service import CardNKOServiceImpl
from ...api.exceptions.error import Error

def get_card_service() -> CardNKOService:
	repo = CardRepoImpl()
	service = CardNKOServiceImpl(repo)
	return service

def get_error() -> Error:
	error = Error()
	return error
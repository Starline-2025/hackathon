from backend.infra.repo import CardRepoImpl
from backend.app.usecase import CardNKOService
from backend.app.service import CardNKOServiceImpl
from backend.api.exceptions.error import Error

def get_card_service() -> CardNKOService:
	repo = CardRepoImpl()
	service = CardNKOServiceImpl(repo)
	return service

def get_error() -> Error:
	error = Error()
	return error
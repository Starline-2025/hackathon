from fastapi import APIRouter, Depends
from typing import List

from backend.api.exceptions.error import Error
from backend.app.usecase import CardNKOService
from backend.infra.di.di import get_card_service, get_error
from backend.api.models.model import Card

router = APIRouter(tags=["cards"])

@router.get("/cards", response_model=List[Card], response_model_exclude_none=True)
def get_cards_by_filter(
	name: str | None = None,
	city: str | None = None,
	category: str | None = None,
	cards_service: CardNKOService = Depends(get_card_service),
	error: Error = Depends(get_error),
):
	try:
		cards = cards_service.get_cards_by_filter(name=name, city=city, category=category)
		return cards
	except Exception as e:
		return error.handle(e)

@router.post("/cards", response_model=Card, response_model_exclude_none=True)
def create_card(
	req: Card,
	cards_service: CardNKOService = Depends(get_card_service),
	error: Error = Depends(get_error),
):
	try:
		created = cards_service.create_card(req)
		return created
	except Exception as e:
		return error.handle(e)

@router.get("/health")
def health():
	return {"status": "ok"}

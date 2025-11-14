from typing import List
from ..app.usecase import CardNKOService
from ..domain.repo import CardRepo
from ..domain.entity import Card

class CardNKOServiceImpl(CardNKOService):
    def __init__(self, repo:CardRepo):
        self._repo = repo

    def get_cards_by_filter(self, name: str | None, category: str | None, city: str | None) -> List[Card]:
        cards = self._repo.get_cards(name, category, city)
        return cards

    def create_card(self, card: Card) -> Card:
        card = self._repo.create_card(card)
        return card
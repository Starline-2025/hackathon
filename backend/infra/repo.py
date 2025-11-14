from backend.domain.entity import Card
from backend.domain.repo import CardRepo


class CardRepoImpl(CardRepo):
	def get_card(self, name : str | None, category: str | None, city: str | None) -> Card:
		...
	def create_card(self, card: Card) -> Card:
		...
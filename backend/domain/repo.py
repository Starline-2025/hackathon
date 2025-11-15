from abc import ABC, abstractmethod
from typing import List
from ..domain.entity import Card


class CardRepo(ABC):
	@abstractmethod
	def get_cards(self, name : str | None, category: str | None, city: str | None) -> List[Card]:
		pass
	
	@abstractmethod
	def create_card(self, card: Card) -> Card:
		pass
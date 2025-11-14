from abc import ABC, abstractmethod

from ..domain.entity import Card


class CardRepo(ABC):
	@abstractmethod
	def get_card(self, name : str | None, category: str | None, city: str | None) -> Card:
		pass
	
	@abstractmethod
	def create_card(self, card: Card) -> Card:
		pass
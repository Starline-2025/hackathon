from abc import ABC, abstractmethod
from typing import List
from backend.domain.entity import Card


# Абстрактный класс (интерфейс) для репозитория карточек
class CardRepo(ABC):
	# Абстрактный метод для получения карточек с фильтрацией
	@abstractmethod
	def get_cards(self, name: str | None, category: str | None, city: str | None) -> List[Card]:
		# Конкретная реализация будет в наследниках (например, SQL или in-memory репозиторий)
		...
	
	# Абстрактный метод для создания новой карточки
	@abstractmethod
	def create_card(self, card: Card) -> Card:
		# Конкретная реализация будет в наследниках
		...

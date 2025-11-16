from abc import ABC, abstractmethod
from typing import List
from backend.domain.entity import Card


# Абстрактный класс (интерфейс) для сервиса работы с карточками
class CardNKOService(ABC):
	# Абстрактный метод для получения списка карточек с фильтром
	@abstractmethod
	def get_cards_by_filter(self, name: str | None, category: str | None, city: str | None) -> List[Card]:
		# Метод не реализован здесь, он должен быть реализован в наследниках
		...
	
	# Абстрактный метод для создания новой карточки
	@abstractmethod
	def create_card(self, card: Card) -> Card:
		# Метод не реализован здесь, реализация будет в конкретном сервисе
		...

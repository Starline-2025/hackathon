from typing import List
from backend.app.usecase import CardNKOService
from backend.domain.repo import CardRepo
from backend.domain.entity import Card

# Реализация сервиса CardNKOService
class CardNKOServiceImpl(CardNKOService):
    def __init__(self, repo: CardRepo):
        # Инициализация сервиса с репозиторием для работы с карточками
        # Репозиторий отвечает за взаимодействие с базой данных или хранилищем
        self._repo = repo

    # Метод для получения списка карточек с фильтрацией
    def get_cards_by_filter(self, name: str | None, category: str | None, city: str | None) -> List[Card]:
        # Вызываем метод репозитория, который возвращает карточки с учетом фильтров
        cards = self._repo.get_cards(name, category, city)
        return cards  # Возвращаем список карточек

    # Метод для создания новой карточки
    def create_card(self, card: Card) -> Card:
        # Вызываем метод репозитория для создания карточки в базе данных
        card = self._repo.create_card(card)
        return card  # Возвращаем созданную карточку

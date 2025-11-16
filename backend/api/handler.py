from fastapi import APIRouter, Depends
from typing import List

from backend.api.exceptions.error import Error
from backend.app.usecase import CardNKOService
from backend.infra.di.di import get_card_service, get_error
from backend.api.models.model import Card

# Создаем роутер FastAPI для группы маршрутов, связанных с "cards"
router = APIRouter(tags=["cards"])

# GET /cards — получение списка карточек с возможностью фильтрации
@router.get("/cards", response_model=List[Card], response_model_exclude_none=True)
def get_cards_by_filter(
    name: str | None = None,        # Фильтр по имени (необязательный)
    city: str | None = None,        # Фильтр по городу (необязательный)
    category: str | None = None,    # Фильтр по категории (необязательный)
    cards_service: CardNKOService = Depends(get_card_service),  # Внедрение зависимости: сервис карточек
    error: Error = Depends(get_error),                           # Внедрение зависимости: обработчик ошибок
):
    try:
        # Получаем список карточек с учетом фильтров
        cards = cards_service.get_cards_by_filter(name=name, city=city, category=category)
        return cards  # Возвращаем клиенту
    except Exception as e:
        # Если произошла ошибка, используем общий обработчик ошибок
        return error.handle(e)

# POST /cards — создание новой карточки
@router.post("/cards", response_model=Card, response_model_exclude_none=True)
def create_card(
    req: Card,  # Данные карточки из тела запроса
    cards_service: CardNKOService = Depends(get_card_service),  # Сервис для работы с карточками
    error: Error = Depends(get_error),                           # Обработчик ошибок
):
    try:
        # Создаем карточку через сервис
        created = cards_service.create_card(req)
        return created
    except Exception as e:
        # Обрабатываем все исключения через Error
        return error.handle(e)

# GET /health — проверка здоровья сервиса
@router.get("/health")
def health():
    # Возвращаем простой статус, чтобы проверить, работает ли API
    return {"status": "ok"}

from typing import List
from sqlalchemy import func

from backend.infra.errors.error import InvalidGetCards, InvalidCreateCard
from backend.domain.entity import Card
from backend.domain.errors import CardsNotFoundException
from backend.domain.repo import CardRepo
from backend.infra.db.db_connector import get_session
from backend.infra.models.model import CardNKOORM
from backend.logger import error_logger


# Конкретная реализация репозитория карточек
class CardRepoImpl(CardRepo):
	# Получение карточек с фильтрацией
	def get_cards(self, name: str | None, category: str | None, city: str | None) -> List[Card]:
		try:
			# Создаем сессию SQLAlchemy
			with get_session() as session:
				# Начальный запрос: выбираем только верифицированные карточки
				query = session.query(CardNKOORM).filter(CardNKOORM.is_verificate)
				
				# Применяем фильтры, если они указаны
				if name:
					query = query.filter(CardNKOORM.name == name)
				if category:
					# Сравнение категорий без учета регистра
					query = query.filter(func.lower(CardNKOORM.category) == category.lower())
				if city:
					# Сравнение города без учета регистра
					query = query.filter(func.lower(CardNKOORM.city) == city.lower())
				
				# Выполняем запрос и получаем все результаты
				results = query.all()
				
				# Если карточки не найдены — выбрасываем специализированное исключение
				if not results:
					raise CardsNotFoundException()
				
				# Конвертируем ORM-объекты в сущности домена (Card)
				return [Card.from_orm(obj) for obj in results]
		
		except CardsNotFoundException as e:
			# Пробрасываем исключение дальше без изменений
			raise e
		except Exception as e:
			# Логируем ошибку и выбрасываем исключение инфраструктурного уровня
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetCards()
	
	# Создание новой карточки
	def create_card(self, card: Card) -> Card:
		try:
			# Создаем сессию SQLAlchemy
			with get_session() as session:
				# Создаем ORM-объект на основе сущности домена
				new_card = CardNKOORM(
					name=card.name,
					category=card.category,
					description=card.description,
					contacts=card.contacts,
					city=card.city,
					img=card.img,
					website=card.website,
					lat=card.lat,
					lng=card.lng,
					address=card.address,
				)
				
				# Добавляем объект в сессию
				session.add(new_card)
				# Фиксируем изменения в базе данных
				session.commit()
				# Обновляем объект, чтобы получить сгенерированные поля (например, id)
				session.refresh(new_card)
				
				# Конвертируем ORM-объект обратно в сущность домена и возвращаем
				return Card.from_orm(new_card)
		
		except Exception as e:
			# Логируем ошибку и выбрасываем исключение инфраструктурного уровня
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidCreateCard()

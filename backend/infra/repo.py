from typing import List
from sqlalchemy import func

from backend.infra.errors.error import InvalidGetCards, InvalidCreateCard
from backend.domain.entity import Card
from backend.domain.errors import CardsNotFoundException
from backend.domain.repo import CardRepo
from backend.infra.db.db_connector import get_session
from backend.infra.models.model import CardNKOORM
from backend.logger import error_logger

class CardRepoImpl(CardRepo):
	def get_cards(self, name : str | None, category: str | None, city: str | None) -> List[Card]:
		try:
			with get_session() as session:
				query = session.query(CardNKOORM).filter(CardNKOORM.is_verificate)
				if name:
					query = query.filter(CardNKOORM.name == name)
				if category:
					query = query.filter(func.lower(CardNKOORM.category) == category.lower())
				if city:
					query = query.filter(func.lower(CardNKOORM.city) == city.lower())
				results = query.all()
				if not results:
					raise CardsNotFoundException()
				return [Card.from_orm(obj) for obj in results]
		except CardsNotFoundException as e:
			raise e
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidGetCards()
		
	def create_card(self, card: Card) -> Card:
		try:
			with get_session() as session:
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
				session.add(new_card)
				session.commit()
				session.refresh(new_card)
				return Card.from_orm(new_card)
		except Exception as e:
			error_logger.error(f"{str(e)}", exc_info=True)
			raise InvalidCreateCard()
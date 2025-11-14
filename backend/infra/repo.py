from typing import List
from ..domain.entity import Card
from ..domain.repo import CardRepo
from ..infra.db.db_connector import get_session
from ..infra.models.model import CardNKOORM


class CardRepoImpl(CardRepo):
	def get_cards(self, name : str | None, category: str | None, city: str | None) -> List[Card]:
		with get_session() as session:
			query = session.query(CardNKOORM)
			if name:
				query = query.filter(CardNKOORM.name == name)
			if category:
				query = query.filter(CardNKOORM.category == category)
			if city:
				query = query.filter(CardNKOORM.city == city)
			results = query.all()
			if not results:
				#TODO: Доделать ошибку
				raise ...
			return [Card.from_orm(obj) for obj in results]
		
	def create_card(self, card: Card) -> Card:
		with get_session() as session:
			new_card = CardNKOORM(
				name=card.name,
				category=card.category,
				description=card.description,
				contacts=card.contacts,
				city=card.city,
				img=card.img,
				website=card.website,
			)
			session.add(new_card)
			session.commit()
			session.refresh(new_card)
			return Card.from_orm(new_card)
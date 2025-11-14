from pip._internal.models import link

from ..domain.entity import Card
from ..domain.repo import CardRepo
from ..infra.db.db_connector import get_session
from ..infra.models.model import CardNKOORM


class CardRepoImpl(CardRepo):
	def get_card(self, name : str | None, category: str | None, city: str | None) -> Card:
		with get_session() as session:
			...
		
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
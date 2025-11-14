from dataclasses import dataclass

@dataclass
class Card:
	name: str
	category: str
	description: str
	contacts: str
	city: str
	img: str
	website: str
	
	@classmethod
	def from_orm(cls, card_orm):
		return cls(
			name=card_orm.name,
			category=card_orm.category,
			description=card_orm.description,
			contacts=card_orm.contacts,
			city=card_orm.city,
			img=card_orm.img,
			website=card_orm.website,
		)
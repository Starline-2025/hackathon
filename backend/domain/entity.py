from dataclasses import dataclass


@dataclass
class Card:
	name: str
	category: str
	description: str
	city: str
	website: str
	lat: float
	lng: float
	address: str | None = None
	contacts: str | None = None
	img: str | None = None
	
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
			lat=card_orm.lat,
			lng=card_orm.lng,
			address=card_orm.address,
		)
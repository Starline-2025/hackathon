from dataclasses import dataclass

# Используем @dataclass для автоматического создания методов __init__, __repr__ и других
@dataclass
class Card:
    # Обязательные поля карточки
    name: str
    category: str
    description: str
    city: str
    website: str
    lat: float  # Широта
    lng: float  # Долгота

    # Необязательные поля (по умолчанию None)
    address: str | None = None
    contacts: str | None = None
    img: str | None = None

    # Метод класса для создания экземпляра из ORM-объекта (например, SQLAlchemy)
    @classmethod
    def from_orm(cls, card_orm):
        # Берем все поля из ORM-модели и передаем их в конструктор dataclass
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

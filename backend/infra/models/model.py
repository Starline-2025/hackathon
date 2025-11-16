from sqlalchemy import Column, String, Boolean, Integer, text, Float
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для всех ORM моделей SQLAlchemy
Base = declarative_base()

# ORM-модель для таблицы "cards_nko"
class CardNKOORM(Base):
    # Название таблицы в базе данных
    __tablename__ = 'cards_nko'

    # Поля таблицы
    id = Column(Integer, autoincrement=True, primary_key=True)  # Уникальный идентификатор, автоинкремент
    name = Column(String, nullable=False)                       # Название карточки, обязательно
    category = Column(String, nullable=False)                   # Категория, обязательно
    description = Column(String, nullable=False)                # Описание, обязательно
    contacts = Column(String, nullable=True)                    # Контакты, необязательное поле
    city = Column(String, nullable=False)                       # Город, обязательно
    address = Column(String, nullable=True)                     # Адрес, необязательное поле
    img = Column(String, nullable=True)                         # Ссылка на изображение, необязательное поле
    website = Column(String, nullable=False)                    # Веб-сайт, обязательно
    lat = Column(Float, nullable=True)                           # Широта, необязательное поле
    lng = Column(Float, nullable=True)                           # Долгота, необязательное поле
    is_verificate = Column(Boolean, nullable=False, default=False, server_default=text("false"))
    # Флаг верификации, по умолчанию False

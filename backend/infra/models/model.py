from sqlalchemy import Column, String, Boolean, Integer, text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CardNKOORM(Base):
    __tablename__ = 'cards_nko'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=False)
    contacts = Column(String, nullable=True)
    city = Column(String, nullable=False)
    address = Column(String, nullable=True)
    img = Column(String, nullable=True)
    website = Column(String, nullable=False)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)
    is_verificate = Column(Boolean, nullable=False, default=False, server_default=text("false"))


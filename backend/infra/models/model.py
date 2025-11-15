from sqlalchemy import Column, String, Boolean, Integer, text
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
    img = Column(String, nullable=True)
    website = Column(String, nullable=False)
    is_verificate = Column(Boolean, nullable=False, default=False, server_default=text("false"))


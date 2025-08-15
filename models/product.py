from sqlalchemy import Column, Integer, String, Float
from db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    category_id = Column(Integer, nullable=True)

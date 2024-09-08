from sqlalchemy import Column, Integer, String, Float

from core.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Adjust the size (255 in this example)
    price = Column(Float)
    stock_level = Column(Integer)

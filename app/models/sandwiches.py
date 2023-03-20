from app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float, DECIMAL
from sqlalchemy.orm import relationship


class Sandwich(Base):
    __tablename__ = "sandwiches"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_size = Column(String(50), nullable=False)
    price = Column(DECIMAL(5, 2), nullable=False)

from app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship


class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)

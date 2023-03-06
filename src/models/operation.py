from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.models.base import Base
from sqlalchemy.orm import relationship


class Operation(Base):

    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    operation = Column(String)
    called_date = Column(DateTime)
    called_by = Column(Integer, ForeignKey('users.id'), nullable=True)

    user_called = relationship('User', foreign_keys=[called_by], backref='called_operations')

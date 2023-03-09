from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.models.base import Base


class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_at = Column(DateTime)

    user_called = relationship('User', foreign_keys=[created_by], backref='created_models')

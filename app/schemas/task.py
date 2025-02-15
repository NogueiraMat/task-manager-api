from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

from schemas.base import Base
from schemas.user import User


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, index=True)
    status = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    user_id = Column(ForeignKey(User.id), nullable=False)


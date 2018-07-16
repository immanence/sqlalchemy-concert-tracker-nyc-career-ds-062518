from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class UserShow(Base):
    __tablename__ = 'user_shows'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    show_id = Column(Integer, ForeignKey('shows.id'), primary_key=True)

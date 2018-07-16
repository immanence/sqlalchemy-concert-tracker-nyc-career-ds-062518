from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from venue import Venue

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    capacity = Column(Integer)
    venues = relationship("Venue", back_populates = 'city')

from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from show import Show

class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    shows = relationship("Show", back_populates = 'band')

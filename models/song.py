from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from show import Show

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    shows = relationship("Show", secondary="show_songs", back_populates="songs")
    show_songs = relationship("ShowSong", back_populates = "song")

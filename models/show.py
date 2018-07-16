from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Show(Base):
    __tablename__ = 'shows'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    users = relationship("User", secondary = 'user_shows')
    songs = relationship("Song", secondary = 'show_songs', back_populates = "shows")
    show_songs = relationship("ShowSong", back_populates = "show")
    band_id = Column(Integer, ForeignKey('bands.id'))
    band = relationship("Band", back_populates = 'shows')
    venue_id = Column(Integer, ForeignKey('venues.id'))
    venue = relationship("Venue", back_populates = 'shows')

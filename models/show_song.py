from base import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from song import Song
from show import Show


class ShowSong(Base):
    __tablename__ = 'show_songs'
    id = Column(Integer, primary_key=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    song_id = Column(Integer, ForeignKey('songs.id'))
    length = Column(Integer)
    notes = Column(Text)
    song = relationship("Song", back_populates="show_songs")
    show = relationship("Show", back_populates="show_songs")

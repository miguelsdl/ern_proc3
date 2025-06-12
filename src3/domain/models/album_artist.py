from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .base import Base

class AlbumArtist(Base):
    __tablename__ = 'albums_artists'
    __table_args__ = {'schema': 'feed'}

    id_album_artist = Column(Integer, primary_key=True, autoincrement=True)
    id_album = Column(Integer)
    id_artist = Column(Integer)
    artist_role_album_artist = Column(String(100))
    active_album_artist = Column(Boolean, default=True, nullable=False)
    manually_edited_album_artist = Column(Boolean, default=False, nullable=False)
    audi_manually_edited_album_artist = Column(DateTime)
    audi_edited_album_artist = Column(DateTime)
    audi_created_album_artist = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
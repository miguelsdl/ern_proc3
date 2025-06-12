from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .base import Base

class TrackArtist(Base):
    __tablename__ = 'tracks_artists'
    __table_args__ = {'schema': 'feed'}

    id_track_artist = Column(Integer, primary_key=True, autoincrement=True)
    id_track = Column(Integer)
    id_artist = Column(Integer)
    artist_role_track_artist = Column(String(100))
    audi_edited_track_artist = Column(DateTime)
    audi_created_track_artist = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
    active_track_artist = Column(Boolean, default=True, nullable=False)
    manually_edited_track_artist = Column(Boolean, default=False, nullable=False)
    audi_manually_edited_track_artist = Column(DateTime)
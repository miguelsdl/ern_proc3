from sqlalchemy import Column, Integer, DateTime
from .base import Base

class AlbumTrack(Base):
    __tablename__ = 'albums_tracks'
    __table_args__ = {'schema': 'feed'}

    id_album_track = Column(Integer, primary_key=True, autoincrement=True)
    id_album = Column(Integer)
    id_track = Column(Integer)
    volume_album_track = Column(Integer)
    number_album_track = Column(Integer)
    audi_edited_album_track = Column(DateTime)
    audi_created_album_track = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
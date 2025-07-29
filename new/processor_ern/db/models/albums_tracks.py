from sqlalchemy import Column, Integer, DateTime, Boolean
from .mixins import SaveByFieldsMixin
from .base import  Base


class AlbumTrack(SaveByFieldsMixin, Base):
    __tablename__ = "albums_tracks"
    __unique_fields__ = ('id_album', 'id_track')

    id_album_track = Column(Integer, primary_key=True, autoincrement=True)
    id_album = Column(Integer)
    id_track = Column(Integer)

    volume_album_track = Column(Integer)
    number_album_track = Column(Integer)

    active_album_track = Column(Boolean, default=True)
    audi_edited_album_track = Column(DateTime)
    audi_created_album_track = Column(DateTime)
    update_id_message = Column(Integer, default=0)
    insert_id_message = Column(Integer, default=0)

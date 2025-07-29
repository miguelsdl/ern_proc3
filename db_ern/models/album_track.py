from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base
from .mixins import SaveByFieldsMixin

class AlbumTrack(SaveByFieldsMixin, Base):
    __tablename__ = 'album_track'
    id_album_track = Column(Integer, primary_key=True)
    id_album = Column(Integer, nullable=False)
    id_track = Column(Integer, nullable=False)
    description = Column(String(500))

    __unique_fields__ = ('id_album', 'id_track')  # 🧠 Clave lógica

    def __repr__(self):
        return f"AlbumTrack(id_album_track={self.id_album_track}, id_album={self.id_album}, id_track={self.id_track}, description='{self.description}')"
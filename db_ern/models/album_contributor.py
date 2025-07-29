from sqlalchemy import Column, Integer, String
from .base import Base
from .mixins import SaveByFieldsMixin

class AlbumContributor(SaveByFieldsMixin, Base):
    __tablename__ = 'album_contributor'
    id_album_contributor = Column(Integer, primary_key=True)
    id_album = Column(Integer, nullable=False)
    id_contributor = Column(Integer, nullable=False)
    rol = Column(String(100))

    __unique_fields__ = ('id_album', 'id_contributor')

    def __repr__(self):
        return (f"AlbumContributor(id_album_contributor={self.id_album_contributor}, id_album={self.id_album}, "
                f"id_contributor={self.id_contributor}, rol='{self.rol}')")

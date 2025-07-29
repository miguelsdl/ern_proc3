from sqlalchemy import Column, Integer, String
from .base import Base
from .mixins import SaveByFieldsMixin

class TrackContributor(SaveByFieldsMixin, Base):
    __tablename__ = 'track_contributor'
    id_track_contributor = Column(Integer, primary_key=True)
    id_track = Column(Integer, nullable=False)
    id_contributor = Column(Integer, nullable=False)
    rol = Column(String(100))

    __unique_fields__ = ('id_track', 'id_contributor')

    def __repr__(self):
        return (f"TrackContributor(id_track_contributor={self.id_track_contributor}, id_track={self.id_track}, "
                f"id_contributor={self.id_contributor}, rol='{self.rol}')")
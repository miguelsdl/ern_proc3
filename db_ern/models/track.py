from sqlalchemy import Column, Integer, String
from .base import Base
from .mixins import SaveByFieldsMixin


class Track(SaveByFieldsMixin, Base):
    __tablename__ = 'tracks'
    __unique_fields__ = ('name',)
    id_album = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(500))

    def __repr__(self):
        return f"Track(id_album={self.id_album}, name='{self.name}', description='{self.description}')"
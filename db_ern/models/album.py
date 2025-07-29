from sqlalchemy import Column, Integer, String
from .base import Base
from .mixins import SaveByFieldsMixin

class Album(SaveByFieldsMixin, Base):
    __tablename__ = 'albums'
    __unique_fields__ = ('name',)
    id_album = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)  # <- con longitud
    description = Column(String(500))  # <- opcional longitud también

    def __repr__(self):
        return f"Album(id_album={self.id_album}, name='{self.name}', description='{self.description}')"
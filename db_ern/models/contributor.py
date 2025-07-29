from sqlalchemy import Column, Integer, String, Boolean
from .base import Base
from .mixins import SaveByFieldsMixin

class Contributor(SaveByFieldsMixin, Base):
    __tablename__ = 'contributors'
    id_contributor = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    active = Column(Boolean, default=True)

    __unique_fields__ = ('name',)

    def __repr__(self):
        return f"Contributor(id_contributor={self.id_contributor}, name='{self.name}', active={self.active})"

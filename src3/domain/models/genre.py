from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .base import Base

class Genre(Base):
    __tablename__ = 'genres'
    __table_args__ = {'schema': 'feed'}

    id_genre = Column(Integer, primary_key=True, autoincrement=True)
    name_genre = Column(String(100))
    active_genre = Column(Boolean)
    audi_edited_genre = Column(DateTime)
    audi_created_genre = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
from sqlalchemy import Column, Integer, Text, Boolean, DateTime, JSON
from .base import Base

class Artist(Base):
    __tablename__ = 'artists'
    __table_args__ = {'schema': 'feed'}

    id_artist = Column(Integer, primary_key=True, autoincrement=True)
    name_artist = Column(Text)
    id_parent_artist = Column(Integer)
    active_artist = Column(Boolean)
    specific_data_artist = Column(JSON)
    audi_edited_artist = Column(DateTime)
    audi_created_artist = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
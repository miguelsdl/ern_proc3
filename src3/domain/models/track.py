from sqlalchemy import Column, Integer, String, Text, Time, Boolean, DateTime, JSON
from .base import Base

class Track(Base):
    __tablename__ = 'tracks'
    __table_args__ = {'schema': 'feed'}

    id_track = Column(Integer, primary_key=True, autoincrement=True)
    isrc_track = Column(String(20))
    name_track = Column(Text)
    version_track = Column(Text)
    length_track = Column(Time)
    explicit_track = Column(Boolean)
    active_track = Column(Boolean)
    specific_data_track = Column(JSON)
    audi_edited_track = Column(DateTime)
    audi_created_track = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
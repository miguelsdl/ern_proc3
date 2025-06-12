from sqlalchemy import Column, Integer, String, Text, Time, DateTime, Boolean, JSON
from .base import Base

class Album(Base):
    __tablename__ = 'albums'
    __table_args__ = {'schema': 'feed'}

    id_album = Column(Integer, primary_key=True, autoincrement=True)
    upc_album = Column(String(20))
    name_album = Column(Text)
    subtitle_album = Column(String(200))
    release_type_album = Column(String(25))
    length_album = Column(Time)
    tracks_qty_album = Column(Integer)
    release_date_album = Column(DateTime)
    active_album = Column(Boolean)
    specific_data_album = Column(JSON)
    audi_edited_album = Column(DateTime)
    audi_created_album = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
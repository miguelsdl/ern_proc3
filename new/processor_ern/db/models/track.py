from sqlalchemy import Column, Integer, String, Text, Time, DateTime, Boolean, JSON, TIMESTAMP
from .mixins import SaveByFieldsMixin
from .base import  Base
from sqlalchemy.orm import relationship


class Track(SaveByFieldsMixin, Base):
    __tablename__ = "tracks"
    __unique_fields__ = ('isrc_track',)

    id_track = Column(Integer, primary_key=True, autoincrement=True)
    isrc_track = Column(String(20), unique=True)
    grid_track = Column(Text)
    name_track = Column(Text)
    version_track = Column(Text)
    length_track = Column(Time)
    explicit_track = Column(Boolean)
    active_track = Column(Boolean)
    specific_data_track = Column(JSON)
    audi_edited_track = Column(DateTime)
    audi_created_track = Column(DateTime)
    update_id_message = Column(Integer, default=0)
    insert_id_message = Column(Integer, default=0)

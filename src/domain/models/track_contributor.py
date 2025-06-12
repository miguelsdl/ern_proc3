from sqlalchemy import Column, Integer, Text, DateTime
from .base import Base

class TrackContributor(Base):
    __tablename__ = 'tracks_contributors'
    __table_args__ = {'schema': 'feed'}

    id_track_contri = Column(Integer, primary_key=True, autoincrement=True)
    id_track = Column(Integer)
    id_contri = Column(Integer)
    contributor_role_track_contri = Column(Text)
    contributor_role_type_track_contri = Column(Text)
    audi_edited_track_contri = Column(DateTime)
    audi_created_track_contri = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
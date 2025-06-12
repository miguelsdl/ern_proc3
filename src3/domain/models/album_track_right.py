from sqlalchemy import Column, BigInteger, Integer, DateTime, Text, JSON
from .base import Base

class AlbumTrackRight(Base):
    __tablename__ = 'albums_tracks_rights'
    __table_args__ = {'schema': 'feed'}

    id_albtraright = Column(BigInteger, primary_key=True, autoincrement=True)
    id_album_track = Column(BigInteger)
    id_dist = Column(Integer)
    id_label = Column(Integer)
    id_cmt = Column(Integer)
    id_use_type = Column(Integer)
    cnty_ids_albtraright = Column(JSON)
    start_date_albtraright = Column(DateTime)
    end_date_albtraright = Column(DateTime)
    pline_text_albtraright = Column(Text)
    pline_year_albtraright = Column(Text)
    audi_edited_albtraright = Column(DateTime)
    audi_created_albtraright = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
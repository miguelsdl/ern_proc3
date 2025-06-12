from sqlalchemy import Column, BigInteger, Integer, DateTime, JSON
from .base import Base

class AlbumRight(Base):
    __tablename__ = 'albums_rights'
    __table_args__ = {'schema': 'feed'}

    id_albright = Column(BigInteger, primary_key=True, autoincrement=True)
    id_album = Column(BigInteger)
    id_dist = Column(Integer)
    id_label = Column(Integer)
    id_cmt = Column(Integer)
    id_use_type = Column(Integer)
    cnty_ids_albright = Column(JSON)
    start_date_albright = Column(DateTime)
    end_date_albright = Column(DateTime)
    audi_edited_albright = Column(DateTime)
    audi_created_albright = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
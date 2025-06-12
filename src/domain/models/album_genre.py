from sqlalchemy import Column, Integer, DateTime
from .base import Base

class AlbumGenre(Base):
    __tablename__ = 'albums_genres'
    __table_args__ = {'schema': 'feed'}

    id_album_genre = Column(Integer, primary_key=True, autoincrement=True)
    id_album = Column(Integer)
    id_genre = Column(Integer)
    audi_edited_album_genre = Column(DateTime)
    audi_created_album_genre = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
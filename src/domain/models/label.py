from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .base import Base

class Label(Base):
    __tablename__ = 'labels'
    __table_args__ = {'schema': 'feed'}

    id_label = Column(Integer, primary_key=True, autoincrement=True)
    name_label = Column(String(50))
    active_label = Column(Boolean)
    audi_edited_label = Column(DateTime)
    audi_created_label = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
from sqlalchemy import Column, Integer, Text, DateTime
from .base import Base

class UseType(Base):
    __tablename__ = 'use_types'
    __table_args__ = {'schema': 'feed'}

    id_use_type = Column(Integer, primary_key=True, autoincrement=True)
    name_use_type = Column(Text)
    description_use_type = Column(Text)
    audi_edited_use_type = Column(DateTime)
    audi_created_use_type = Column(DateTime)
    update_id_message = Column(Integer, default=0)
    insert_id_message = Column(Integer, default=0)
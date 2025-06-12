from sqlalchemy import Column, Integer, Text, DateTime
from .base import Base

class ComercialModelType(Base):
    __tablename__ = 'comercial_model_types'
    __table_args__ = {'schema': 'feed'}

    id_cmt = Column(Integer, primary_key=True, autoincrement=True)
    name_cmt = Column(Text)
    description_cmt = Column(Text)
    audi_edited_cmt = Column(DateTime)
    audi_created_cmt = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
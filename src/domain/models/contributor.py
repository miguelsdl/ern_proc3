from sqlalchemy import Column, Integer, Text, Boolean, DateTime
from .base import Base

class Contributor(Base):
    __tablename__ = 'contributors'
    __table_args__ = {'schema': 'feed'}

    id_contri = Column(Integer, primary_key=True, autoincrement=True)
    name_contri = Column(Text)
    active_contri = Column(Boolean)
    audi_edited_contri = Column(DateTime)
    audi_created_contri = Column(DateTime)
    update_id_message = Column(Integer, default=0, nullable=False)
    insert_id_message = Column(Integer, default=0, nullable=False)
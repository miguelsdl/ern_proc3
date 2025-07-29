from sqlalchemy import Column, Integer, String, Text, Time, DateTime, Boolean, JSON
from .mixins import SaveByFieldsMixin

from .base import  Base
from .descriptor import Descriptor


class Album(SaveByFieldsMixin, Descriptor, Base):
    __tablename__ = "albums"
    __unique_fields__ = ('upc_album',)

    id_album = Column(Integer, primary_key=True, autoincrement=True)
    upc_album = Column(String(20), unique=True)
    grid_album = Column(Text)
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
    update_id_message = Column(Integer, default=0)
    insert_id_message = Column(Integer, default=0)

    def __init__(self, *args, **kwargs):
        SaveByFieldsMixin.__init__(self)
        Descriptor.__init__(self, *args, **kwargs)
        Base.__init__(self)

    def __repr__(self):
        return (
            f"Album(id_album={self.id_album}, upc_album='{self.upc_album}', "
            f"name_album='{self.name_album}', release_date_album={self.release_date_album})"
        )
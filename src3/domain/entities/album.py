# src3/main/python/com/tuempresa/ddex/domain/entities/albums/Album.py
from dataclasses import dataclass
from datetime import datetime
import json
from typing import Optional, Union


@dataclass
class Album:
    """Entidad que representa un álbum musical en el sistema DDEX"""

    id_album: Optional[int] = None
    upc_album: Optional[str] = None
    name_album: Optional[str] = None
    subtitle_album: Optional[str] = None
    release_type_album: Optional[str] = None
    length_album: Optional[datetime.time] = None
    tracks_qty_album: Optional[int] = None
    release_date_album: Optional[datetime] = None
    active_album: Optional[bool] = None
    specific_data_album: Optional[dict] = None
    audi_edited_album: Optional[datetime] = None
    audi_created_album: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        # Convertimos el JSON string a dict si es necesario
        if isinstance(self.specific_data_album, str):
            self.specific_data_album = json.loads(self.specific_data_album)

        # Validaciones básicas
        if self.active_album is not None:
            self.active_album = bool(self.active_album)

        # Aseguramos que los timestamps estén en formato datetime
        if isinstance(self.audi_created_album, str):
            self.audi_created_album = datetime.fromisoformat(self.audi_created_album.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_album, str):
            self.audi_edited_album = datetime.fromisoformat(self.audi_edited_album.replace('Z', '+00:00'))


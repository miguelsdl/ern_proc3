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


# src3/main/python/com/tuempresa/ddex/domain/entities/albums/AlbumArtist.py
@dataclass
class AlbumArtist:
    """Entidad que representa la relación entre un álbum y un artista"""

    id_album_artist: Optional[int] = None
    id_album: Optional[int] = None
    id_artist: Optional[int] = None
    artist_role_album_artist: Optional[str] = None
    active_album_artist: Optional[bool] = None
    manually_edited_album_artist: Optional[bool] = None
    audi_manually_edited_album_artist: Optional[datetime] = None
    audi_edited_album_artist: Optional[datetime] = None
    audi_created_album_artist: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if self.active_album_artist is not None:
            self.active_album_artist = bool(self.active_album_artist)
        if self.manually_edited_album_artist is not None:
            self.manually_edited_album_artist = bool(self.manually_edited_album_artist)


# src3/main/python/com/tuempresa/ddex/domain/entities/artists/Artist.py
@dataclass
class Artist:
    """Entidad que representa un artista en el sistema DDEX"""

    id_artist: Optional[int] = None
    name_artist: Optional[str] = None
    id_parent_artist: Optional[int] = None
    active_artist: Optional[bool] = None
    specific_data_artist: Optional[dict] = None
    audi_edited_artist: Optional[datetime] = None
    audi_created_artist: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if isinstance(self.specific_data_artist, str):
            self.specific_data_artist = json.loads(self.specific_data_artist)
        if self.active_artist is not None:
            self.active_artist = bool(self.active_artist)
        if isinstance(self.audi_created_artist, str):
            self.audi_created_artist = datetime.fromisoformat(self.audi_created_artist.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_artist, str):
            self.audi_edited_artist = datetime.fromisoformat(self.audi_edited_artist.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/tracks/Track.py
@dataclass
class Track:
    """Entidad que representa una pista musical en el sistema DDEX"""

    id_track: Optional[int] = None
    isrc_track: Optional[str] = None
    name_track: Optional[str] = None
    version_track: Optional[str] = None
    length_track: Optional[datetime.time] = None
    explicit_track: Optional[bool] = None
    active_track: Optional[bool] = None
    specific_data_track: Optional[dict] = None
    audi_edited_track: Optional[datetime] = None
    audi_created_track: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if isinstance(self.specific_data_track, str):
            self.specific_data_track = json.loads(self.specific_data_track)
        if self.active_track is not None:
            self.active_track = bool(self.active_track)
        if self.explicit_track is not None:
            self.explicit_track = bool(self.explicit_track)
        if isinstance(self.audi_created_track, str):
            self.audi_created_track = datetime.fromisoformat(self.audi_created_track.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_track, str):
            self.audi_edited_track = datetime.fromisoformat(self.audi_edited_track.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/albums/AlbumGenre.py
@dataclass
class AlbumGenre:
    """Entidad que representa la relación entre un álbum y un género"""

    id_album_genre: Optional[int] = None
    id_album: Optional[int] = None
    id_genre: Optional[int] = None
    audi_edited_album_genre: Optional[datetime] = None
    audi_created_album_genre: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if isinstance(self.audi_created_album_genre, str):
            self.audi_created_album_genre = datetime.fromisoformat(self.audi_created_album_genre.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_album_genre, str):
            self.audi_edited_album_genre = datetime.fromisoformat(self.audi_edited_album_genre.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/albums/AlbumRights.py
@dataclass
class AlbumRights:
    """Entidad que representa los derechos de un álbum"""

    id_albright: Optional[int] = None
    id_album: Optional[int] = None
    id_dist: Optional[int] = None
    id_label: Optional[int] = None
    id_cmt: Optional[int] = None
    id_use_type: Optional[int] = None
    cnty_ids_albright: Optional[dict] = None
    start_date_albright: Optional[datetime] = None
    end_date_albright: Optional[datetime] = None
    audi_edited_albright: Optional[datetime] = None
    audi_created_albright: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if isinstance(self.cnty_ids_albright, str):
            self.cnty_ids_albright = json.loads(self.cnty_ids_albright)
        if isinstance(self.audi_created_albright, str):
            self.audi_created_albright = datetime.fromisoformat(self.audi_created_albright.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_albright, str):
            self.audi_edited_albright = datetime.fromisoformat(self.audi_edited_albright.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/albums/AlbumTrack.py
@dataclass
class AlbumTrack:
    """Entidad que representa la relación entre un álbum y una pista"""

    id_album_track: Optional[int] = None
    id_album: Optional[int] = None
    id_track: Optional[int] = None
    volume_album_track: Optional[int] = None
    number_album_track: Optional[int] = None
    audi_edited_album_track: Optional[datetime] = None
    audi_created_album_track: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if isinstance(self.audi_created_album_track, str):
            self.audi_created_album_track = datetime.fromisoformat(self.audi_created_album_track.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_album_track, str):
            self.audi_edited_album_track = datetime.fromisoformat(self.audi_edited_album_track.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/albums/AlbumTrackRights.py
@dataclass
class AlbumTrackRights:
    """Entidad que representa los derechos de una pista de álbum"""

    id_albtraright: Optional[int] = None
    id_album_track: Optional[int] = None
    id_dist: Optional[int] = None
    id_label: Optional[int] = None
    id_cmt: Optional[int] = None
    id_use_type: Optional[int] = None
    cnty_ids_albtraright: Optional[dict] = None
    start_date_albtraright: Optional[datetime] = None
    end_date_albtraright: Optional[datetime] = None
    pline_text_albtraright: Optional[str] = None
    pline_year_albtraright: Optional[str] = None
    audi_edited_albtraright: Optional[datetime] = None
    audi_created_albtraright: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if isinstance(self.cnty_ids_albtraright, str):
            self.cnty_ids_albtraright = json.loads(self.cnty_ids_albtraright)
        if isinstance(self.audi_created_albtraright, str):
            self.audi_created_albtraright = datetime.fromisoformat(self.audi_created_albtraright.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_albtraright, str):
            self.audi_edited_albtraright = datetime.fromisoformat(self.audi_edited_albtraright.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/genres/Genre.py
@dataclass
class Genre:
    """Entidad que representa un género musical"""

    id_genre: Optional[int] = None
    name_genre: Optional[str] = None
    active_genre: Optional[bool] = None
    audi_edited_genre: Optional[datetime] = None
    audi_created_genre: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if self.active_genre is not None:
            self.active_genre = bool(self.active_genre)
        if isinstance(self.audi_created_genre, str):
            self.audi_created_genre = datetime.fromisoformat(self.audi_created_genre.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_genre, str):
            self.audi_edited_genre = datetime.fromisoformat(self.audi_edited_genre.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/labels/Label.py
@dataclass
class Label:
    """Entidad que representa un sello discográfico"""

    id_label: Optional[int] = None
    name_label: Optional[str] = None
    active_label: Optional[bool] = None
    audi_edited_label: Optional[datetime] = None
    audi_created_label: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if self.active_label is not None:
            self.active_label = bool(self.active_label)
        if isinstance(self.audi_created_label, str):
            self.audi_created_label = datetime.fromisoformat(self.audi_created_label.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_label, str):
            self.audi_edited_label = datetime.fromisoformat(self.audi_edited_label.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/contributors/Contributor.py
@dataclass
class Contributor:
    """Entidad que representa un colaborador"""

    id_contri: Optional[int] = None
    name_contri: Optional[str] = None
    active_contri: Optional[bool] = None
    audi_edited_contri: Optional[datetime] = None
    audi_created_contri: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if self.active_contri is not None:
            self.active_contri = bool(self.active_contri)
        if isinstance(self.audi_created_contri, str):
            self.audi_created_contri = datetime.fromisoformat(self.audi_created_contri.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_contri, str):
            self.audi_edited_contri = datetime.fromisoformat(self.audi_edited_contri.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/contributors/TrackContributor.py
@dataclass
class TrackContributor:
    """Entidad que representa la relación entre una pista y un colaborador"""

    id_track_contri: Optional[int] = None
    id_track: Optional[int] = None
    id_contri: Optional[int] = None
    contributor_role_track_contri: Optional[str] = None
    contributor_role_type_track_contri: Optional[str] = None
    audi_edited_track_contri: Optional[datetime] = None
    audi_created_track_contri: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __post_init__(self):
        if isinstance(self.audi_created_track_contri, str):
            self.audi_created_track_contri = datetime.fromisoformat(
                self.audi_created_track_contri.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_track_contri, str):
            self.audi_edited_track_contri = datetime.fromisoformat(self.audi_edited_track_contri.replace('Z', '+00:00'))


# src3/main/python/com/tuempresa/ddex/domain/entities/use_types/UseType.py
@dataclass
class UseType:
    """Entidad que representa un tipo de uso comercial"""

    id_use_type: Optional[int] = None
    name_use_type: Optional[str] = None
    description_use_type: Optional[str] = None
    audi_edited_use_type: Optional[datetime] = None
    audi_created_use_type: Optional[datetime] = None
    update_id_message: Optional[int] = None
    insert_id_message: Optional[int] = None

    def __post_init__(self):
        if isinstance(self.audi_created_use_type, str):
            self.audi_created_use_type = datetime.fromisoformat(self.audi_created_use_type.replace('Z', '+00:00'))
        if isinstance(self.audi_edited_use_type, str):
            self.audi_edited_use_type = datetime.fromisoformat(self.audi_edited_use_type.replace('Z', '+00:00'))


# src/main/python/com/tuempresa/ddex/domain/use_cases/album_use_case.py
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class AlbumUseCase:
    """Caso de uso para la gestión de álbumes"""

    album_repository: 'AlbumRepository'
    album_artist_repository: 'AlbumArtistRepository'
    album_genre_repository: 'AlbumGenreRepository'
    album_rights_repository: 'AlbumRightsRepository'

    def create_album(self, album_data: dict) -> 'Album':
        """Crea un nuevo álbum con sus relaciones"""
        # Validación básica
        if not album_data.get('name_album'):
            raise ValueError("El nombre del álbum es obligatorio")

        # Crear el álbum base
        album = Album(
            name_album=album_data['name_album'],
            upc_album=album_data.get('upc_album'),
            release_type_album=album_data.get('release_type_album'),
            release_date_album=album_data.get('release_date_album'),
            specific_data_album=album_data.get('specific_data_album'),
            active_album=album_data.get('active_album', True)
        )

        # Guardar el álbum
        album = self.album_repository.save(album)

        # Crear relaciones con artistas
        if 'artists' in album_data:
            for artist_data in album_data['artists']:
                album_artist = AlbumArtist(
                    id_album=album.id_album,
                    id_artist=artist_data['id_artist'],
                    artist_role_album_artist=artist_data['role'],
                    active_album_artist=artist_data.get('active', True)
                )
                self.album_artist_repository.save(album_artist)

        # Crear relaciones con géneros
        if 'genres' in album_data:
            for genre_id in album_data['genres']:
                album_genre = AlbumGenre(
                    id_album=album.id_album,
                    id_genre=genre_id
                )
                self.album_genre_repository.save(album_genre)

        # Crear derechos del álbum
        if 'rights' in album_data:
            album_rights = AlbumRights(
                id_album=album.id_album,
                id_dist=album_data['rights'].get('distributor_id'),
                id_label=album_data['rights'].get('label_id'),
                id_cmt=album_data['rights'].get('cmt_id'),
                id_use_type=album_data['rights'].get('use_type_id'),
                cnty_ids_albright=album_data['rights'].get('countries'),
                start_date_albright=album_data['rights'].get('start_date'),
                end_date_albright=album_data['rights'].get('end_date')
            )
            self.album_rights_repository.save(album_rights)

        return album

    def get_album(self, album_id: int) -> Optional['Album']:
        """Obtiene un álbum con sus relaciones"""
        album = self.album_repository.find_by_id(album_id)
        if not album:
            return None

        # Obtener relaciones
        album_artists = self.album_artist_repository.find_by_album_id(album_id)
        album_genres = self.album_genre_repository.find_by_album_id(album_id)
        album_rights = self.album_rights_repository.find_by_album_id(album_id)

        # Enrichir el álbum con sus relaciones
        album.artists = album_artists
        album.genres = album_genres
        album.rights = album_rights

        return album

    def update_album(self, album_id: int, album_data: dict) -> 'Album':
        """Actualiza un álbum existente"""
        album = self.get_album(album_id)
        if not album:
            raise ValueError(f"Álbum no encontrado con ID: {album_id}")

        # Actualizar campos del álbum
        if 'name_album' in album_data:
            album.name_album = album_data['name_album']
        if 'release_date_album' in album_data:
            album.release_date_album = album_data['release_date_album']
        if 'specific_data_album' in album_data:
            album.specific_data_album = album_data['specific_data_album']
        if 'active_album' in album_data:
            album.active_album = album_data['active_album']

        return self.album_repository.save(album)

    def delete_album(self, album_id: int) -> None:
        """Elimina un álbum y sus relaciones"""
        # Eliminar relaciones
        self.album_artist_repository.delete_by_album_id(album_id)
        self.album_genre_repository.delete_by_album_id(album_id)
        self.album_rights_repository.delete_by_album_id(album_id)

        # Eliminar el álbum
        self.album_repository.delete(album_id)

    def search_albums(self, criteria: dict) -> List['Album']:
        """Busca álbumes según criterios"""
        return self.album_repository.search(criteria)

# src/main/python/com/tuempresa/ddex/domain/use_cases/artist_use_case.py
@dataclass
class ArtistUseCase:
    """Caso de uso para la gestión de artistas"""

    artist_repository: 'ArtistRepository'
    album_artist_repository: 'AlbumArtistRepository'
    track_artist_repository: 'TrackArtistRepository'

    def create_artist(self, artist_data: dict) -> 'Artist':
        """Crea un nuevo artista"""
        if not artist_data.get('name_artist'):
            raise ValueError("El nombre del artista es obligatorio")

        artist = Artist(
            name_artist=artist_data['name_artist'],
            id_parent_artist=artist_data.get('id_parent_artist'),
            specific_data_artist=artist_data.get('specific_data_artist'),
            active_artist=artist_data.get('active_artist', True)
        )

        return self.artist_repository.save(artist)

    def get_artist(self, artist_id: int) -> Optional['Artist']:
        """Obtiene un artista con sus relaciones"""
        artist = self.artist_repository.find_by_id(artist_id)
        if not artist:
            return None

        # Obtener álbumes y pistas del artista
        album_artists = self.album_artist_repository.find_by_artist_id(artist_id)
        track_artists = self.track_artist_repository.find_by_artist_id(artist_id)

        artist.albums = album_artists
        artist.tracks = track_artists

        return artist

    def update_artist(self, artist_id: int, artist_data: dict) -> 'Artist':
        """Actualiza un artista existente"""
        artist = self.get_artist(artist_id)
        if not artist:
            raise ValueError(f"Artista no encontrado con ID: {artist_id}")

        if 'name_artist' in artist_data:
            artist.name_artist = artist_data['name_artist']
        if 'id_parent_artist' in artist_data:
            artist.id_parent_artist = artist_data['id_parent_artist']
        if 'specific_data_artist' in artist_data:
            artist.specific_data_artist = artist_data['specific_data_artist']
        if 'active_artist' in artist_data:
            artist.active_artist = artist_data['active_artist']

        return self.artist_repository.save(artist)

    def delete_artist(self, artist_id: int) -> None:
        """Elimina un artista y sus relaciones"""
        self.album_artist_repository.delete_by_artist_id(artist_id)
        self.track_artist_repository.delete_by_artist_id(artist_id)
        self.artist_repository.delete(artist_id)

    def search_artists(self, criteria: dict) -> List['Artist']:
        """Busca artistas según criterios"""
        return self.artist_repository.search(criteria)


# src/main/python/com/tuempresa/ddex/domain/use_cases/track_use_case.py
@dataclass
class TrackUseCase:
    """Caso de uso para la gestión de pistas"""

    track_repository: 'TrackRepository'
    album_track_repository: 'AlbumTrackRepository'
    track_artist_repository: 'TrackArtistRepository'
    track_contributor_repository: 'TrackContributorRepository'

    def create_track(self, track_data: dict) -> 'Track':
        """Crea una nueva pista"""
        if not track_data.get('name_track'):
            raise ValueError("El nombre de la pista es obligatorio")

        track = Track(
            name_track=track_data['name_track'],
            isrc_track=track_data.get('isrc_track'),
            version_track=track_data.get('version_track'),
            length_track=track_data.get('length_track'),
            explicit_track=track_data.get('explicit_track'),
            specific_data_track=track_data.get('specific_data_track'),
            active_track=track_data.get('active_track', True)
        )

        return self.track_repository.save(track)

    def get_track(self, track_id: int) -> Optional['Track']:
        """Obtiene una pista con sus relaciones"""
        track = self.track_repository.find_by_id(track_id)
        if not track:
            return None

        # Obtener álbumes y colaboradores de la pista
        album_tracks = self.album_track_repository.find_by_track_id(track_id)
        track_contributors = self.track_contributor_repository.find_by_track_id(track_id)

        track.albums = album_tracks
        track.contributors = track_contributors

        return track

    def update_track(self, track_id: int, track_data: dict) -> 'Track':
        """Actualiza una pista existente"""
        track = self.get_track(track_id)
        if not track:
            raise ValueError(f"Pista no encontrada con ID: {track_id}")

        if 'name_track' in track_data:
            track.name_track = track_data['name_track']
        if 'isrc_track' in track_data:
            track.isrc_track = track_data['isrc_track']
        if 'version_track' in track_data:
            track.version_track = track_data['version_track']
        if 'length_track' in track_data:
            track.length_track = track_data['length_track']
        if 'explicit_track' in track_data:
            track.explicit_track = track_data['explicit_track']
        if 'specific_data_track' in track_data:
            track.specific_data_track = track_data['specific_data_track']
        if 'active_track' in track_data:
            track.active_track = track_data['active_track']

        return self.track_repository.save(track)

    def delete_track(self, track_id: int) -> None:
        """Elimina una pista y sus relaciones"""
        self.album_track_repository.delete_by_track_id(track_id)
        self.track_artist_repository.delete_by_track_id(track_id)
        self.track_contributor_repository.delete_by_track_id(track_id)
        self.track_repository.delete(track_id)

    def search_tracks(self, criteria: dict) -> List['Track']:
        """Busca pistas según criterios"""
        return self.track_repository.search(criteria)


# src/main/python/com/tuempresa/ddex/domain/use_cases/album_artist_use_case.py
@dataclass
class AlbumArtistUseCase:
    """Caso de uso para la gestión de relaciones álbum-artista"""

    album_artist_repository: 'AlbumArtistRepository'

    def create_album_artist(self, album_artist_data: dict) -> 'AlbumArtist':
        """Crea una nueva relación álbum-artista"""
        if not album_artist_data.get('id_album') or not album_artist_data.get('id_artist'):
            raise ValueError("Se requieren el ID del álbum y del artista")

        album_artist = AlbumArtist(
            id_album=album_artist_data['id_album'],
            id_artist=album_artist_data['id_artist'],
            artist_role_album_artist=album_artist_data.get('role'),
            active_album_artist=album_artist_data.get('active', True)
        )

        return self.album_artist_repository.save(album_artist)

    def get_album_artists(self, album_id: int) -> List['AlbumArtist']:
        """Obtiene todos los artistas de un álbum"""
        return self.album_artist_repository.find_by_album_id(album_id)

    def update_album_artist(self, album_artist_id: int, album_artist_data: dict) -> 'AlbumArtist':
        """Actualiza una relación álbum-artista"""
        album_artist = self.album_artist_repository.find_by_id(album_artist_id)
        if not album_artist:
            raise ValueError(f"Relación álbum-artista no encontrada con ID: {album_artist_id}")

        if 'role' in album_artist_data:
            album_artist.artist_role_album_artist = album_artist_data['role']
        if 'active' in album_artist_data:
            album_artist.active_album_artist = album_artist_data['active']

        return self.album_artist_repository.save(album_artist)

    def delete_album_artist(self, album_artist_id: int) -> None:
        """Elimina una relación álbum-artista"""
        self.album_artist_repository.delete(album_artist_id)


# src/main/python/com/tuempresa/ddex/domain/use_cases/album_genre_use_case.py
@dataclass
class AlbumGenreUseCase:
    """Caso de uso para la gestión de relaciones álbum-género"""

    album_genre_repository: 'AlbumGenreRepository'

    def create_album_genre(self, album_genre_data: dict) -> 'AlbumGenre':
        """Crea una nueva relación álbum-género"""
        if not album_genre_data.get('id_album') or not album_genre_data.get('id_genre'):
            raise ValueError("Se requieren el ID del álbum y del género")

        album_genre = AlbumGenre(
            id_album=album_genre_data['id_album'],
            id_genre=album_genre_data['id_genre']
        )

        return self.album_genre_repository.save(album_genre)

    def get_album_genres(self, album_id: int) -> List['AlbumGenre']:
        """Obtiene todos los géneros de un álbum"""
        return self.album_genre_repository.find_by_album_id(album_id)

    def delete_album_genre(self, album_genre_id: int) -> None:
        """Elimina una relación álbum-género"""
        self.album_genre_repository.delete(album_genre_id)


# src/main/python/com/tuempresa/ddex/domain/use_cases/album_rights_use_case.py
@dataclass
class AlbumRightsUseCase:
    """Caso de uso para la gestión de derechos de álbumes"""

    album_rights_repository: 'AlbumRightsRepository'

    def create_album_rights(self, rights_data: dict) -> 'AlbumRights':
        """Crea nuevos derechos de álbum"""
        if not rights_data.get('id_album'):
            raise ValueError("Se requiere el ID del álbum")

        album_rights = AlbumRights(
            id_album=rights_data['id_album'],
            id_dist=rights_data.get('id_dist'),
            id_label=rights_data.get('id_label'),
            id_cmt=rights_data.get('id_cmt'),
            id_use_type=rights_data.get('id_use_type'),
            cnty_ids_albright=rights_data.get('countries'),
            start_date_albright=rights_data.get('start_date'),
            end_date_albright=rights_data.get('end_date')
        )

        return self.album_rights_repository.save(album_rights)

    def get_album_rights(self, album_id: int) -> List['AlbumRights']:
        """Obtiene todos los derechos de un álbum"""
        return self.album_rights_repository.find_by_album_id(album_id)

    def update_album_rights(self, rights_id: int, rights_data: dict) -> 'AlbumRights':
        """Actualiza derechos de álbum"""
        rights = self.album_rights_repository.find_by_id(rights_id)
        if not rights:
            raise ValueError(f"Derechos no encontrados con ID: {rights_id}")

        if 'id_dist' in rights_data:
            rights.id_dist = rights_data['id_dist']
        if 'id_label' in rights_data:
            rights.id_label = rights_data['id_label']
        if 'id_cmt' in rights_data:
            rights.id_cmt = rights_data['id_cmt']
        if 'id_use_type' in rights_data:
            rights.id_use_type = rights_data['id_use_type']
        if 'countries' in rights_data:
            rights.cnty_ids_albright = rights_data['countries']
        if 'start_date' in rights_data:
            rights.start_date_albright = rights_data['start_date']
        if 'end_date' in rights_data:
            rights.end_date_albright = rights_data['end_date']

        return self.album_rights_repository.save(rights)

    def delete_album_rights(self, rights_id: int) -> None:
        """Elimina derechos de álbum"""
        self.album_rights_repository.delete(rights_id)


# src/main/python/com/tuempresa/ddex/domain/use_cases/album_track_use_case.py
@dataclass
class AlbumTrackUseCase:
    """Caso de uso para la gestión de relaciones álbum-pista"""

    album_track_repository: 'AlbumTrackRepository'
    album_track_rights_repository: 'AlbumTrackRightsRepository'

    def create_album_track(self, album_track_data: dict) -> 'AlbumTrack':
        """Crea una nueva relación álbum-pista"""
        if not album_track_data.get('id_album') or not album_track_data.get('id_track'):
            raise ValueError("Se requieren el ID del álbum y de la pista")

        album_track = AlbumTrack(
            id_album=album_track_data['id_album'],
            id_track=album_track_data['id_track'],
            volume_album_track=album_track_data.get('volume'),
            number_album_track=album_track_data.get('number')
        )

        # Crear derechos de la pista si se proporcionan
        if 'rights' in album_track_data:
            album_track_rights = AlbumTrackRights(
                id_album_track=album_track.id_album_track,
                id_dist=album_track_data['rights'].get('distributor_id'),
                id_label=album_track_data['rights'].get('label_id'),
                id_cmt=album_track_data['rights'].get('cmt_id'),
                id_use_type=album_track_data['rights'].get('use_type_id'),
                cnty_ids_albtraright=album_track_data['rights'].get('countries'),
                start_date_albtraright=album_track_data['rights'].get('start_date'),
                end_date_albtraright=album_track_data['rights'].get('end_date'),
                pline_text_albtraright=album_track_data['rights'].get('pline_text'),
                pline_year_albtraright=album_track_data['rights'].get('pline_year')
            )
            self.album_track_rights_repository.save(album_track_rights)

        return self.album_track_repository.save(album_track)

    def get_album_tracks(self, album_id: int) -> List['AlbumTrack']:
        """Obtiene todas las pistas de un álbum"""
        return self.album_track_repository.find_by_album_id(album_id)

    def update_album_track(self, album_track_id: int, album_track_data: dict) -> 'AlbumTrack':
        """Actualiza una relación álbum-pista"""
        album_track = self.album_track_repository.find_by_id(album_track_id)
        if not album_track:
            raise ValueError(f"Relación álbum-pista no encontrada con ID: {album_track_id}")

        if 'volume' in album_track_data:
            album_track.volume_album_track = album_track_data['volume']
        if 'number' in album_track_data:
            album_track.number_album_track = album_track_data['number']

        return self.album_track_repository.save(album_track)

    def delete_album_track(self, album_track_id: int) -> None:
        """Elimina una relación álbum-pista y sus derechos"""
        self.album_track_rights_repository.delete_by_album_track_id(album_track_id)
        self.album_track_repository.delete(album_track_id)


# src/main/python/com/tuempresa/ddex/domain/use_cases/genre_use_case.py
@dataclass
class GenreUseCase:
    """Caso de uso para la gestión de géneros"""

    genre_repository: 'GenreRepository'

    def create_genre(self, genre_data: dict) -> 'Genre':
        """Crea un nuevo género"""
        if not genre_data.get('name_genre'):
            raise ValueError("El nombre del género es obligatorio")

        genre = Genre(
            name_genre=genre_data['name_genre'],
            active_genre=genre_data.get('active', True)
        )

        return self.genre_repository.save(genre)

    def get_genre(self, genre_id: int) -> Optional['Genre']:
        """Obtiene un género"""
        return self.genre_repository.find_by_id(genre_id)

    def update_genre(self, genre_id: int, genre_data: dict) -> 'Genre':
        """Actualiza un género existente"""
        genre = self.get_genre(genre_id)
        if not genre:
            raise ValueError(f"Género no encontrado con ID: {genre_id}")

        if 'name_genre' in genre_data:
            genre.name_genre = genre_data['name_genre']
        if 'active' in genre_data:
            genre.active_genre = genre_data['active']

        return self.genre_repository.save(genre)

    def delete_genre(self, genre_id: int) -> None:
        """Elimina un género"""
        self.genre_repository.delete(genre_id)

    def search_genres(self, criteria: dict) -> List['Genre']:
        """Busca géneros según criterios"""
        return self.genre_repository.search(criteria)


# src/main/python/com/tuempresa/ddex/domain/use_cases/label_use_case.py
@dataclass
class LabelUseCase:
    """Caso de uso para la gestión de sellos discográficos"""

    label_repository: 'LabelRepository'

    def create_label(self, label_data: dict) -> 'Label':
        """Crea un nuevo sello discográfico"""
        if not label_data.get('name_label'):
            raise ValueError("El nombre del sello es obligatorio")

        label = Label(
            name_label=label_data['name_label'],
            active_label=label_data.get('active', True)
        )

        return self.label_repository.save(label)

    def get_label(self, label_id: int) -> Optional['Label']:
        """Obtiene un sello discográfico"""
        return self.label_repository.find_by_id(label_id)

    def update_label(self, label_id: int, label_data: dict) -> 'Label':
        """Actualiza un sello discográfico existente"""
        label = self.get_label(label_id)
        if not label:
            raise ValueError(f"Sello no encontrado con ID: {label_id}")

        if 'name_label' in label_data:
            label.name_label = label_data['name_label']
        if 'active' in label_data:
            label.active_label = label_data['active']

        return self.label_repository.save(label)

    def delete_label(self, label_id: int) -> None:
        """Elimina un sello discográfico"""
        self.label_repository.delete(label_id)

    def search_labels(self, criteria: dict) -> List['Label']:
        """Busca sellos discográficos según criterios"""
        return self.label_repository.search(criteria)


# src/main/python/com/tuempresa/ddex/domain/use_cases/contributor_use_case.py
@dataclass
class ContributorUseCase:
    """Caso de uso para la gestión de colaboradores"""

    contributor_repository: 'ContributorRepository'
    track_contributor_repository: 'TrackContributorRepository'

    def create_contributor(self, contributor_data: dict) -> 'Contributor':
        """Crea un nuevo colaborador"""
        if not contributor_data.get('name_contri'):
            raise ValueError("El nombre del colaborador es obligatorio")

        contributor = Contributor(
            name_contri=contributor_data['name_contri'],
            active_contri=contributor_data.get('active', True)
        )

        return self.contributor_repository.save(contributor)

    def get_contributor(self, contributor_id: int) -> Optional['Contributor']:
        """Obtiene un colaborador con sus contribuciones"""
        contributor = self.contributor_repository.find_by_id(contributor_id)
        if not contributor:
            return None

        contributor.tracks = self.track_contributor_repository.find_by_contributor_id(contributor_id)
        return contributor

    def update_contributor(self, contributor_id: int, contributor_data: dict) -> 'Contributor':
        """Actualiza un colaborador existente"""
        contributor = self.get_contributor(contributor_id)
        if not contributor:
            raise ValueError(f"Colaborador no encontrado con ID: {contributor_id}")

        if 'name_contri' in contributor_data:
            contributor.name_contri = contributor_data['name_contri']
        if 'active' in contributor_data:
            contributor.active_contri = contributor_data['active']

        return self.contributor_repository.save(contributor)

    def delete_contributor(self, contributor_id: int) -> None:
        """Elimina un colaborador y sus contribuciones"""
        self.track_contributor_repository.delete_by_contributor_id(contributor_id)
        self.contributor_repository.delete(contributor_id)

    def search_contributors(self, criteria: dict) -> List['Contributor']:
        """Busca colaboradores según criterios"""
        return self.contributor_repository.search(criteria)


# src/main/python/com/tuempresa/ddex/domain/use_cases/track_contributor_use_case.py
@dataclass
class TrackContributorUseCase:
    """Caso de uso para la gestión de relaciones pista-colaborador"""

    track_contributor_repository: 'TrackContributorRepository'

    def create_track_contributor(self, track_contributor_data: dict) -> 'TrackContributor':
        """Crea una nueva relación pista-colaborador"""
        if not track_contributor_data.get('id_track') or not track_contributor_data.get('id_contri'):
            raise ValueError("Se requieren el ID de la pista y del colaborador")

        track_contributor = TrackContributor(
            id_track=track_contributor_data['id_track'],
            id_contri=track_contributor_data['id_contri'],
            contributor_role_track_contri=track_contributor_data.get('role'),
            contributor_role_type_track_contri=track_contributor_data.get('role_type')
        )

        return self.track_contributor_repository.save(track_contributor)

    def get_track_contributors(self, track_id: int) -> List['TrackContributor']:
        """Obtiene todos los colaboradores de una pista"""
        return self.track_contributor_repository.find_by_track_id(track_id)

    def update_track_contributor(self, track_contributor_id: int, track_contributor_data: dict) -> 'TrackContributor':
        """Actualiza una relación pista-colaborador"""
        track_contributor = self.track_contributor_repository.find_by_id(track_contributor_id)
        if not track_contributor:
            raise ValueError(f"Relación pista-colaborador no encontrada con ID: {track_contributor_id}")

        if 'role' in track_contributor_data:
            track_contributor.contributor_role_track_contri = track_contributor_data['role']
        if 'role_type' in track_contributor_data:
            track_contributor.contributor_role_type_track_contri = track_contributor_data['role_type']

        return self.track_contributor_repository.save(track_contributor)

    def delete_track_contributor(self, track_contributor_id: int) -> None:
        """Elimina una relación pista-colaborador"""
        self.track_contributor_repository.delete(track_contributor_id)


# src/main/python/com/tuempresa/ddex/domain/use_cases/use_type_use_case.py
@dataclass
class UseTypeUseCase:
    """Caso de uso para la gestión de tipos de uso"""

    use_type_repository: 'UseTypeRepository'

    def create_use_type(self, use_type_data: dict) -> 'UseType':
        """Crea un nuevo tipo de uso"""
        if not use_type_data.get('name_use_type'):
            raise ValueError("El nombre del tipo de uso es obligatorio")

        use_type = UseType(
            name_use_type=use_type_data['name_use_type'],
            description_use_type=use_type_data.get('description'),
            update_id_message=use_type_data.get('update_id_message'),
            insert_id_message=use_type_data.get('insert_id_message')
        )

        return self.use_type_repository.save(use_type)

    def get_use_type(self, use_type_id: int) -> Optional['UseType']:
        """Obtiene un tipo de uso"""
        return self.use_type_repository.find_by_id(use_type_id)

    def update_use_type(self, use_type_id: int, use_type_data: dict) -> 'UseType':
        """Actualiza un tipo de uso existente"""
        use_type = self.get_use_type(use_type_id)
        if not use_type:
            raise ValueError(f"Tipo de uso no encontrado con ID: {use_type_id}")

        if 'name_use_type' in use_type_data:
            use_type.name_use_type = use_type_data['name_use_type']
        if 'description' in use_type_data:
            use_type.description_use_type = use_type_data['description']

        return self.use_type_repository.save(use_type)

    def delete_use_type(self, use_type_id: int) -> None:
        """Elimina un tipo de uso"""
        self.use_type_repository.delete(use_type_id)

    def search_use_types(self, criteria: dict) -> List['UseType']:
        """Busca tipos de uso según criterios"""
        return self.use_type_repository.search(criteria)
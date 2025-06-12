# src/domain/album/repositories/album_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.album import Album


class IAlbumRepository(ABC):
    """Interfaz del repositorio de Album"""

    @abstractmethod
    async def get_album(self, album_id: str) -> Optional[Album]:
        """Obtiene un álbum por su ID"""
        pass

    @abstractmethod
    async def get_all_albums(self) -> List[Album]:
        """Obtiene todos los álbumes"""
        pass

    @abstractmethod
    async def create_album(self, album: Album) -> Album:
        """Crea un nuevo álbum"""
        pass

    @abstractmethod
    async def update_album(self, album: Album) -> Album:
        """Actualiza un álbum existente"""
        pass

    @abstractmethod
    async def delete_album(self, album_id: str) -> None:
        """Elimina un álbum"""
        pass
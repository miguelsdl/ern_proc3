# src3/domain/album/tests/test_album_repository.py

import pytest
from unittest.mock import Mock
from domain.album.entity import Album
from domain.album.repositories.album_repository import IAlbumRepository


class TestAlbumRepository:
    """Pruebas del repositorio de Album"""

    def test_get_album(self):
        # Arrange
        album_id = "1"
        mock_album = Mock()
        repository = Mock(spec=IAlbumRepository)
        repository.get_album.return_value = mock_album

        # Act
        result = repository.get_album(album_id)

        # Assert
        assert result == mock_album
        repository.get_album.assert_called_once_with(album_id)

    def test_create_album(self):
        # Arrange
        album = Album(
            id="1",
            title="Test Album",
            artist="Test Artist"
        )
        repository = Mock(spec=IAlbumRepository)
        repository.create_album.return_value = album

        # Act
        result = repository.create_album(album)

        # Assert
        assert result == album
        repository.create_album.assert_called_once_with(album)
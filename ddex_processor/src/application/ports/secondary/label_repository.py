from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.label import Label


class LabelRepository(ABC):
    """Interfaz para operaciones de repositorio de etiquetas"""

    @abstractmethod
    def get(self, label_id: int) -> Optional[Label]:
        """Obtener etiqueta por ID"""
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Label]:
        """Buscar etiqueta por nombre"""
        pass

    @abstractmethod
    def list_all(self) -> List[Label]:
        """Listar todas las etiquetas"""
        pass

    @abstractmethod
    def save(self, label: Label) -> Label:
        """Guardar etiqueta"""
        pass

    @abstractmethod
    def delete(self, label_id: int) -> None:
        """Eliminar etiqueta"""
        pass
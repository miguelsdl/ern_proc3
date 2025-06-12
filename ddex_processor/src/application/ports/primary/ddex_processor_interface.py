from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.label import Label


class DDexProcessorInterface(ABC):
    """Interfaz principal para procesamiento de etiquetas DDex"""

    @abstractmethod
    async def get_labels(self) -> List[Label]:
        """Obtener lista de etiquetas"""
        pass

    @abstractmethod
    async def get_label_by_name(self, name: str) -> Optional[Label]:
        """Buscar etiqueta por nombre"""
        pass

    @abstractmethod
    async def create_label(self, label: Label) -> Label:
        """Crear nueva etiqueta"""
        pass

    @abstractmethod
    async def update_label(self, label: Label) -> Label:
        """Actualizar etiqueta existente"""
        pass

    @abstractmethod
    async def delete_label(self, label_id: int) -> None:
        """Eliminar etiqueta"""
        pass

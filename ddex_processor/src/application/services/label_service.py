from typing import List, Optional
from src.domain.entities.label import Label
from src.application.ports.secondary.label_repository import LabelRepository
from src.application.ports.primary.ddex_processor_interface import DDexProcessorInterface


class LabelService(DDexProcessorInterface):
    """Servicio de aplicación para manejo de etiquetas"""

    def __init__(self, repository: LabelRepository):
        self.repository = repository

    async def get_labels(self) -> List[Label]:
        """Implementación de obtener etiquetas"""
        return self.repository.list_all()

    async def get_label_by_name(self, name: str) -> Optional[Label]:
        """Implementación de buscar etiqueta por nombre"""
        return self.repository.get_by_name(name)

    async def create_label(self, label: Label) -> Label:
        """Implementación de crear etiqueta"""
        return self.repository.save(label)

    async def update_label(self, label: Label) -> Label:
        """Implementación de actualizar etiqueta"""
        return self.repository.save(label)

    async def delete_label(self, label_id: int) -> None:
        """Implementación de eliminar etiqueta"""
        self.repository.delete(label_id)

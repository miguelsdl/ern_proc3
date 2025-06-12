from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Label:
    """Entidad de dominio para representar una etiqueta"""
    id_label: Optional[int] = None
    name_label: str = ""
    active_label: bool = True
    audi_edited_label: Optional[datetime] = None
    audi_created_label: Optional[datetime] = None
    update_id_message: int = 0
    insert_id_message: int = 0

    def __eq__(self, other):
        """Comparación basada en el ID"""
        return isinstance(other, Label) and self.id_label == other.id_label

    @classmethod
    def create(cls, name: str, active: bool = True) -> 'Label':
        """Crear una nueva etiqueta"""
        return cls(
            name_label=name,
            active_label=active
        )

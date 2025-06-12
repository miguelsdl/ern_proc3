from sqlalchemy.orm import Session
from typing import List, Optional
from src.domain.entities.label import Label
from src.application.ports.secondary.label_repository import LabelRepository
from src.infrastructure.adapters.database.models.label import LabelModel


class MySQLLabelRepository(LabelRepository):
    """Implementación del repositorio usando MySQL"""

    def __init__(self, session: Session):
        self.session = session

    def get(self, label_id: int) -> Optional[Label]:
        """Obtener etiqueta por ID"""
        model = self.session.query(LabelModel).filter_by(id_label=label_id).first()
        return self._map_model_to_entity(model) if model else None

    def get_by_name(self, name: str) -> Optional[Label]:
        """Buscar etiqueta por nombre"""
        model = self.session.query(LabelModel).filter_by(name_label=name).first()
        return self._map_model_to_entity(model) if model else None

    def list_all(self) -> List[Label]:
        """Listar todas las etiquetas"""
        models = self.session.query(LabelModel).all()
        return [self._map_model_to_entity(model) for model in models]

    def save(self, label: Label) -> Label:
        """Guardar etiqueta"""
        model = self._map_entity_to_model(label)
        self.session.add(model)
        self.session.commit()
        return self._map_model_to_entity(model)

    def delete(self, label_id: int) -> None:
        """Eliminar etiqueta"""
        model = self.session.query(LabelModel).filter_by(id_label=label_id).first()
        if model:
            self.session.delete(model)
            self.session.commit()

    def _map_model_to_entity(self, model: Optional[LabelModel]) -> Optional[Label]:
        """Convertir modelo a entidad"""
        if not model:
            return None
        return Label(
            id_label=model.id_label,
            name_label=model.name_label,
            active_label=bool(model.active_label),
            audi_edited_label=model.audi_edited_label,
            audi_created_label=model.audi_created_label,
            update_id_message=model.update_id_message,
            insert_id_message=model.insert_id_message
        )

    def _map_entity_to_model(self, entity: Label) -> LabelModel:
        """Convertir entidad a modelo"""
        model = LabelModel()
        model.id_label = entity.id_label
        model.name_label = entity.name_label
        model.active_label = int(entity.active_label)
        model.audi_edited_label = entity.audi_edited_label
        model.audi_created_label = entity.audi_created_label
        model.update_id_message = entity.update_id_message
        model.insert_id_message = entity.insert_id_message
        return model

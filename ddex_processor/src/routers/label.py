from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ddex_processor.src.application.services.label_service import LabelService
from ddex_processor.src.infrastructure.adapters.database.mysql_label_repository import MySQLLabelRepository
from ddex_processor.src.infrastructure.adapters.database.session import get_db
from ddex_processor.src.domain.entities.label import Label

router = APIRouter(prefix="/labels")


def get_label_service(db: Session = Depends(get_db)):
    """Obtener instancia del servicio de etiquetas"""
    repository = MySQLLabelRepository(db)
    return LabelService(repository)


@router.get("/", response_model=List[Label])
async def read_labels(service: LabelService = Depends(get_label_service)):
    """Endpoint para listar todas las etiquetas"""
    return await service.get_labels()


@router.post("/", response_model=Label)
async def create_label(
        label_data: Label,
        service: LabelService = Depends(get_label_service)
):
    """Endpoint para crear una nueva etiqueta"""
    return await service.create_label(label_data)


@router.get("/{label_id}", response_model=Label)
async def read_label(
        label_id: int,
        service: LabelService = Depends(get_label_service)
):
    """Endpoint para obtener una etiqueta específica"""
    db_label = await service.get_label_by_name(f"label_{label_id}")
    if db_label is None:
        raise HTTPException(status_code=404, detail="Etiqueta no encontrada")
    return db_label


@router.put("/{label_id}", response_model=Label)
async def update_label(
        label_id: int,
        label_data: Label,
        service: LabelService = Depends(get_label_service)
):
    """Endpoint para actualizar una etiqueta"""
    db_label = await service.get_label_by_name(f"label_{label_id}")
    if db_label is None:
        raise HTTPException(status_code=404, detail="Etiqueta no encontrada")

    # Actualizar datos
    db_label.name_label = label_data.name_label
    db_label.active_label = label_data.active_label

    return await service.update_label(db_label)


@router.delete("/{label_id}")
async def delete_label(
        label_id: int,
        service: LabelService = Depends(get_label_service)
):
    """Endpoint para eliminar una etiqueta"""
    await service.delete_label(label_id)
    return {"message": f"Etiqueta {label_id} eliminada"}

# src/infrastructure/adapters/database/models/label.py
import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LabelModel(Base):
    """Modelo de SQLAlchemy para la tabla de etiquetas"""
    __tablename__ = 'feed.labels'

    # Campos principales
    id_label = Column(Integer, primary_key=True, autoincrement=True)
    name_label = Column(String(50), nullable=True, unique=True)
    active_label = Column(Boolean, nullable=True)

    # Campos de auditoría
    audi_edited_label = Column(TIMESTAMP, nullable=True)
    audi_created_label = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.datetime.utcnow,
        server_default='CURRENT_TIMESTAMP'
    )

    # IDs de mensajes
    update_id_message = Column(Integer, nullable=False, default=0)
    insert_id_message = Column(Integer, nullable=False, default=0)

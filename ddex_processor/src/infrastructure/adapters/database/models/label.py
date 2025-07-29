# src/infrastructure/adapters/database/models/label.py
import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class LabelModel(Base):
    """Modelo de SQLAlchemy para la tabla de etiquetas"""
    __tablename__ = 'pruebas.labels'

    # Campos principales
    id_label = Column(Integer, primary_key=True, autoincrement=True)
    name_label = Column(String(50), nullable=True, unique=True)
    active_label = Column(Boolean, nullable=True)

    # # Campos de auditoría
    # audi_edited_label = Column(TIMESTAMP, nullable=True)
    # audi_created_label = Column(
    #     TIMESTAMP,
    #     nullable=False,
    #     default=datetime.datetime.utcnow,
    #     server_default='CURRENT_TIMESTAMP'
    # )
    #
    # # IDs de mensajes
    # update_id_message = Column(Integer, nullable=False, default=0)
    # insert_id_message = Column(Integer, nullable=False, default=0)

    foo_id = Column(Integer, ForeignKey('pruebas.foo.id_foo'), nullable=True)
    foo = relationship("FooModel", back_populates="labels")


class FooModel(Base):
    """Modelo de SQLAlchemy para la tabla de etiquetas"""
    __tablename__ = 'pruebas.foo'

    # Campos principales
    id_foo = Column(Integer, primary_key=True, autoincrement=True)
    name_foo = Column(String(50), nullable=True, unique=True)
    labels = relationship("LabelModel", back_populates="foo")

# test_models.py
# db_setup.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base

# At the bottom, create the engine and create tables:
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:@localhost/pruebas"  # Update as needed
engine = create_engine(DATABASE_URL, echo=True)
# Base.metadata.create_all(engine)



SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()

# new_foo = FooModel(name_foo="Example Foo")
# session.add(new_foo)
# session.commit()
# session.close()


new_label = LabelModel(name_label="Example Label", active_label=True)

def get_or_create_label(session, name_label, active_label=True):
    instance = session.query(LabelModel).filter_by(name_label=name_label).first()
    if instance:
        return instance, False
    else:
        instance = LabelModel(name_label=name_label, active_label=active_label)
        session.add(instance)
        session.commit()
        return instance, True

label, created = get_or_create_label(session, "Example Label", True)
print(f"ID for label: {label.id_label}, created: {created}")
session.close()

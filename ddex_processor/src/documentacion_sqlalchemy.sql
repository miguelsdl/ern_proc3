from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TablaA(Base):
    __tablename__ = 'tabla_a'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    # Definimos la relación usando PrimaryJoin
    tabla_b = relationship(
        "TablaB",
        primaryjoin="TablaA.id == TablaB.tabla_a_id",
        back_populates="tabla_a"
    )

class TablaB(Base):
    __tablename__ = 'tabla_b'
    id = Column(Integer, primary_key=True)
    tabla_a_id = Column(Integer)  # Columna que actúa como foreign key
    nombre = Column(String)

    # Definimos el backref
    tabla_a = relationship(
        "TablaA",
        back_populates="tabla_b"
    )

-- Pros
--
-- No requiere modificar la estructura física de la base de datos
-- Mantiene la integridad referencial a nivel de aplicación
-- Fácil de implementar y mantener
--
--     Permite definir la relación de manera explícita
--
-- Cons
--
-- No hay restricciones en la base de datos
-- Requiere más cuidado para mantener la consistencia
-- Puede ser menos eficiente en consultas complejas


from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class TablaA(Base):
    __tablename__ = 'tabla_a'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    tabla_b = relationship(
        "TablaB",
        secondary="tabla_a_tabla_b",
        back_populates="tabla_a"
    )

class TablaB(Base):
    __tablename__ = 'tabla_b'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    tabla_a = relationship(
        "TablaA",
        secondary="tabla_a_tabla_b",
        back_populates="tabla_b"
    )

# Tabla intermedia
tabla_a_tabla_b = Table('tabla_a_tabla_b', Base.metadata,
    Column('tabla_a_id', Integer, ForeignKey('tabla_a.id')),
    Column('tabla_b_id', Integer, ForeignKey('tabla_b.id'))
)

-- Pros
--
-- Permite relaciones muchos a muchos
-- Mantiene la flexibilidad de la relación
--
--     Útil cuando necesitas datos adicionales en la relación
--
-- Cons
--
-- Requiere una tabla intermedia
-- Más complejo de mantener
-- Puede ser excesivo para una relación uno a muchos simple
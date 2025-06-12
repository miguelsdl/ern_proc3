# ddex_processor/src/infrastructure/adapters/database/session.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
import os

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+asyncmy://usuario:contraseña@localhost/nombre_base_datos")

# Crear el engine de la base de datos
engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)

# Crear una factoría de sesiones
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)


async def get_db() -> Generator:
    """Función para obtener una sesión de base de datos

    Esta función es un generador que proporciona una sesión de base de datos
    y se asegura de cerrarla automáticamente cuando ya no se necesita.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
import os
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from ddex_processor.src.routers.label import router


# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+asyncmy://user:password@localhost/dbname")

# Crear engine y session maker
engine = create_async_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Crear aplicación FastAPI
app = FastAPI()

# Registrar routers
app.include_router(router)

@app.on_event("shutdown")
async def shutdown_event():
    """Cerrar conexiones cuando la aplicación termine"""
    await engine.dispose()

async def get_db():
    """Obtener una sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
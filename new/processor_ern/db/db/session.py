from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ⚠️ Cambiá esto a tu URI real si usás Postgres, MySQL, etc.
DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/pruebas_feed2"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
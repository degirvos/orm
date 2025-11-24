# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos PostgreSQL
DATABASE_URL = "postgresql://orm:orm@localhost:5432/practica_orm"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)

# Base para los modelos
Base = declarative_base()

# Función para obtener sesión
def obtener_sesion():
    Session = sessionmaker(bind=engine)
    return Session()

# Función para crear tablas
def crear_tablas():
    Base.metadata.create_all(engine)
    print("✅ Tablas verificadas/creadas correctamente")

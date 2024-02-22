from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
# Obtener la ruta completa al archivo SQLite en la misma carpeta que el script principal
sqlite_path = 'sqlite:///{}'.format('database.db')
# Creamos una instancia del motor de la base de datos (SQLite en este caso)
engine = create_engine(sqlite_path, echo=True)

# Creamos la instancia de la base de datos
Base = declarative_base()



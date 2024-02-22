from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from clases.base import Base
estadosBD = []

class Estado(Base):
    __tablename__ = 'estados'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cambiosDeEstado = relationship("CambioEstado", back_populates="estado")
    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def esFinalizada(self):
        if self.nombre == "Finalizada":
            return True
        else:
            return False

    def esIniciada(self):
        #retorna true si el estado tiene como nombre iniciada
        if self.nombre == "Iniciada":
            return True
        else:
            return False
    def __str__(self):
        return self.nombre

    

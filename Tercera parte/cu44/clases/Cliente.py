from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from clases.base import Base
clientesBD = []

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    dni = Column(Integer)
    nombreCompleto = Column(String)
    nroCelular = Column(Integer)
    
    llamadas = relationship("Llamada", back_populates="cliente")
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

    def getNombre(self):
        # retorna el nombre del cliente
        return self.nombreCompleto
    def __str__(self):
        return self.nombreCompleto
    


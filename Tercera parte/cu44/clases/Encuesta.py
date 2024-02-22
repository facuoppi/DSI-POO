from clases.Pregunta import preguntasBD
from sqlalchemy import Column, Integer, String, ForeignKey,Date,DateTime
from sqlalchemy.orm import relationship, Mapped
from clases.base import Base
encuestasBD = []
class Encuesta(Base):
    __tablename__ = 'encuestas'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    fechaFinVigencia = Column(DateTime)
    preguntas = relationship("Pregunta", back_populates="encuesta", cascade="all, delete-orphan")

    llamadas = relationship("Llamada", back_populates="encuestaEnviada")
    def __init__(self, fechaFinVigencia, descripcion, preguntas):
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia
        self.preguntas = preguntas 

    def agregarPreguntas(self, unPregunta):
        self.preguntas.append(unPregunta)

    def getDescripcionEncuesta(self):
        return self.descripcion
    def esDeEncuesta(self, pregunta):
        if pregunta in self.preguntas:
            return True
        return False
    def esDeEncuestaRespuesta(self, respuestaPosible):
        # recorre la lista de preguntas de la encuesta y verifica que la pregunta sea de la encuesta
        for unaPregunta in self.preguntas:
            if unaPregunta.esDePregunta(respuestaPosible):
                return True
            return False
    def printPreguntas(self):
        for unaPregunta in self.preguntas:
            print(unaPregunta)
    def __str__(self):
        return self.descripcion

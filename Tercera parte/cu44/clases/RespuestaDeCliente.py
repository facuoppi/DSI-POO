from clases.RespuestaPosible import respuestasPosiblesBD
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from clases.base import Base
respuestasDeClienteBD = []

class RespuestaDeCliente(Base):
    __tablename__ = 'respuestasDeCliente'
    id = Column(Integer, primary_key=True)
    fechaEncuesta = Column(String)
    respuestaSeleccionada_id = Column(Integer, ForeignKey('respuestasPosibles.id'))
    respuestaSeleccionada = relationship("RespuestaPosible", back_populates="respuestasDeCliente")
    
    llamada_id = Column(Integer, ForeignKey('llamadas.id'))
    llamada = relationship("Llamada", back_populates="respuestasDeEncuesta")

    def __init__(self, fechaEncuesta, respuestaSeleccionada):
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada
    
    def getDescripcionRta(self,listaPreguntas):
        # llama al metodo getDescripcionRta de la clase RespuestaPosible y retorna el resultado
        return self.respuestaSeleccionada.getDescripcionRta(listaPreguntas)

    def obtenerValorSeleccionado(self):
        # obtiene el valor seleccionado por el cliente
        return self.respuestaSeleccionada.getValor()
    def obtenerEncuesta(self, listaDeEncuestas, listaPreguntas):
        #recibe la lista de encuesta y se la pasa a la respuestaPosible
        return self.respuestaSeleccionada.obtenerEncuesta(listaDeEncuestas,listaPreguntas)

    def getRespuesta(self):
        return self
    def __str__(self):
        return self.getDescripcionRta()

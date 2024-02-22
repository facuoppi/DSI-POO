from clases.RespuestaPosible import respuestasPosiblesBD
respuestasDeClienteBD = []

class RespuestaDeCliente:
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

from clases.RespuestaPosible import respuestasPosiblesBD
preguntasBD = []
class Pregunta:
    def __init__(self, pregunta, respuestas):
        self.respuestas = respuestas
        self.pregunta = pregunta


    def getDescripcion(self):
        # retorna su descripcion
        return self.pregunta
    def esDePregunta(self, respuesta):
        # verifica si la respuesta recibida por parametro pertenece a la pregunta
        if respuesta in self.respuestas :
            return True
        return False

    # def obtenerEncuesta(self, listaDeEncuestas):
    #     for encuesta in listaDeEncuestas:
    #         if self in encuesta.preguntas:
    #             return encuesta.getDescripcionEncuesta()
    #     return "La pregunta no pertenece a ninguna encuesta"
    def obtenerEncuesta(self, listaDeEncuestas):
        for unaEncuesta in listaDeEncuestas:
            #por cada encuesta verifica si la pregunta actual es de la encuesta
            if unaEncuesta.esDeEncuesta(self):
                return unaEncuesta.getDescripcionEncuesta()
    def __str__(self):
        return self.pregunta

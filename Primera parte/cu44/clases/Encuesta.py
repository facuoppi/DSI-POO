from clases.Pregunta import preguntasBD
encuestasBD = []
class Encuesta:
    def __init__(self, fechaFinVigencia, descripcion, preguntas):
        self.preguntas = []
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
    def __str__(self):
        return self.descripcion

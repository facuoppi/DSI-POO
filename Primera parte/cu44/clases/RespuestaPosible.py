respuestasPosiblesBD = []
class RespuestaPosible:
    def __init__(self, descripcion, valor):
        self.descripcion = descripcion
        self.valor = valor

    def getRespuesta(self):
        return self
    def getValor(self):
        # retorna el valor de la respuesta
        return self.valor
    def getDescripcionRta(self,listaPreguntaBD):
        # retorna su descripcion
        for unaPregunta in listaPreguntaBD:
            # busca la pregunta a que pertenece esta respuesta
            if unaPregunta.esDePregunta(self):
                #retorna la descripcion de la pregunta relacionada
                return unaPregunta.getDescripcion()
    
    # def obtenerEncuesta(self, listaDeEncuestas):
    #     # recibe la lista de encuestas y se la pasa a la pregunta
    #     # recorre las encuestas y su lista de preguntas
    #     for unaEncuesta in listaDeEncuestas:
    #         for unaPregunta in unaEncuesta.preguntas:
    #             if self in unaPregunta.respuestas:
    #                 return unaPregunta.obtenerEncuesta(listaDeEncuestas)





    #         if self in unaEncuesta.preguntas:
    #             return unaEncuesta.nombre
    #     return "La pregunta no pertenece a ninguna encuesta"
    
    def obtenerEncuesta(self, listaDeEncuestas,listaPreguntas):
        for unaPregunta in listaPreguntas:
            #por cada encuesta verifica si la pregunta actual es de la encuesta
            if unaPregunta.esDePregunta(self):
                return unaPregunta.obtenerEncuesta(listaDeEncuestas)
            
    def __str__(self):
        return self.descripcion

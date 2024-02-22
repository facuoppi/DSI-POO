
from clases.CambioEstado import cambiosDeEstadoBD
from clases.Cliente import clientesBD
from clases.RespuestaDeCliente import respuestasDeClienteBD

llamadasBD = []

class Llamada:
    def __init__(self, descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, ObservacionAuditor, respuestaDeEncuesta, cambioEstado, cliente):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.ObservacionAuditor = ObservacionAuditor
        # Este es un atributo referencial (cambioEstado va a ser una lista, ya que, la relación es un o muchos (? )
        self.cambiosDeEstado = cambioEstado
        self.respuestasDeEncuesta = respuestaDeEncuesta
        self.cliente = cliente

    def agregarCambioEstado(self, unCambioDeEstado):
        self.cambiosDeEstado.append(unCambioDeEstado)
        
    def agregarRespuestaDeEncuesta(self, respuestaEncuesta):
        self.respuestasDeEncuesta.append(respuestaEncuesta)

    def esDePeriodo(self, fechaInicio, fechaFin):
        # retorna boolean si la llamada esta dentro del periodo recibido por parametro
        #bucle mientas haya cambios de estado en la llamada
        for unCambioDeEstado in self.cambiosDeEstado:
            if unCambioDeEstado.esEstadoInicial():
                # busca la fechaHoraInicio del cambio de estado iniciada
                fechaHoraInicio = unCambioDeEstado.getFechaHoraInicio()
                # verifica que el cambio de estado este en periodo
                if fechaInicio <= fechaHoraInicio and fechaHoraInicio <= fechaFin:
                    return True
        return False
    
    def tieneEncuestaRespondida(self):
        # retorna true si en la coleccion de respuestas de encuesta hay al menos una respuesta
        if len(self.respuestasDeEncuesta) > 0:
            return True


    def getDuracion(self):
        return self.duracion

    def determinarEstadoInicial(self):
        for unCambioDeEstado in self.cambiosDeEstado:
            if unCambioDeEstado.esEstadoInicial():
                return unCambioDeEstado.getFechaHoraInicio()

    def getNombreClienteLlamada(self):
        # retorna el nombre del cliente de la llamada
        return self.cliente.getNombre()
    
    def determinarUltimoEstado(self):
        # recorre la lista de cambios de estado y retorna el ultimo estado con su nombre
        cambioEstadoActual = self.cambiosDeEstado[0]
        # llama al metodo esUltimoCambioEstado de la clase CambioEstado por cada cambioEstado de la llamada
        for cambioEstado in self.cambiosDeEstado:
            cambioEstadoActual = cambioEstado.esUltimoCambioEstado(cambioEstadoActual)
        return cambioEstadoActual.getNombreEstado()
    
    def getRespuestas(self,listaPreguntas):
        # Recibe la lista de Preguntas para poder obtener la descripcion de la respuesta
        preguntas = []
        valoresSeleccionados = []
        # loop mientras tenga respuestas
        for unaRespuesta in self.respuestasDeEncuesta:
            preguntas.append(unaRespuesta.getDescripcionRta(listaPreguntas))
            valoresSeleccionados.append(unaRespuesta.obtenerValorSeleccionado())
        return preguntas, valoresSeleccionados

    def mostrarDatosLlamada(self, listaDeEncuestas,listaPreguntas):
        # retorna un diccionario con los datos de la llamada
        nombreCliente = self.getNombreClienteLlamada()
        # busca el ultimoEstado en su lista de cambios de estado
        ultimoEstado = self.determinarUltimoEstado()
        duracion = self.getDuracion()
        # llama al metodo getRespuestas para obtener las descripciones de las preguntas y valores seleccionados
        preguntas, valoresSeleccionados = self.getRespuestas(listaPreguntas)
        # llama al metodo obtenerEncuesta de la primera RespuestaDeCliente para obtener la encuesta
        encuesta = self.respuestasDeEncuesta[0].obtenerEncuesta(listaDeEncuestas,listaPreguntas)
        # retorna un diccionario para mostrarlo en la pantalla
        return {"nombreCliente": nombreCliente, 
                "ultimoEstado": ultimoEstado, 
                "duracion": duracion,
                "preguntas": preguntas, 
                "valoresSeleccionados": valoresSeleccionados,
                "encuesta":encuesta}

    def __str__(self):
        return self.descripcionOperador + " " + self.detalleAccionRequerida + " " + str(self.duracion) + " " + self.ObservacionAuditor + " " + str(self.cambiosDeEstado) +  str(self.cliente)

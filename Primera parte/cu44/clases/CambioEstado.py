from clases.Estado import estadosBD
cambiosDeEstadoBD = []


class CambioEstado:
    # El atributo estado es un objeto de la clase Estado
    def __init__(self, fechaHoraInicio, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def esEstadoInicial(self):
        # retorna true si el cambio de estado tiene en su estado el puntero a es iniciada
        if self.estado.esIniciada():
            return True
        else:
            return False

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio
    
    def getNombreEstado(self):
        # Aca le pedimos al estado el nombre ... Envio de mensajes
        return self.estado.getNombre()
    
    def obtenerEstadoActual(self):
        # Aca obtenemos el estado actual
        return self.estado
    
    def esUltimoCambioEstado(self, unCambioEstado):
        # compara dos objetos que representan cambios de estado y devuelve el objeto que representa el cambio de estado más reciente en función de su atributo fechaHoraInicio.
        if self.fechaHoraInicio > unCambioEstado.getFechaHoraInicio():
            # se retorna a el mismo si es mas reciente para luego ser comparado con los demas cambios de estado
            return self
        #retorna el cambio de estado recibido por parametro si es mas reciente para comparar con los demas cambios de estado
        return unCambioEstado
    def __str__(self):
        return str(self.fechaHoraInicio) + " " + self.estado.getNombre()

from typing import List
from clases.Iterator.IIterador import IIterador
from clases.CambioEstado import CambioEstado
iteradoresCambioEstadoBD = []
class IteratorCambioEstado(IIterador):
    actual = None
    elementos = []

    def new(self, elementos:List[CambioEstado],filtros:List[object]):
        self.elementos = elementos
        self.filtros = filtros
        return self
    def primero(self):
        if len(self.elementos) > 0:
            self.actual = 0
    def siguiente(self):
        if self.actual != None:
            #print(self.elementos[self.actual].getFechaHoraInicio())
            self.actual += 1
    def haTerminado(self):
        return self.actual == None or self.actual >= len(self.elementos)
    def elementoActual(self):
        if self.actual != None:
            return self.elementos[self.actual]
        else:
            return None
    
    def cumpleFiltro(self, filtros):
        for nombre_metodo, parametros in filtros:
            metodo = getattr(self.elementos[self.actual], nombre_metodo)
            resultado = metodo(*parametros)
            if resultado == False:
                return False
        return True

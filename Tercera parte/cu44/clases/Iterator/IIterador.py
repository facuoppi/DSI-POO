from abc import ABC
from typing import List
class IIterador(ABC):
    def primero(self):
        pass
    def siguiente(self):
        pass
    def haTerminado(self):
        return True
    def elementoActual(self):
        return object
    def cumpleFiltro(self, filtros:List[object]):
        return True

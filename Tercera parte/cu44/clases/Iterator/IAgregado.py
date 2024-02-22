from abc import ABC
from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from clases.base import Base
class IAgregado(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    def crear_iterador(self,elementos:List[object]):
        return self


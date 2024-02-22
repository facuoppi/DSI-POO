import sys

from clases.ControlConsultarEncuesta import ControladorConsultaEncuesta
from clases.pantallaConsultarEncuesta import Ui_PantallaConsultarEncuesta
from generador import GeneradorAleatorio
from PyQt5 import QtWidgets
from sqlalchemy.orm import declarative_base, Session, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
import qdarkstyle
import platform
import subprocess
import os
def main():

    #populate de los datos
    generador = GeneradorAleatorio()
    session = generador.iniciarDB()
    # iniciamos el controlador
    controlador = ControladorConsultaEncuesta()
    #opc consultar encuesta
    ui = Ui_PantallaConsultarEncuesta(controlador)
    #habiliarPatalla()
    ui.habilitarPantalla(controlador,session)
    # Creamos las tablas en la base de datos

    
if __name__ == '__main__':
    main()








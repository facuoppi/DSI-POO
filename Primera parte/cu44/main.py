import sys

from clases.ControlConsultarEncuesta import ControladorConsultaEncuesta
from clases.pantallaConsultarEncuesta import Ui_PantallaConsultarEncuesta
from generador import GeneradorAleatorio
from PyQt5 import QtWidgets


def main():
    #populate de los datos
    generador = GeneradorAleatorio()
    generador.inicializar()

    # iniciamos el controlador
    controlador = ControladorConsultaEncuesta()
    #opc consultar encuesta
    ui = Ui_PantallaConsultarEncuesta(controlador)
    #habiliarPatalla()
    ui.habilitarPantalla(controlador)
    

if __name__ == '__main__':
    main()








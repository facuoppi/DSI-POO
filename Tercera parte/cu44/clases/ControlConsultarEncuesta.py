import csv
import os
import platform
import sys
from typing import List
from clases.Iterator.IteratorLlamadas import IteratorLlamadas,iteradoresLlamadaBD
from clases.Iterator.IAgregado import IAgregado
from clases.Llamada import Llamada, llamadasBD
from clases.Encuesta import encuestasBD,Encuesta
from PyQt5.QtCore import QDate, QDateTime
import pandas as pd
import subprocess
class ControladorConsultaEncuesta(IAgregado):
    __abstract__ = True
    listaIteradores = iteradoresLlamadaBD
    listaPreguntas = []
    def consultarEncuesta(self, pantalla,session):
       self.listaLlamadas = session.query(Llamada).all()
       self.listaEncuestas = session.query(Encuesta).all()
       self.fechaHoraInicio = None
       self.fechaHoraFin = None
       self.llamadasEnPeriodoRespondidas = []
       self.llamadaSeleccionada = None
       self.formatoSeleccionado = None
       self.datosLlamada = None
       self.pantalla = pantalla
       # recorre las encuestas
       for encuesta in self.listaEncuestas:
            # por cada encuesta recorre su lista de preguntas
            for pregunta in encuesta.preguntas:
                # añade la pregunta a la lista de preguntas en memoria
                self.listaPreguntas.append(pregunta)

    def crear_iterador(self,elementos:List[Llamada],filtros:List[object]):
        iterador = IteratorLlamadas().new(elementos,filtros)
        self.listaIteradores.append(iterador)
        return iterador
        
    def tomarSeleccionFechaInicio(self, fecha):
        #recibe la fecha inicio en formato QDate y la convierte a datetime almacenada en fechaHoraInicio
        self.fechaHoraInicio = fecha.toPyDateTime()

    def tomarSeleccionFechaFin(self, fecha):
        #recibe la fecha fin en formato QDate y la convierte a datetime almacenada en fechaHoraFin
        self.fechaHoraFin = fecha.toPyDateTime()
        #el controlador ejecuta el metodo para buscar las llamadas en el periodo seleccionado
        if self.fechaHoraFin != None and self.fechaHoraInicio != None: 
            self.buscarLlamadasRespondidas()

    def buscarLlamadasRespondidas(self):
        #busca las llamadas que esten iniciadas y dentro del periodo previamente seleccioando
        self.llamadasEnPeriodoRespondidas = []
        # count = 0
        # for i in self.listaLlamadas:
        #     count += 1
        #     print(i.getNombreClienteLlamada())
        #     print(count)

        # print("-------------------------------------")
        filtros =[
            ("esDePeriodo", (self.fechaHoraInicio, self.fechaHoraFin)),
            ("tieneEncuestaRespondida", ())
        ]
        if len(self.listaLlamadas) > 0:
            iteradorLlamadas = self.crear_iterador(self.listaLlamadas,filtros)
            iteradorLlamadas.primero()
            conter = 0
            while not iteradorLlamadas.haTerminado():
                
                llamada = iteradorLlamadas.elementoActual()
                if iteradorLlamadas.cumpleFiltro(filtros):
                    self.agregarLlamadaEnPeriodo(llamada)
                # conter += 1
                # print(conter)
                iteradorLlamadas.siguiente()
                
        #el controlador le pide a la pantalla que actualize la tabla con las llamadas en periodo
        self.pantalla.actualizarTablaLlamadas(self.llamadasEnPeriodoRespondidas)
        #retorna la lista de llamadas en periodo
        return self.llamadasEnPeriodoRespondidas
    def obtenerNombreClienteLlamada(self, unaLlamda):
        # se utiliza en la tabla para obtener el nombre del cliente de la llamada
        return unaLlamda.getNombreClienteLlamada()
    def obtenerUltimoEstadoLlamada(self, unaLlamda):
        # se utiliza en la tabla para obtener el ultimo estado de la llamada
        return unaLlamda.determinarUltimoEstado()
    def obtenerDuracionLlamada(self, unaLlamda):
        # se utiliza en la tabla para obtener la duracion de la llamada
        return unaLlamda.getDuracion()
    def agregarLlamadaEnPeriodo(self, llamada_en_periodo):
        self.llamadasEnPeriodoRespondidas.append(llamada_en_periodo)

    def tomarSeleccionLlamada(self, llamadaSeleccionada):
        #al seleccionar una llamada de la tabla, el controlador almacena la llamada seleccionada
        self.llamadaSeleccionada = llamadaSeleccionada
        # el controlador ejecuta el metodo para obtener los datos de la llamada seleccionada
        self.obtenerDatosLlamada()

    def getDatosLlamada(self):
        return self.datosLlamada
    def determinarEstadoInicial(self, unaLlamada):
        # determina el estado inicial de la llamada
        return unaLlamada.determinarEstadoInicial()
    def obtenerDatosLlamada(self):
        # Obtenemos los datos de la llamada seleccionada con el metodo de llamada mostrar datos de llamada
        self.datosLlamada = self.llamadaSeleccionada.mostrarDatosLlamada(self.listaEncuestas, self.listaPreguntas)
        # enviamos los datos obtenidos a la pantalla por el metodo mostrarDatosLlamada
        self.pantalla.mostrarDatosLlamada(self.datosLlamada)
        return self.datosLlamada
    
    def tomarSeleccionFormato(self, seleccion):
        # recibe el formato seleccionado por el usuario en la pantalla y ejecuta el metodo dependiendo del formato
        self.formatoSeleccionado = seleccion
        if self.formatoSeleccionado == "CSV":
            self.generarInformeCSV()
        elif self.formatoSeleccionado == "IMPRIMIR":
            self.generarImpresion()
        elif self.formatoSeleccionado == "AMBOS":
            self.generarInformeCSV()
            self.generarImpresion()
        else:
            raise ValueError(f'No se puede imprimir en formato {seleccion!r}')
        

    def cancelarOperacion(self):
        raise SystemExit(0)

    def generarInformeCSV(self):
        # genera un archivo csv con los datos de la llamada seleccionada
        if self.datosLlamada is None:
            raise ValueError('No hay datos :(')
        directorio = "./informes"
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        datosLlamada = self.datosLlamada
        # header = {
        #     "Nombre de Cliente": self.datosLlamada["nombreCliente"],
        #     "Ultimo Estado": self.datosLlamada["ultimoEstado"],
        #     "Duracion de llamada": self.datosLlamada["duracion"],
        # }
        # body = {
        #      "Preguntas": self.datosLlamada["preguntas"],
        #      "Respuestas": self.datosLlamada["valoresSeleccionados"],
        #      "Encuesta": self.datosLlamada["encuesta"]

        #  }
        # df = pd.DataFrame(body)
        df = pd.DataFrame(datosLlamada)
        archivo = f"{directorio}/{datosLlamada['nombreCliente']}_{datosLlamada['ultimoEstado']}_{str(datosLlamada['duracion'])}.csv"
        df.to_csv(archivo, index=False)
        ruta_absoluta_pdf = os.path.abspath(directorio)
        # Obtén el nombre del sistema operativo
        sistema_operativo = platform.system()

        # Abre el explorador de archivos en la ubicación del PDF según el sistema operativo
        if sistema_operativo == "Windows":
            os.system(f"start explorer /select,{ruta_absoluta_pdf}")
        elif sistema_operativo == "Linux":
            os.system(f"xdg-open {ruta_absoluta_pdf}")
        else:
            print("No se ha implementado el soporte para este sistema operativo.")
        
    def generarImpresion(self):
        # genera un archivo md con los datos de la llamada seleccionada
        directorio = "./informes"
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        if self.datosLlamada is None:
            raise ValueError('No hay datos :(')
        datosLlamada = self.datosLlamada
        df = pd.DataFrame(datosLlamada)
        archivo = "./informes/"+datosLlamada["nombreCliente"]+"_"+datosLlamada["ultimoEstado"] +"_" +str(datosLlamada["duracion"])+".md"
        df.to_markdown(archivo, index=False)
        sistema_operativo = platform.system()

        # Abre el explorador de archivos en la ubicación del PDF según el sistema operativo
        ruta_absoluta_pdf = os.path.abspath(directorio)
        if sistema_operativo == "Windows":
            os.system(f"start explorer /select,{ruta_absoluta_pdf}")
        elif sistema_operativo == "Linux":
            os.system(f"xdg-open {ruta_absoluta_pdf}")
        else:
            print("No se ha implementado el soporte para este sistema operativo.")
        

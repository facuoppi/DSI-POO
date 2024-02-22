import csv
import sys
from clases.Llamada import llamadasBD
from clases.Encuesta import encuestasBD
from PyQt5.QtCore import QDate, QDateTime
import pandas as pd
class ControladorConsultaEncuesta:
    listaLlamadas = llamadasBD
    listaEncuestas = encuestasBD
    listaPreguntas = []
    def consultarEncuesta(self, pantalla):
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
        if len(self.listaLlamadas) > 0:
            #loop mientras haya llamadas
            for unaLlamada in self.listaLlamadas:
                #si la llamada esta dentro del periodo y tiene encuesta respondida con 2 metodos
                if (unaLlamada.esDePeriodo(self.fechaHoraInicio, self.fechaHoraFin) and unaLlamada.tieneEncuestaRespondida()):
                    # agrega la llamada a la lista de llamadas en periodo para ser renderizada en la tabla
                    self.agregarLlamadaEnPeriodo(unaLlamada)

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
        else:
            raise ValueError(f'No se puede imprimir en formato {seleccion!r}')
        

    def cancelarOperacion(self):
        raise SystemExit(0)

    def generarInformeCSV(self):
        # genera un archivo csv con los datos de la llamada seleccionada
        if self.datosLlamada is None:
            raise ValueError('No hay datos :(')
        datosLlamada = self.datosLlamada
        # header = {
        #     "Nombre de Cliente": self.datosLlamada["nombreCliente"],
        #     "Ultimo Estado": self.datosLlamada["ultimoEstado"],
        #     "Duracion de llamada": self.datosLlamada["duracion"],
        # }
        # body = {
        #     "Preguntas": self.datosLlamada["preguntas"],
        #     "Respuestas": self.datosLlamada["valoresSeleccionados"],
        #     "Encuesta": self.datosLlamada["encuesta"]

        # }
        df = pd.DataFrame(datosLlamada)
        df.to_csv('informe.csv', index=False)
        
    def generarImpresion(self):
        # genera un archivo md con los datos de la llamada seleccionada
        if self.datosLlamada is None:
            raise ValueError('No hay datos :(')
        datosLlamada = self.datosLlamada
        df = pd.DataFrame(datosLlamada)
        df.to_markdown('informe.md', index=False)
        

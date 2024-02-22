from PyQt5.QtWidgets import QMessageBox

from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from clases.ControlConsultarEncuesta import ControladorConsultaEncuesta
import sys

class Ui_PantallaConsultarEncuesta:
    def __init__(self, controlador) -> None:
        self.controlador = controlador

    def setupUi(self, PantallaConsultarEncuesta):
        PantallaConsultarEncuesta.setObjectName("PantallaConsultarEncuesta")
        PantallaConsultarEncuesta.resize(881, 705)
        self.centralwidget = QtWidgets.QWidget(PantallaConsultarEncuesta)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 881, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fechaHoraFin_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fechaHoraFin_lbl.setObjectName("fechaHoraFin_lbl")
        self.horizontalLayout.addWidget(self.fechaHoraFin_lbl)
        self.fechaInicio_input = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.fechaInicio_input.setObjectName("fechaInicio_input")
        self.fechaInicio_input.setDateTime(datetime.now() - timedelta(days=10))
        self.horizontalLayout.addWidget(self.fechaInicio_input)
        self.fechaHoraInicio_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fechaHoraInicio_lbl.setObjectName("fechaHoraInicio_lbl")
        self.horizontalLayout.addWidget(self.fechaHoraInicio_lbl)
        self.fechaFin_input = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget)
        self.fechaFin_input.setObjectName("fechaFin_input")
        self.fechaFin_input.setDateTime(datetime.now())
        self.horizontalLayout.addWidget(self.fechaFin_input)
        self.buscarLlamada_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buscarLlamada_btn.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.buscarLlamada_btn)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 871, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.llamadas_tbl = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.llamadas_tbl.setObjectName("llamadas_tbl")
        self.llamadas_tbl.setColumnCount(3)
        self.llamadas_tbl.setHorizontalHeaderLabels(["Nombre Cliente","FechaInicio","Duracion"])
        self.llamadas_tbl.setRowCount(0)
        
        self.verticalLayout.addWidget(self.llamadas_tbl)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.cancelar_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelar_btn.setObjectName("cancelar_btn")
        self.gridLayout.addWidget(self.cancelar_btn, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.llamadaSelected_tbl = QtWidgets.QTableWidget(self.centralwidget)
        self.llamadaSelected_tbl.setGeometry(QtCore.QRect(0, 370, 871, 221))
        self.llamadaSelected_tbl.setObjectName("llamadaSelected_tbl")
        self.llamadaSelected_tbl.setColumnCount(5)
        self.llamadaSelected_tbl.setHorizontalHeaderLabels(["Nombre Cliente","Ultimo Estado","Descripcion Preguntas","Valor Seleccionado","Encuesta"])
        self.llamadasEnPeriodo_lbl = QtWidgets.QLabel(self.centralwidget)
        self.llamadasEnPeriodo_lbl.setGeometry(QtCore.QRect(0, 80, 331, 16))
        self.llamadasEnPeriodo_lbl.setObjectName("llamadasEnPeriodo_lbl")
        self.datoLlamada_lbl = QtWidgets.QLabel(self.centralwidget)
        self.datoLlamada_lbl.setGeometry(QtCore.QRect(10, 350, 231, 16))
        self.datoLlamada_lbl.setObjectName("datoLlamada_lbl")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 590, 871, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formato_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.formato_lbl.setObjectName("formato_lbl")
        self.horizontalLayout_2.addWidget(self.formato_lbl)
        self.formato_input = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.formato_input.setObjectName("formato_input")
        self.formato_input.addItem("")
        self.formato_input.addItem("")
        self.horizontalLayout_2.addWidget(self.formato_input)
        self.confirmar_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.confirmar_btn.setObjectName("confirmar_btn")
        self.horizontalLayout_2.addWidget(self.confirmar_btn)
        PantallaConsultarEncuesta.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PantallaConsultarEncuesta)
        self.statusbar.setObjectName("statusbar")
        PantallaConsultarEncuesta.setStatusBar(self.statusbar)

        self.retranslateUi(PantallaConsultarEncuesta)
        QtCore.QMetaObject.connectSlotsByName(PantallaConsultarEncuesta)

        
        self.llamadas_tbl.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.llamadaSelected_tbl.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # aca se determinan los eventos de los botones para ejecutar las funciones y recibir los datos del actor
        self.buscarLlamada_btn.clicked.connect(self.tomarSeleccionFechaInicio)
        self.buscarLlamada_btn.clicked.connect(self.tomarSeleccionFechaFin)
        self.llamadas_tbl.cellClicked.connect(self.tomarSeleccionLlamada)
        self.cancelar_btn.clicked.connect(self.cancelarOperacion)
        self.confirmar_btn.clicked.connect(self.tomarSeleccionFormato)

        #muestra la pantalla
        PantallaConsultarEncuesta.show()

    def retranslateUi(self, PantallaConsultarEncuesta):
        _translate = QtCore.QCoreApplication.translate
        PantallaConsultarEncuesta.setWindowTitle(_translate("PantallaConsultarEncuesta", "MainWindow"))
        self.fechaHoraInicio_lbl.setText(_translate("PantallaConsultarEncuesta", "                       FechaHoraFin:"))
        self.fechaHoraFin_lbl.setText(_translate("PantallaConsultarEncuesta", "                   FechaHoraInicio:"))
        self.buscarLlamada_btn.setText(_translate("PantallaConsultarEncuesta", "Confirmar"))
        self.cancelar_btn.setText(_translate("PantallaConsultarEncuesta", "cancelar"))
        self.llamadasEnPeriodo_lbl.setText(_translate("PantallaConsultarEncuesta", "Llamadas Iniciadas y en periodo seleccionada:"))
        self.datoLlamada_lbl.setText(_translate("PantallaConsultarEncuesta", "Datos de llamada seleccionada:"))
        self.formato_lbl.setText(_translate("PantallaConsultarEncuesta", "Seleccion de Formato:"))
        self.formato_input.setToolTip(_translate("PantallaConsultarEncuesta", "<html><head/><body><p>Formato de informe</p></body></html>"))
        self.formato_input.setItemText(0, _translate("PantallaConsultarEncuesta", "CSV"))
        self.formato_input.setItemText(1, _translate("PantallaConsultarEncuesta", "IMPRIMIR"))
        self.confirmar_btn.setText(_translate("PantallaConsultarEncuesta", "Generar Informe"))

    def habilitarPantalla(self,controlador):
        #inicia la pantalla y llama al metodo consultarEncuesta del controlador para generarlo
        app = QtWidgets.QApplication(sys.argv)
        self.app = app
        PantallaConsultarEncuesta = QtWidgets.QMainWindow()
        ui = self
        ui.setupUi(PantallaConsultarEncuesta)
        #controlar ejecuta consultarEncuesta
        controlador.consultarEncuesta(ui)
        sys.exit(app.exec_())

    def tomarSeleccionFechaInicio(self):
        #obtiene la fecha inicio del inputLbl y se la pasa al controlador
        self.controlador.tomarSeleccionFechaInicio(self.fechaInicio_input.dateTime())

    def tomarSeleccionFechaFin(self):
        #obtiene la fecha fin del inputLbl y se la pasa al controlador
        self.controlador.tomarSeleccionFechaFin(self.fechaFin_input.dateTime())
        

    def actualizarTablaLlamadas(self,llamadasEnPeridoRespondidas):
        #recibe la lista de llamadas en periodo y las renderiza en la tabla
        #verifica que la lista recibida sea mayor a 0
        if len(llamadasEnPeridoRespondidas)== 0:
            #muestra un mensaje de error cu alternativo A1 no hay llamadas en el periodo
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('No hay llamadas en el periodo seleccionado o no tienen una encuesta respondida')
            msg.setWindowTitle("No hay Llamadas en el periiodo")
            msg.exec_()
        else:
            #vacia la tabla y la renderiza con los datos recibidos
            self.llamadas_tbl.setRowCount(0)
            self.llamadas_tbl.setRowCount(len(llamadasEnPeridoRespondidas))
            self.llamadas_tbl.setColumnCount(3)
            contador = 0
            for unaLlamada in llamadasEnPeridoRespondidas:
                # utiliza el controlador para obtener los datos de la llamada y renderizarlos en la tabla
                self.llamadas_tbl.setItem(contador,0,QtWidgets.QTableWidgetItem(str(self.controlador.obtenerNombreClienteLlamada(unaLlamada))))
                self.llamadas_tbl.setItem(contador,1,QtWidgets.QTableWidgetItem(str(self.controlador.obtenerUltimoEstadoLlamada(unaLlamada))))
                self.llamadas_tbl.setItem(contador,2,QtWidgets.QTableWidgetItem(str(self.controlador.obtenerDuracionLlamada(unaLlamada))))
                contador +=1
    def tomarSeleccionLlamada(self, row, column):
        # toma la seleccion de la tablaLlamadas obteniendo la fila seleccionada y se la pasa al controlador
        # ejecuta el metodo tomarSeleccionLlamada del controlador
        self.controlador.tomarSeleccionLlamada(self.controlador.llamadasEnPeriodoRespondidas[row])

    def mostrarDatosLlamada(self,llamada):
        # recibe los datos de la llamada seleccionada y los renderiza en la tabla
        self.llamadaSelected_tbl.setRowCount(0)
        self.llamadaSelected_tbl.setRowCount(len(llamada))
        self.llamadaSelected_tbl.setItem(0,0,QtWidgets.QTableWidgetItem("Nombre Cliente"))
        self.llamadaSelected_tbl.setItem(0,1,QtWidgets.QTableWidgetItem(llamada["nombreCliente"]))
        self.llamadaSelected_tbl.setItem(1,0,QtWidgets.QTableWidgetItem("Ultimo Estado"))
        self.llamadaSelected_tbl.setItem(1,1,QtWidgets.QTableWidgetItem(llamada["ultimoEstado"]))
        self.llamadaSelected_tbl.setItem(2,0,QtWidgets.QTableWidgetItem("Duracion"))
        self.llamadaSelected_tbl.setItem(2,1,QtWidgets.QTableWidgetItem(str(llamada["duracion"])))
        self.llamadaSelected_tbl.setItem(3,0,QtWidgets.QTableWidgetItem("Respuestas:"))
        self.llamadaSelected_tbl.setItem(3,2,QtWidgets.QTableWidgetItem("Descripcion de Pregunta"))
        self.llamadaSelected_tbl.setItem(3,3,QtWidgets.QTableWidgetItem("Valor Seleccionado"))
        self.llamadaSelected_tbl.setItem(3,4,QtWidgets.QTableWidgetItem("Descripcion de Encuesta"))
        # por cada pregunta genera una fila en la tabla y lo ordena
        for i in range(len(llamada["preguntas"])):
            self.llamadaSelected_tbl.setItem(i+4,2,QtWidgets.QTableWidgetItem(llamada["preguntas"][i]))
            self.llamadaSelected_tbl.setItem(i+4,3,QtWidgets.QTableWidgetItem(llamada["valoresSeleccionados"][i]))
            self.llamadaSelected_tbl.setItem(i+4,4,QtWidgets.QTableWidgetItem(llamada["encuesta"]))
        
    def cancelarOperacion(self):
        # llama al controlador para cancelar la operacion
        self.controlador.cancelarOperacion()

    def tomarSeleccionFormato(self):
        # toma la seleccion del formato y se la pasa al controlador
        msg = QMessageBox()
        try:
            self.controlador.tomarSeleccionFormato(self.formato_input.currentText())
            msg.setIcon(QMessageBox.Information)
            msg.setInformativeText('El informe se genero correctamente en formato '+self.formato_input.currentText())
            msg.setWindowTitle("Informe generado")
        except Exception as e:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
        msg.exec_()

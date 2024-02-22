import datetime
import random

from clases.CambioEstado import CambioEstado, cambiosDeEstadoBD
from clases.Cliente import Cliente, clientesBD
from clases.Encuesta import Encuesta, encuestasBD
from clases.Llamada import Llamada, llamadasBD
from clases.Pregunta import Pregunta, preguntasBD
from clases.RespuestaDeCliente import RespuestaDeCliente, respuestasDeClienteBD
from clases.RespuestaPosible import RespuestaPosible, respuestasPosiblesBD
from clases.Estado import Estado, estadosBD


class GeneradorAleatorio:
    def generarEstado(self):
        estados = ["Iniciada", "EnProceso", "Finalizada"]
        # Aca se crean estados y se agregan a la lista estadosBD
        for estadito in estados:
            estadosBD.append(Estado(estadito))
        
    def generarCambioDeEstado(self,unEstado):
        end_date = datetime.datetime.now()
        start_date = datetime.datetime.now() - datetime.timedelta(days=40)
        
        random_date = start_date + (end_date - start_date) * random.random()
        if unEstado == 0:
            cambioEstadito = CambioEstado(random_date,estadosBD[0])
        else:    
            cambioEstadito = CambioEstado(random_date, estadosBD[unEstado])
        cambiosDeEstadoBD.append(cambioEstadito)
        return cambioEstadito

    def generadorClientes(self):
        # Aca se crean clientes y se agregan a la lista clientesBD
        nombres = ["Juan Ramirez", "Pedro Toledo", "Maria Oppido", "Jose Getta", "Lucas piedra", "Camila Avellaneda", "Florencia gorosito", "Martin Martinez", "Micaela Cordoba", "Lucia Lopez"]
        
        for i in range(len(nombres)):
            clientesBD.append(Cliente(i, nombres[i], 1234567890+i))
    
    def generarEncuestas(self):
        # Aca se crean encuestas y se agregan a la lista encuestasBD
        listaPreguntas = []
        for i in range(10):
            for j in range(5):
                listaPreguntas.append(GeneradorAleatorio().generarPreguntas())
            encuestasBD.append(Encuesta(datetime.datetime.now(), "Encuesta"+str(i), listaPreguntas))
            
    def generarPreguntas(self):
        respuestasPosibles = ["Si", "No", "No se", "A veces", "Siempre", "Nunca"]
        listaRespuestas = []
        for i in respuestasPosibles:
            listaRespuestas.append(GeneradorAleatorio().generarRespuestasPosibles(i))
        nuevaPregunta = Pregunta("Pregunta"+str(len(preguntasBD)+1), listaRespuestas)
        preguntasBD.append(nuevaPregunta)

        return nuevaPregunta

    def generarRespuestasPosibles(self,unaRespuesta):
        descripcionesRespuestaPosible = ["Descripcion1", "Descripcion2", "Descripcion3", "Descripcion4", "Descripcion5"]
        nuevaRespuestaPosible = RespuestaPosible(random.choice(descripcionesRespuestaPosible), unaRespuesta)
        respuestasPosiblesBD.append(nuevaRespuestaPosible)
        return nuevaRespuestaPosible
    
    def generarRespuestaDeCliente(self):
        respuestaCliente = RespuestaDeCliente(datetime.datetime.now(), random.choice(respuestasPosiblesBD))
        respuestasDeClienteBD.append(respuestaCliente) 
        return respuestaCliente
    
    def generarRespuestaDeEncuesta(self,encuesta):
        for i in encuestasBD:
            if i == encuesta:
                pregunta = random.choice(i.preguntas)
                respuestaCliente =RespuestaDeCliente(datetime.datetime.now(), random.choice(pregunta.respuestas))
                respuestasDeClienteBD.append(respuestaCliente)
                return respuestaCliente

    
    def generarLlamada(self):
        descripcionOperador = "DescripcionOperador"
        detalleAccionRequerida = "DetalleSccionRequerida"
        duracion = random.randint(0, 100)
        encuestaEnviada = random.choice(encuestasBD)
        observacionAuditor = "Observaciones"
        respuestaDeEncuesta = []
        for i in range(10):
            respuestaDeEncuesta.append(GeneradorAleatorio().generarRespuestaDeEncuesta(encuestaEnviada))

        cambioEstado = []
        for i in range(random.randint(1, 3)):
            cambioEstado.append(GeneradorAleatorio().generarCambioDeEstado(i-1))
        cliente = random.choice(clientesBD)
            
        nuevaLlamada = Llamada(descripcionOperador, detalleAccionRequerida, duracion, encuestaEnviada, observacionAuditor, respuestaDeEncuesta, cambioEstado, cliente)
        llamadasBD.append(nuevaLlamada)

    def inicializar(self):
        self.generarEstado()
        for i in range(10):
            self.generarEncuestas()
        self.generadorClientes()
        self.generarEncuestas()
        for i in range(20):
            self.generarLlamada()


   













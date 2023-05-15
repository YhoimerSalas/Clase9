import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QScrollArea, QWidget, \
    QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui

from cliente import Cliente
import math


class Ventana2(QMainWindow):

    # metodo constructor de la ventana
    def __init__(self, anterior=None):
        super(Ventana2, self).__init__(anterior)

        # creamos un atributo que guarde la ventana anterior
        self.ventanaAnterior = anterior

        # ponemos el titulo
        self.setWindowTitle("Usuarios registrados")

        # poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))

        # establecemos el ancho y alto

        self.ancho = 1000
        self.alto = 700

        # establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # centramos la ventana
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # fijamos el tamaño la ventana
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap('imagenes/Fondo2.jpg')

        # le asignamos la imagen al fondo
        self.fondo.setPixmap(self.imagenFondo)

        # establecemos que se pueda escalar la imagen
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta a la ventana
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # establecemos la distribucion de los elementos en un layout vertical
        self.vertical = QVBoxLayout()

        # hacemos un letrero
        self.letrero1 = QLabel()

        # le escribimos el texto
        self.letrero1.setText("Usuarios registrados")

        # le asignamos el tipo de letra
        self.letrero1.setFont(QFont("SimSun", 16))

        # le ponemos color de texto
        self.letrero1.setStyleSheet("color: #FFFFFF;")

        # ponemos el letrero en la primera fila
        self.vertical.addWidget(self.letrero1)

        # ponemos un espacio
        self.vertical.addStretch()

        # creamos un scroll
        self.scrollArea = QScrollArea()

        # le ponemos el fondo trasparente al scroll
        self.scrollArea.setStyleSheet("background-color: transparent;")

        # hacemos que el scroll se adapte a los diferentes tamaños
        self.scrollArea.setWidgetResizable(True)

        # creamos un aventana contenedora para cada celda
        self.contenedora = QWidget()

        # vamos a crear un layout de grid para poner una cuadricula de elementos
        self.cuadricula = QGridLayout(self.contenedora)

        # metemos la ventana contenedora en el scroll
        self.scrollArea.setWidget(self.contenedora)

        # metemos en el layout vertical el scroll
        self.vertical.addWidget(self.scrollArea)

        # abrimos el archivo en modo de lectura
        self.file = open('datos/clientes.txt', 'rb')

        # lista vacia para guardar los usuarios
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista de 11 datos separados por ;
            lista = linea.split(";")

            # se para si ya no hay registros en el archivo
            if linea == '':
                break

            # creamos un objeto tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )

            # metemos el objeto en la lista usuario
            self.usuarios.append(u)

        # cerramos el archivo
        self.file.close()

        # Ya tenemos la lista con todos los usuarios

        # obtenemos el numero de usuarios registrados
        # consultamos el tamaño de la lista de los usuarios
        self.numeroUsuarios = len(self.usuarios)

        # contador de elementos para controlar a los usuarios en la lista usuarios
        self.contador = 0

        # definimos la cantidad de elementos a mostrar por columna
        self.elementosPorColumna = 3

        # calculamos el numero de filas
        # redondeamos al entero superior + 1, dividimos por elementosPorColumna
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # controlamos todos los botones por una variable
        self.botones = QButtonGroup()

        # definimos que el controlador de los botones
        # debe agrupar a todos los botones internos
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                # validamos que se estan ingresando la cantidad de usuarios correcta
                if self.contador < self.numeroUsuarios:

                    # en cada celda de la cuadricula va una ventana
                    self.ventanaAuxiliar = QWidget()

                    # se establece el alto y el ancho
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # creamos un layout vertical para cada elemento de la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    # creamos un boton para cada usuario mostrando su cedula
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    # establecemos el ancho del boton
                    self.botonAccion.setFixedWidth(150)

                    # le ponemos los estilos
                    self.botonAccion.setStyleSheet("background-color: #008B45;"
                                                   "color: #FFFFFF;"
                                                    "padding: 10px;")

                    # metemos el boton en el layout vertical para que se vea
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # agregamos el boton al grupo, con su cedula como id
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    # agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # a la ventana le asignamos el layout vertical
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # a la cuadricula le agregamos la ventana en la fila y columna actual
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # aumentamos el contador
                    self.contador += 1

        # establecemos el metodo para que funcionen todos los botones
        self.botones.idClicked.connect(self.metodo_accionBotones)

        # ------------------------------------- BOTON VOLVER ------------------------

        # hacemos el boton para devolvernos a la ventana anterior:
        self.botonVolver = QPushButton("volver")

        # establecemos el ancho del boton:
        self.botonVolver.setFixedWidth(90)

        # le ponemos los estilos:
        self.botonVolver.setStyleSheet("background-color: #008b45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )
        # hacemos que el boton botonContinuar tenga su metodo:
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # metemos en el layout vertical el botonVolver:
        self.vertical.addWidget(self.botonVolver)





        # poner siempre de ultimo
        self.fondo.setLayout(self.vertical)


    # metodo para controlar las acciones de los botones
    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo Ventana2 con el nombre ventana2
    ventana2 = Ventana2()

    # hacemos que ventana2 se vea
    ventana2.show()

    # para que se cierra la aplicacion
    sys.exit(app.exec_())
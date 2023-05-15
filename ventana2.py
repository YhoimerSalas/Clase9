import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication
from PyQt5 import QtGui

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



        # poner siempre de ultimo
        self.fondo.setLayout(self.vertical)

if __name__ == '__main__':

    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo Ventana2 con el nombre ventana2
    ventana2 = Ventana2()

    # hacemos que ventana2 se vea
    ventana2.show()

    # para que se cierra la aplicacion
    sys.exit(app.exec_())
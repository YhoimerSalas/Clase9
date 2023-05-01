import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui

class Ventana1(QMainWindow):
    # metodo constructor de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # ponemos el titulo
        self.setWindowTitle("Formulario de registro")

        # para poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))

        # establecemos el ancho y alto
        self.ancho = 900
        self.alto = 600

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
        self.imagenFondo = QPixmap('imagenes/Fondo.jpg')

        # le asignamos la imagen al fondo
        self.fondo.setPixmap(self.imagenFondo)

        # establecemos que se pueda escalar la imagen
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta a la ventana
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # establecemos la distribucion de los elementos en layout horizontal
        self.horizontal = QHBoxLayout()

        # le ponemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # siempre poner al final
        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana1()

    # hacemos que ventana1 se vea
    ventana1.show()

    # para que se cierra la aplicacion
    sys.exit(app.exec_())
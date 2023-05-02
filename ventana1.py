import sys

from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
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

        # creamos el layout izquierdo:
        self.ladoizquierdo = QFormLayout()

        # hacemos un letrero
        self.letrero1 = QLabel()

        # le escribimos el texto
        self.letrero1.setText("Informacion del cliente")

        # le asignamos el tipo de letra
        self.letrero1.setFont(QFont("SimSun", 16))

        # consultar tipo de letra del pc
        for c in QFontDatabase().families():
            print(c)

        # le ponemos color de texto
        self.letrero1.setStyleSheet("color: #FFFFFF;")

        # agregamos el letrero en la primera fila, solo sera de una columna
        self.ladoizquierdo.addRow(self.letrero1)

        # hacemos un letrero
        self.letrero2 = QLabel()

        # establecemos el ancho
        self.letrero2.setFixedWidth(375)

        # le escribimos el texto
        self.letrero2.setText("Por favor ingrear la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # le asignamos el tipo de letra
        self.letrero2.setFont(QFont("SimSun", 8))

        # le ponemos color de texto y margenes
        self.letrero2.setStyleSheet("color: #FFFFFF; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FFFFFF;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # agregamos el letrero en la siguiente fila
        self.ladoizquierdo.addRow(self.letrero2)

        # hacemos un campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # agregamos al formulario
        self.ladoizquierdo.addRow("Nombre completo*", self.nombreCompleto)

        # hacemos un campo para ingresar el usuario
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # agregamos al formulario
        self.ladoizquierdo.addRow("Usuario*", self.usuario)

        # hacemos el campo para ingresar el password
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # los agregamos al formulario
        self.ladoizquierdo.addRow("Password*", self.password)

        # hacemos el campo para ingresar el password confirmacion
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # los agregamos al formulario
        self.ladoizquierdo.addRow("Comfirmar Password*", self.password2)

        # hacemos un campo para ingresar el documento
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # lo agregamos
        self.ladoizquierdo.addRow("Documento*", self.documento)

        # hacemos un campo para ingresar el correo
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # agregamos al formulario
        self.ladoizquierdo.addRow("Correo*", self.correo)

        # boton para regirtar los datos
        self.botonRegistrar = QPushButton("Registrar")

        # establecemos el ancho del boton
        self.botonRegistrar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonRegistrar.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                 "padding: 10px; margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # hacemos el boton para limpiar los campos
        self.botonLimpiar = QPushButton("Limpiar")

        # establecemos el ancho del boton
        self.botonLimpiar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                 "padding: 10px; margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # agregamos los dos botones a ladoizquierdo
        self.ladoizquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # agregamos el layout ladoizquierdo al layout horozontal
        self.horizontal.addLayout(self.ladoizquierdo)

        # siempre poner al final
        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

    # metodo botonLimpiar
    def accion_botonLimpiar(self):
        pass

    # metodo botonRegistrar
    def accion_botonRegistrar(self):
        pass


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana1()

    # hacemos que ventana1 se vea
    ventana1.show()

    # para que se cierra la aplicacion
    sys.exit(app.exec_())
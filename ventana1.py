import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QPushButton, QLineEdit, \
    QFormLayout, QVBoxLayout, QDialogButtonBox, QDialog
from PyQt5 import QtGui, QtCore


class Ventana1(QMainWindow):
    # metodo constructor de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # ponemos el titulo
        self.setWindowTitle("Formulario de registro")

        # para poner el icono
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

        # creamos el layout del lado derecho
        self.ladoDerecho = QFormLayout()

        # asignamos margen a la izquierda
        self.ladoDerecho.setContentsMargins(50, 0, 0, 0)

        # hacemos un letrero
        self.letrero3 = QLabel()

        # le escribimos el texto
        self.letrero3.setText("Recuperar contraseña")

        # le asignamos el tipo de letra
        self.letrero3.setFont(QFont("SimSun", 16))

        # le ponemos color de texto
        self.letrero3.setStyleSheet("color: #FFFFFF;")

        # agregamos el letrero en la primera fila, solo sera de una columna
        self.ladoDerecho.addRow(self.letrero3)

        # hacemos un letrero
        self.letrero4 = QLabel()

        # establecemos el ancho
        self.letrero4.setFixedWidth(400)

        # le escribimos el texto
        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # le asignamos el tipo de letra
        self.letrero4.setFont(QFont("SimSun", 8))

        # le ponemos color de texto
        self.letrero4.setStyleSheet("color: #FFFFFF; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FFFFFF;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # agregamos el letrero en la primera fila, solo sera de una columna
        self.ladoDerecho.addRow(self.letrero4)

        # 1
        # hacemos el letrero de la primera pregunta y lo agregamos
        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")
        self.ladoDerecho.addRow(self.labelPregunta1)

        # hacemos el campo para ingresar la pregunta y lo agregamos
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta1)

        # hacemos el letrero de la respuesta1 y lo agregamos
        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # hacemos el campo para ingresar respuesta1 y lo agregamos
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)
        self.ladoDerecho.addRow(self.respuesta1)

        # 2
        # hacemos el letrero de la pregunta2 y lo agregamos
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")
        self.ladoDerecho.addRow(self.labelPregunta2)

        # hacemos el campo para ingresar la pregunta y lo agregamos
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta2)

        # hacemos el letrero de la respuesta1 y lo agregamos
        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2*")
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # hacemos el campo para ingresar respuesta1 y lo agregamos
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.respuesta2)

        # 3
        # hacemos el letrero de la pregunta3 y lo agregamos
        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")
        self.ladoDerecho.addRow(self.labelPregunta3)

        # hacemos el campo para ingresar la pregunta y lo agregamos
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta3)

        # hacemos el letrero de la respuesta1 y lo agregamos
        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # hacemos el campo para ingresar respuesta1 y lo agregamos
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.respuesta3)

        # hacemos el boton para buscar preguntas
        self.botonBuscar = QPushButton("Buscar")

        # establecemos el ancho del boton
        self.botonBuscar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonBuscar.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                       "padding: 10px; margin-top: 40px;")

        # self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        # hacemos el boton para recuperar contraseña
        self.botonRecuperar = QPushButton("Recuperar")

        # establecemos el ancho del boton
        self.botonRecuperar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonRecuperar.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                          "padding: 10px; margin-top: 40px;")

        # self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        # agregamos los botones
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)

        # agregamos el layout lado derecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)

        # siempre poner al final
        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

    # metodo botonLimpiar
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    # metodo botonRegistrar
    def accion_botonRegistrar(self):

        # creamos ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300, 150)

        # cramos un boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opcionesBotones = QDialogButtonBox(self.botonAceptar)
        self.opcionesBotones.accepted.connect(self.ventanaDialogo.accept)

        # establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # configuramos la ventana para que sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # creamos un layout vertical
        self.vertical = QVBoxLayout()

        # cramos un label para mensajes
        self.mensaje = QLabel("")

        # le ponemos estilos al label
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        # agregamos las opciones de los botones
        self.vertical.addWidget(self.opcionesBotones)

        # establecemos el layout vertical a la ventana
        self.ventanaDialogo.setLayout(self.vertical)

        # variable para controlar que se han ingresado datos correctos
        self.datosCorrectos = True

        # validamos que los 2 password sean iguales
        if (self.password.text() != self.password2.text()):
            self.datosCorrectos = False

            # texto explicativo
            self.mensaje.setText("Los password no son iguales")

            # para que se vea ventalaDialogo
            self.ventanaDialogo.exec_()

        # validamos que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            # texto explicativo
            self.mensaje.setText("Debe ingresar todos los campos")

            # para que se vea ventalaDialogo
            self.ventanaDialogo.exec_()

        # si los datos estan correctos
        if self.datosCorrectos:

            # abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('datos/clientes.txt', 'ab')

            # trae el texto de los QlineEdit y los agrega contatenados
            self.file.write(bytes(self.nombreCompleto.text() + ";"
                                  + self.usuario.text() + ";"
                                  + self.password.text() + ";"
                                  + self.password2.text() + ";"
                                  + self.documento.text() + ";"
                                  + self.correo.text() + ";"
                                  + self.pregunta1.text() + ";"
                                  + self.respuesta1.text() + ";"
                                  + self.pregunta2.text() + ";"
                                  + self.respuesta2.text() + ";"
                                  + self.pregunta3.text() + ";"
                                  + self.respuesta3.text() + "\n", encoding='UTF-8'))
            # para cerrar el archivo
            self.file.close()

            # abrimos en modo lectura en formato de bytes
            self.file = open('datos/clientes.txt', 'rb')

            # recorre el archivo linea por linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':  # para cuando encuentra una linea vacia
                    break
            self.file.close()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana1()

    # hacemos que ventana1 se vea
    ventana1.show()

    # para que se cierra la aplicacion
    sys.exit(app.exec_())
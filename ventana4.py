import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QApplication, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore

from cliente import Cliente


class Ventana4(QMainWindow):
    def __init__(self, anterior, cedula):
        super(Ventana4, self).__init__(None)

        self.ventanaAnterior = anterior
        self.cendulaUsuario = cedula

        # ponemos el titulo
        self.setWindowTitle("Editar Usuario")

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
        self.fondo.setStyleSheet("background-color: #FFDEAD")

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # establecemos la distribucion de los elementos en un layout vertical
        self.horizontal = QHBoxLayout()

        #le ponemos margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        #_______________CREAMOS EL LAYOUT IZQUIERDO_____________________________

        # creamos el layout izquierdo:
        self.ladoizquierdo = QFormLayout()

        # hacemos un letrero
        self.letrero1 = QLabel()

        # le escribimos el texto
        self.letrero1.setText("Editar Cliente")

        # le asignamos el tipo de letra
        self.letrero1.setFont(QFont("SimSun", 16))

        # le ponemos color de texto
        self.letrero1.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FF8C00;")

        # agregamos el letrero en la primera fila, solo sera de una columna
        self.ladoizquierdo.addRow(self.letrero1)

        # hacemos un letrero
        self.letrero2 = QLabel()

        # establecemos el ancho
        self.letrero2.setFixedWidth(340)

        # le escribimos el texto
        self.letrero2.setText("Por favor ingrear la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # le asignamos el tipo de letra
        self.letrero2.setFont(QFont("SimSun", 8))

        # le ponemos color de texto y margenes
        self.letrero2.setStyleSheet("color: #FFFFFF; margin-bottom: 40px;"
                                    "background-color: #FF8C00;"
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

        #___________BOTON EDITAR_______________

        # boton para editar los datos
        self.botonEditar = QPushButton("Editar")

        # establecemos el ancho del boton
        self.botonEditar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonEditar.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                          "padding: 10px; margin-top: 40px;")

        self.botonEditar.clicked.connect(self.accion_botonEditar)

        #____________BOTON LIMPIAR_________________

        # boton para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        # establecemos el ancho del boton
        self.botonLimpiar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                          "padding: 10px; margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # agregamos los dos botones a ladoizquierdo
        self.ladoizquierdo.addRow(self.botonEditar, self.botonLimpiar)

        #______________BOTON ELIMINAR______________

        # hacemos el boton para eliminar
        self.botonEliminar = QPushButton("Eliminar")

        # establecemos el ancho del boton
        self.botonEliminar.setFixedWidth(90)

        # le ponemos los estilos
        self.botonEliminar.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                        "padding: 10px; margin-top: 10px;")

        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        # agregamos el boton a ladoizquierdo
        self.ladoizquierdo.addRow(self.botonEliminar)

        # _______________BOTON VOLVER_________________

        # hacemos el boton para eliminar
        self.botonVolver = QPushButton("Volver")

        # establecemos el ancho del boton
        self.botonVolver.setFixedWidth(90)

        # le ponemos los estilos
        self.botonVolver.setStyleSheet("background-color: #008B45; color: #FFFFFF;"
                                         "padding: 10px; margin-top: 10px;")

        self.botonVolver.clicked.connect(self.accion_botonVolver)

        # agregamos el boton a ladoizquierdo
        self.ladoizquierdo.addRow(self.botonVolver)

        # agregamos el layout ladoizquierdo al horizontal
        self.horizontal.addLayout(self.ladoizquierdo)

        #___________CREAMOS EL LAYOUT DERECHO_____________

        # creamos el layout del lado derecho
        self.ladoDerecho = QFormLayout()

        # asignamos margen a la izquierda
        self.ladoDerecho.setContentsMargins(60, 0, 0, 0)

        # hacemos un letrero
        self.letrero3 = QLabel()

        # le escribimos el texto
        self.letrero3.setText("Editar Recuperar contraseña")

        # le asignamos el tipo de letra
        self.letrero3.setFont(QFont("SimSun", 16))

        # le ponemos color de texto
        self.letrero3.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FF8C00;")

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
        self.letrero4.setStyleSheet("color: #FFFFFF; background-color: #FF8C00;"
                                    "margin-bottom: 40px;"
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

        # agregamos el layout ladoderecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)

        #_________SIEMPRE PONER AL FINAL_________

        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)

        # -------------------CONSTRUCCION DE LA VENTANA EMERGENTE-----------------------

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

        # llamamos al metodo cargar datos para que se llenen los datos del cliente
        self.cargar_datos()

    def accion_botonEditar(self):

        # variable para controlar que se han ingresado datos correctos
        self.datosCorrectos = True

        # establecemos el titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Formulario de edicion")

        # validamos que los password sean iguales
        if ( self.password.text() != self.password2.text() ):

            self.datosCorrectos = False

            # escribimos un texto explicativo
            self.mensaje.setText("Los passwords no son iguales")

            # hacemos que la ventana de dialogo se vea
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
            self.mensaje.setText("Debe seleccionar un usuario con documento valido")

            # para que se vea ventalaDialogo
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        # si los datos estan correctos
        if self.datosCorrectos:
            # abrimos el archivo en modo lectura
            self.file = open('datos/clientes.txt', 'rb')

            # lista vacia para guardar los usuarios
            usuarios = []

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
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            # Ya tenemos la lista con todos los usuarios

            # variable para controlar si el documento existe
            existeDocumento = False

            # buscamos en la lista usuario por usuario si existe el documento
            for u in usuarios:

                # comparamos el documento ingresado
                # si corresponde con el documento, es el usuario correcto
                if int(u.documento) == self.cendulaUsuario:
                    # guardamos los datos del formulario en las propiedades del usuario

                    u.usuario = self.usuario.text()
                    u.password = self.password.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()
                    # indicamos que encontramos el documento
                    existeDocumento = True
                    # paramos el for
                    break

            # si no existe un usuario con este documento
            if ( not existeDocumento ):
                # escribimos un texto expplicativo
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cendulaUsuario))

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

            # abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('datos/clientes.txt', 'wb')

            # recorremos la lista de usuaris
            # para guardar usuario por usuario en el archivo
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            # para cerrar el archivo
            self.file.close()

            # si existe documento y se edito correctamenett
            if ( existeDocumento ):

                # escribimos texto explicativo
                self.mensaje.setText("Usuario actualizado correctamente!")

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.accion_botonVolver()

            # abrimos el archivo en modo lectura
            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

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

    def accion_botonEliminar(self):

        # variable para controlar que se han ingresado datos correctos
        self.datosCorrectos = True

        # controlamos si vamos a eliminar
        self.eliminar = False

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
            self.mensaje.setText("Debe seleccionar un usuario con documento valido")

            # para que se vea ventalaDialogo
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        # si los datos estan correctos
        if self.datosCorrectos:

            # creamos ventana de dialogo para confirmar si vamos a eliminar
            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            # definimos el tamaño de la ventana
            self.ventanaDialogo.resize(300, 150)

            # configuramos la ventana para que sea modal
            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            # creamos un layout vertical
            self.verticalEliminar = QVBoxLayout()

            # creamos un label para los mensajes
            self.mensajeEliminar = QLabel("¿Esta seguro que desea eliminar este registro?")

            # le ponemos los estilos
            self.mensajeEliminar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

            # agregamos el label de mensaje
            self.verticalEliminar.addWidget(self.mensajeEliminar)

            # agregamos las opciones de aceptar y cancelar en la ventana de dialogo
            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # agregamos las opciones de los botones
            self.verticalEliminar.addWidget(self.opcionesBox)

            # establecemos el layout para la ventana
            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            # hacemos que la ventana se vea
            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            # abrimos el archivo en modo lectura
            self.file = open('datos/clientes.txt', 'rb')

            # lista vacia para guardar los usuarios
            usuarios = []

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
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            # Ya tenemos la lista con todos los usuarios

            # variable para controlar si el documento existe
            existeDocumento = False

            # buscamos en la lista usuario por usuario si existe el documento
            for u in usuarios:

                # comparamos el documento ingresado
                # si corresponde con el documento, es el usuario correcto
                if int(u.documento) == self.cendulaUsuario:

                    # eliminamos el usuario de la lista de usuarios
                    usuarios.remove(u)
                    existeDocumento = True
                    # paramos el for
                    break

            # abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('datos/clientes.txt', 'wb')

            # recorremos la lista de usuaris
            # para guardar usuario por usuario en el archivo
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            # para cerrar el archivo
            self.file.close()

            # si existe documento y se edito correctamenett
            if (existeDocumento):

                # escribimos texto explicativo
                self.mensaje.setText("Usuario eliminado exitosamente!")

                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.accion_botonVolver()

    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):
        # abrimos el archivo en modo lectura
        self.file = open('datos/clientes.txt', 'rb')

        # lista vacia para guardar los usuarios
        usuarios = []

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
            usuarios.append(u)

        # cerramos el archivo
        self.file.close()

        # en este punto tenemos la lista de usuarios con todos los usuarios

        # variable para controlar si el documento existe
        existeDocumento = False

        # buscamos en la lista usuario por usuario si existe el documento
        for u in usuarios:

            # comparamos el documento ingresado
            # si corresponde con el documento, es el usuario correcto
            if int(u.documento) == self.cendulaUsuario:

                # mostramos los datos en el formulario
                self.nombreCompleto.setText(u.nombreCompleto)
                # hacemos que el nombre no se pueda editar
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                # hacemos que el documento no se pueda editar
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)
                # indocamos que encontramos el documento
                existeDocumento = True
                # paramos el for
                break

        # si no existe un usuario con el documento
        if ( not existeDocumento ):

            # escribimos un texto explicativo
            self.mensaje.setText("No existe un usuario con este documento:\n"
                                 + str(self.cendulaUsuario))

            # hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()

if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo Ventana1 con el nombre ventana1
    ventana1 = Ventana4()

    # hacemos que ventana1 se vea
    ventana1.show()

    # para que se cierra la aplicacion
    sys.exit(app.exec_())

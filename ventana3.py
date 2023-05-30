import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication, QToolBar, QAction, QMessageBox
from PyQt5 import QtGui

from cliente import Cliente



class Ventana3(QMainWindow):

    # Hacer el metodo de construccion de la ventana:
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        # Creamos un atributo que guarde la ventana anterior:
        self.ventanaAnterior = anterior

        # Poner el titulo:
        self.setWindowTitle("usuarios Registrados")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/bag.png'))

        # Estableciendo las propiedades de ancho y alto:
        self.ancho = 900
        self.alto = 600

        # establecer el tamano de la ventana:
        self.resize(self.ancho, self.alto)

        # hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal:
        self.fondo = QLabel(self)

        # definimos la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/fondo4.jpg')

        # Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamano de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

        # lista vacia para guardar los usuarios:
        self.usuarios = []

        # recorremos el archivo, linea por linea:
        while self.file:

            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista con 11 datos separados por;
            lista = linea.split(";")
            # Separa si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto tipo cliente llamado u
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
            # Metemos el objeto en la lista de usuarios:
            self.usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto tenemos la lista usuarios con todos los usuarios:

        # Obtenemos el numero de usuarios registrados:
        # Consultamos el tamano de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la tabla:
        self.contador = 0

        # Establecemos la distribucion de los elementos en layout vertical:
        self.vertical = QVBoxLayout()

        # ---------------- CONSTRUIR EL MENU TOOLBAR ----:

        self.toolbar = QToolBar('Main toolbar')
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        # -------------- delete ----------
        self.delete = QAction(QIcon('imagenes/delete.png'), '&Delete', self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # ---------- add ---------
        self.add = QAction(QIcon('imagenes/add.png'), '&Add', self)
        self.add.triggered.connect(self.accion_add)
        self.toolbar.addAction(self.add)

        # ---------- insert ------------
        self.insert = QAction(QIcon('imagenes/edit.png'), '&Insert', self)
        self.insert.triggered.connect(self.accion_insert)
        self.toolbar.addAction(self.insert)

        # ---------------------------- FIN MENU TOOLBAR --------------------------------


        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: #000080;")

        # Agregamos el letrero en la primera fila:
        self.vertical.addWidget(self.letrero1)

        # Ponemos un espacio despues:
        self.vertical.addStretch()

        # Creamos un scroll:
        self.scrollArea = QScrollArea()

        # Hacemos Que el scroll se adapte a diferentes tamanos:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una tabla:
        self.tabla = QTableWidget()

        # definimos el numero de columnas que tendra la tabla:
        self.tabla.setColumnCount(11)

        # definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        # Definimos el texto de la cabecera:
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])

        # Establecemos el numero de filas:
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla:
        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            # Hacemos que el nombre no se pueda editar:
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # Hacemos que el documento no se pueda editar:
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Metemos en el layout vertical el scroll:
        self.vertical.addWidget(self.scrollArea)

        # Ponemos un espacio despues:
        self.vertical.addStretch()

        # ------------------------- BOTON VOLVER ------------------------

        # Hacemos el boton para devolvernos a la ventana anterior:
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del boton:
        self.botonVolver.setFixedWidth(90)

        # le ponemos los estilos:
        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )

        # Hacemos que l boton botonContinuar tenga su metodo:
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Metemos en el layout vertical el botonVolver:
        self.vertical.addWidget(self.botonVolver)

        # ------------------- OJO IMPORTANTE PONER AL FINAL --------

        # indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def accion_delete(self):
        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self,'Warning', 'Para borrar, se debe seleccionar un registro')

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Esta seguro de que quieres borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if boton == QMessageBox.StandardButton.Yes:

            if (
                self.tabla.item(filaActual, 0).text() != '' and
                self.tabla.item(filaActual, 1).text() != '' and
                self.tabla.item(filaActual, 2).text() != '' and
                self.tabla.item(filaActual, 3).text() != '' and
                self.tabla.item(filaActual, 4).text() != '' and
                self.tabla.item(filaActual, 5).text() != '' and
                self.tabla.item(filaActual, 6).text() != '' and
                self.tabla.item(filaActual, 7).text() != '' and
                self.tabla.item(filaActual, 8).text() != '' and
                self.tabla.item(filaActual, 9).text() != '' and
                self.tabla.item(filaActual, 10).text() != ''
            ):

                # Abrimos el archivo en modo de lectura:
                self.file = open('datos/clientes.txt', 'rb')

                # lista vacia para guardar los usuarios:
                usuarios = []

                # Iteramos sobre el archivo linea por linea:
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # obtenemos dle string una lista con 11 datos separados por ;
                    lista = linea.split(";")
                    # va a parar si ya no hay mas registros en el archivo
                    if linea == '':
                        break
                    # creamos un objeto tipo cliente llamado u
                    # y le pasamos los elementos de la lista:
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
                        lista[10]
                    )
                    # metemos el objeto en la lista de usuarios:
                    usuarios.append(u)

                # cerramos el archivo:
                self.file.close()

                # en este punto tenemos la lista usuarios con todos los usuarios:

                # Recorremos la lista de usuarios
                for u in usuarios:
                    # buscamos el usuario por el documento:
                    if(
                        u.documento == self.tabla.item(filaActual, 3).text()
                    ):
                        # Indicamos que encontramos el documento:
                        existeRegistro = True

                        # Removemos el usuario de la lista de usuarios:
                        usuarios.remove(u)

                        # paramos el for:
                        break

                # Abrimos el archivo en modo escritura para reescribir los datos sin el usuario borrado.
                self.file = open('datos/clientes.txt', 'wb')

                # recorremos la lista de usuarios
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
                self.file.close()

                # Hacemos que en la tabla no se vea el registro:
                self.tabla.removeRow(filaActual)

                return QMessageBox.question(
                    self,
                    'Confirmation',
                    'El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )
            else:
                # Hacemos que en la tabla no se vea el registro en case de tratarse de una fila vacia:
                self.tabla.removeRow(filaActual)


    def accion_add(self):
        # Obtenemos el numero de filas que tiene la tabla:
        ultimaFila = self.tabla.rowCount()

        # Insertamos una fila nueva despues de la ultima fila:
        self.tabla.insertRow(ultimaFila)

        # llenamos cada celda de la nueva fila con un string vacio '':
        self.tabla.setItem(ultimaFila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 3, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 4, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 5, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 6, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 7, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 8, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 9, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 10, QTableWidgetItem(''))
    def accion_insert(self):

        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self, 'Warning', 'Para ingresar, debe seleccionar un registro')

        boton = QMessageBox.question(
            self,
            'Confirmation',
            '¿Esta seguro de que quiere ingresar este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        # variable para controlar que se hayan ingresado todos los datos:
        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            # Validamos que se hayan ingresado los datos:
            if (
                self.tabla.item(filaActual, 0).text() != '' and
                self.tabla.item(filaActual, 1).text() != '' and
                self.tabla.item(filaActual, 2).text() != '' and
                self.tabla.item(filaActual, 3).text() != '' and
                self.tabla.item(filaActual, 4).text() != '' and
                self.tabla.item(filaActual, 5).text() != '' and
                self.tabla.item(filaActual, 6).text() != '' and
                self.tabla.item(filaActual, 7).text() != '' and
                self.tabla.item(filaActual, 8).text() != '' and
                self.tabla.item(filaActual, 9).text() != '' and
                self.tabla.item(filaActual, 10).text() != ''
            ):
                # Actualizamos la variable para indicar que se ingresaron todos los datos:
                datosVacios = False

                # Abrimos el archivo en modo de lectura:
                self.file = open('datos/clientes.txt', 'rb')

                # lista vacia para guardar los usuarios:
                usuarios = []

                # Iteramos sobre el archivo liena por linea:
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # obtenemos del string una lista con 11 datos separados por ;
                    lista = linea.split(";")
                    # se detiene si yan o hay mas Registros en el archivo
                    if linea == '':
                        break
                    # Creamos un objeto tipo cliente llamado u
                    # y le pasamos los elementos de la lista:
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
                        lista[10]
                    )
                    # metemos el objeto en la lista de usuarios:
                    usuarios.append(u)

                # Cerramos el archivo:
                self.file.close()

                # En este punto tenemos la lista usuarios con todos los usuarios:

                # Variable para controlar si ya existe el registro:
                existeRegistro = False

                # Variable para controlar si ya es un registro que ya existe y se va a editar:
                existeDocumento = False

                # recorremos la lista de usuarios
                for u in usuarios:
                    # comparamos todos los datos del registro ingresado:
                    if (
                        u.nombreCompleto == self.tabla.item(filaActual, 0).text() and
                        u.usuario == self.tabla.item(filaActual, 1).text() and
                        u.password == self.tabla.item(filaActual, 2).text() and
                        u.documento == self.tabla.item(filaActual, 3).text() and
                        u.correo == self.tabla.item(filaActual, 4).text() and
                        u.pregunta1 == self.tabla.item(filaActual, 5).text() and
                        u.respuesta1 == self.tabla.item(filaActual, 6).text() and
                        u.pregunta2 == self.tabla.item(filaActual, 7).text() and
                        u.respuesta2 == self.tabla.item(filaActual, 8).text() and
                        u.pregunta3 == self.tabla.item(filaActual, 9).text() and
                        u.respuesta3 == self.tabla.item(filaActual, 10).text()
                    ):
                        # Indicamos que encontramos el docuemnto:
                        existeRegistro = True

                        return QMessageBox.warning(self, 'Warning', 'Registro duplicado, no se puede registrar')

                        # Paramos el for:
                        break


            # si los datos son diferentes a lo que existe:
            if not existeRegistro:

                # Recorre la lista de usuarios
                for u in usuarios:
                    # comparamo todos los datos del registro ingresado ocn el documento:
                    if (u.documento == self.tabla.item(filaActual, 3).text()):
                        # Indicamos que encontramos el documento
                        existeDocumento = True

                        # Volvemos a actualizar todos los datos del usuario:
                        u.nombreCompleto = self.tabla.item(filaActual, 0).text()
                        u.usuario = self.tabla.item(filaActual, 1).text()
                        u.password = self.tabla.item(filaActual, 2).text()
                        u.documento = self.tabla.item(filaActual, 3).text()
                        u.correo = self.tabla.item(filaActual, 4).text()
                        u.pregunta1 = self.tabla.item(filaActual, 5).text()
                        u.respuesta1 = self.tabla.item(filaActual, 6).text()
                        u.pregunta2 = self.tabla.item(filaActual, 7).text()
                        u.respuesta2 = self.tabla.item(filaActual, 8).text()
                        u.pregunta3 = self.tabla.item(filaActual, 9).text()
                        u.respuesta3 = self.tabla.item(filaActual, 10).text()

                        # abrimos el archivo en modo escritura escribiendo datos en binario.
                        self.file = open('datos/clientes.txt', 'wb')

                        # recorremos la lista de usuarios
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

                        self.file.close()

                        return QMessageBox.question(
                            self,
                            'Confirmation',
                            'Los datos del registro se han editado exitosamente.',
                            QMessageBox.StandardButton.Yes
                        )

                        # Paramos el for:
                        break

                # si se trata de un usuario nuevo:
                if not existeDocumento:
                    # Abrimos el archivo en modo agregar escribiendo datos en binario.
                    self.file = open('datos/clientes.txt', 'ab')

                    # agregamos los datos de la fila en el archivo
                    self.file.write(bytes(self.tabla.item(filaActual, 0).text() + ";" +
                                          self.tabla.item(filaActual, 1).text() + ";" +
                                          self.tabla.item(filaActual, 2).text() + ";" +
                                          self.tabla.item(filaActual, 3).text() + ";" +
                                          self.tabla.item(filaActual, 4).text() + ";" +
                                          self.tabla.item(filaActual, 5).text() + ";" +
                                          self.tabla.item(filaActual, 6).text() + ";" +
                                          self.tabla.item(filaActual, 7).text() + ";" +
                                          self.tabla.item(filaActual, 8).text() + ";" +
                                          self.tabla.item(filaActual, 9).text() + ";" +
                                          self.tabla.item(filaActual, 10).text() + "\n", encoding='UTF-8'))
                    self.file.seek(0, 2)
                    self.file.close()
                return QMessageBox.question(
                    self,
                    'Confirmation',
                    'Los datos del registro se han ingresado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )

        if datosVacios:
            return QMessageBox.warning(self, 'Warning', 'Debe ingresar todos los datos en el registro')














if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana3 = Ventana3()

    ventana3.show()

    sys.exit(app.exec_())
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QStatusBar
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt, QPoint, QSize
from PySide6.QtGui import QFont, QPainter, QBrush, QColor, QIcon
from util.util_popup import CustomMessageBox
from util.util_roundbutton import RoundButton
import re


# Importar el archivo de recursos generado
import rc_resources

class Ui_RegisterMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(625, 565)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 550, 500))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(:/img/imagenes/login-regi-imagen.png);\n"
"border-top-left-radius: 50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 30, 240, 430))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(300, 220, 190, 40))
        font = QFont()
        font.setFamilies([u"LEMON MILK"])
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(300, 300, 190, 40))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 350, 181, 51))
        font1 = QFont()
        font1.setFamilies([u"LEMON MILK"])
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 #E5BF89, stop:1 rgba(255, 0, 0, 0.35) );\n"
"    color:rgba(255, 255, 255, 210);\n"
"   border-radius:25px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"   padding-left:5px;\n"
"    padding-top:5px;\\n\n"
"  background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 400, 211, 21))
        font2 = QFont()
        font2.setFamilies([u"LEMON MILK"])
        font2.setPointSize(7)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.botonlogin = QPushButton("Logeate Aquí",self.widget)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 30, 171, 131))
        self.label_6.setStyleSheet(u"border-image: url(:/img/imagenes/tfglogo.png);")
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(300, 140, 190, 40))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contraseña", None))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00bfYa tienes cuenta?", None))
        self.label_5.setStyleSheet("margin-left: 12px;")
        self.label_6.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMAIL", None))

        font_button = QFont()
        font_button.setPointSize(7)  # Tamaño de fuente más pequeño
        self.botonlogin.setFont(font_button)
        self.botonlogin.setGeometry(326, 420, 211, 21)
        self.botonlogin.setFixedSize(120, 30)
        self.botonlogin.setStyleSheet(u"QPushButton {\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 #E5BF89, stop:1 rgba(255, 0, 0, 0.35) );\n"
                                                 "    color:rgba(255, 255, 255, 210);\n"
                                                 "    border-radius: 15px;\n"
                                                 "    margin-left: 12px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover{\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed{\n"
                                                 "    padding-left: 5px;\n"
                                                 "    padding-top: 5px;\n"
                                                 "    background-color:rgba(150, 123, 111, 255);\n"
                                                 "}")
        self.botonlogin.clicked.connect(self.open_login_window)

    def open_login_window(self):
            from formularios.ui_Login import LoginWindow
            self.hide()
            self.login_window = LoginWindow()
            self.login_window.show()

class RegisterMainWindow(QMainWindow, Ui_RegisterMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # Ocultar el marco de la ventana
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # Hacer que la ventana sea transparente

        self.pushButton_close = RoundButton(self)  # Icono de x
        self.pushButton_close.setIcon(QIcon("./imagenes/cerrar.png"))      
        self.pushButton_close.setStyleSheet("QPushButton {background-color: #dc3545; border-radius: 15px; border: none; color: white; font-family: FontAwesome; font-size: 16px; padding: 5px 10px;} QPushButton:hover {background-color: #830000;}") # Personalizar estilo del botón
        icon_size = QSize(8, 8)  # Tamaño del icono
        self.pushButton_close.setIconSize(icon_size)  # Establecer el tamaño del icono
        self.pushButton_close.setGeometry(QRect(500, 65, 40, 40))
        self.pushButton_close.clicked.connect(self.close)

        self.old_pos = self.pos()  # Posición antigua para el movimiento

        # Conectar eventos de mouse a la ventana principal para hacerla arrastrable
        self.mousePressEvent = self.mousePressEvent
        self.mouseMoveEvent = self.mouseMoveEvent

        # Conectar el botón de registro al método de registro
        self.pushButton.clicked.connect(self.registrarse)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def registrarse(self):
        usuario = self.lineEdit.text()
        contrasena = self.lineEdit_2.text()
        email = self.lineEdit_3.text()

        if usuario and contrasena and email:  # Verificar que los campos no estén vacíos
            # Validar el formato del correo electrónico
            if not re.match(r'^.+@[^@]+\.[^@]+$', email):
                message_box = CustomMessageBox()
                message_box.setIcon(QMessageBox.Warning)
                message_box.setText("El formato del correo electrónico no es válido. Por favor, inténtelo de nuevo.")
                message_box.exec()
                return

            # Conectar a la base de datos SQLite
            conexion = sqlite3.connect('tfg.db')
            cursor = conexion.cursor()

            try:
                # Verificar si el nombre de usuario ya existe en la base de datos
                cursor.execute('SELECT COUNT(*) FROM Usuarios WHERE nusuario = ?', (usuario,))
                existe = cursor.fetchone()[0]
                if existe:
                    message_box = CustomMessageBox()
                    message_box.setIcon(QMessageBox.Warning)
                    message_box.setText("El nombre de usuario ya está en uso. Por favor, elige otro.")
                    message_box.exec()
                    return

                # Crear la tabla si no existe
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nusuario TEXT,
                        correo TEXT,
                        contrasena TEXT
                    )
                ''')

                # Insertar los datos del usuario en la base de datos
                cursor.execute('''
                    INSERT INTO Usuarios (nusuario, correo, contrasena)
                    VALUES (?, ?, ?)
                ''', (usuario, email, contrasena))

                # Guardar los cambios en la base de datos
                conexion.commit()
                message_box = CustomMessageBox()
                message_box.setIcon(QMessageBox.Information)
                message_box.setText("Usuario registrado correctamente")
                message_box.exec()
            except Exception as e:
                message_box = CustomMessageBox()
                message_box.setIcon(QMessageBox.Critical)
                message_box.setText(f'Error al registrar usuario: {str(e)}')
                message_box.exec()
            finally:
                # Cerrar la conexión a la base de datos
                conexion.close()
        else:
            message_box = CustomMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Por favor, complete todos los campos.")
            message_box.exec()


    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = RegisterMainWindow()
    window.show()
    sys.exit(app.exec_())

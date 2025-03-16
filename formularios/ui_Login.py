import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QStatusBar
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt, QPoint, QSize
from PySide6.QtGui import QFont, QPainter, QBrush, QColor, QBitmap, QIcon
from formularios.ui_Register import RegisterMainWindow
from formularios.form_maestro_design import FormularioMaestroDesign
from util.util_popup import CustomMessageBox
from util.util_roundbutton import RoundButton

# Importar el archivo de recursos generado
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(625, 565)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(30, 30, 550, 500)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(40, 30, 280, 430)
        self.label.setStyleSheet(u"border-image: url(:/img/imagenes/login-regi-imagen.png);\n"
                                  "border-top-left-radius: 50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(270, 30, 240, 430)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                  "border-bottom-right-radius: 50px;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(295, 150, 190, 40)
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
        self.lineEdit_2.setGeometry(295, 230, 190, 40)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgba(46,82,101,200);\n"
                                       "color: rgba(0,0,0,240);\n"
                                       "padding-bottom: 7px;\n"
                                       "")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(300, 300, 181, 51)
        font1 = QFont()
        font1.setFamilies([u"LEMON MILK"])
        font1.setPointSize(12)
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
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(290, 370, 211, 21)
        font2 = QFont()
        font2.setFamilies([u"LEMON MILK"])
        font2.setPointSize(7)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(285, 360, 211, 21)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(300, 30, 171, 131)
        self.label_6.setStyleSheet(u"border-image: url(:/img/imagenes/tfglogo.png);")
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesión", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"¿No tienes cuenta? ", None))
        self.label_6.setText("")


class LoginWindow(QMainWindow, Ui_MainWindow):
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

        # Inicializar variables para el seguimiento del movimiento de la ventana
        self.old_pos = self.pos()
        self.mouse_pressed = False

        # Conexión del botón de inicio de sesión
        self.pushButton.clicked.connect(self.login)

        # Botón de registro
        self.pushButton_register = QPushButton("Registrarse aquí", self)
        font_button = QFont()
        font_button.setPointSize(7)  # Tamaño de fuente más pequeño
        self.pushButton_register.setFont(font_button)
        self.pushButton_register.setGeometry(360, 420, 211, 21)
        self.pushButton_register.setFixedSize(120, 30)
        self.pushButton_register.setStyleSheet(u"QPushButton {\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 #E5BF89, stop:1 rgba(255, 0, 0, 0.35) );\n"
                                                 "    color:rgba(255, 255, 255, 210);\n"
                                                 "    border-radius: 15px;\n"
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
        self.pushButton_register.clicked.connect(self.open_register_window)

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()
        self.mouse_pressed = True

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.mouse_pressed = False

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username and password:
            # Conectar a la base de datos SQLite
            conexion = sqlite3.connect('tfg.db')
            cursor = conexion.cursor()

            try:
                # Consultar la base de datos para el usuario proporcionado
                cursor.execute('SELECT id FROM Usuarios WHERE nusuario=? AND contrasena=?', (username, password))
                user_id = cursor.fetchone()

                if user_id:
                    # Si el usuario existe en la base de datos, mostrar un mensaje de bienvenida
                    message_box = CustomMessageBox()
                    message_box.setIcon(QMessageBox.Information)
                    message_box.setText(f"¡Bienvenido, {username}!")
                    message_box.exec()
                    self.abrir_app(user_id[0])  # Abrir la aplicación principal con la ID del usuario

                else:
                    # Si el usuario no existe en la base de datos, mostrar un mensaje de error
                    message_box = CustomMessageBox()
                    message_box.setIcon(QMessageBox.Warning)
                    message_box.setText("Usuario o contraseña incorrectos.")
                    message_box.exec()
            
            finally:
                # Cerrar la conexión a la base de datos
                conexion.close()
        else:
            # Si el usuario o la contraseña están vacíos, mostrar un mensaje de advertencia
            message_box = CustomMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Por favor, complete todos los campos.")
            message_box.exec()

    def open_register_window(self):
        self.hide()
        self.register_window = RegisterMainWindow()
        self.register_window.show()

    def abrir_app(self, user_id):
        self.hide()
        self.mainapp_window = FormularioMaestroDesign(user_id)  # Pasar la ID del usuario al formulario principal
        self.mainapp_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

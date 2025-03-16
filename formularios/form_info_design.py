from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class FormularioInfoDesign(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Info Picanton')
        self.setWindowIcon(QIcon("./imagenes/logo.ico"))
        self.resize(400, 200)
        self.construir_widget()

    def construir_widget(self):
        self.labelVersion = QLabel(self)
        self.labelVersion.setText("Version : 1.0")
        self.labelVersion.setStyleSheet("color: #000000; font-size: 15pt;")
        self.labelVersion.setAlignment(Qt.AlignCenter)
        self.labelVersion.setGeometry(0, 0, 400, 50)

        self.labelAutor = QLabel(self)
        self.labelAutor.setText("Autor : Juan Jose Montero Solano")
        self.labelAutor.setStyleSheet("color: #000000; font-size: 15pt;")
        self.labelAutor.setAlignment(Qt.AlignCenter)
        self.labelAutor.setGeometry(0, 50, 400, 50)

        self.labelAutor2 = QLabel(self)
        self.labelAutor2.setText("Autor : Luis Rebollo Diaz")
        self.labelAutor2.setStyleSheet("color: #000000; font-size: 15pt;")
        self.labelAutor2.setAlignment(Qt.AlignCenter)
        self.labelAutor2.setGeometry(0, 100, 400, 50)

        self.labelAutor3 = QLabel(self)
        self.labelAutor3.setText("Autor : Adrian Aznar Madrid")
        self.labelAutor3.setStyleSheet("color: #000000; font-size: 15pt;")
        self.labelAutor3.setAlignment(Qt.AlignCenter)
        self.labelAutor3.setGeometry(0, 150, 400, 50)




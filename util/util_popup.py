from PySide6.QtWidgets import  QLabel, QMessageBox
from PySide6.QtCore import  Qt


class CustomMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # Sin marco
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.background_label = QLabel(self)
        self.update_background_label_geometry()  # Igual tamaño que la ventana
        self.background_label.setStyleSheet("""
            background-color: white; /* Fondo blanco semi-transparente */
            border: 4px solid #E5BF89; /* Borde sólido */
            border-radius: 20px; /* Bordes redondeados */
        """)
        self.setStyleSheet("""

            QMessageBox {
                background-color: #ffffff; /* Fondo blanco */
                color: #000000;
                border-radius: 10px; /* Bordes redondeados */
                border: 4px solid #E5BF89; /* Borde sólido */
            }
            
            QMessageBox QPushButton {
                background-color: #E5BF89;
                color: #ffffff;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            
            QMessageBox QPushButton:hover {
                background-color: #8A2200;
            }
        """)
        self.background_label.lower()  # Hacer que la etiqueta de fondo esté detrás de la caja de mensajeç

    def update_background_label_geometry(self):
        """Actualizar la geometría de la etiqueta de fondo para que coincida con la ventana."""
        self.background_label.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        """Manejar el evento de redimensionamiento de la ventana."""
        super().resizeEvent(event)
        self.update_background_label_geometry()  # Actualizar la geometría de la etiqueta de fondo al cambiar el tamaño de la ventana

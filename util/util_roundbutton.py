
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QBrush
from PySide6.QtWidgets import (QPushButton)

class RoundButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(30, 30)  # Ajusta el tamaño del botón para que sea cuadrado

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Color de fondo del botón
        if self.isEnabled():
            color = self.palette().button().color()
        else:
            color = self.palette().disabled().color()

        painter.setBrush(QBrush(color))

        # Dibuja un rectángulo redondeado
        rect = self.rect()
        painter.drawRoundedRect(rect, 15, 15)

        # Dibuja el icono en el centro del botón
        icon = self.icon()
        if not icon.isNull():
            icon_rect = icon.pixmap(self.iconSize()).rect()
            icon_rect.moveCenter(rect.center())
            painter.drawPixmap(icon_rect, icon.pixmap(self.iconSize()))

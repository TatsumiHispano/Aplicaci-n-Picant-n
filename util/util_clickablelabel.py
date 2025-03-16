
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (QLabel)

class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

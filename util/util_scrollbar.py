
from PySide6.QtWidgets import (QScrollBar)

class ModernScrollBar(QScrollBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background: #E5BF89;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical:hover {
                background: #555;
            }
        """)



import sys
import os
from PySide6.QtCore import Qt, QTimer, QRectF, QPointF
from PySide6.QtGui import QPainter, QPen, QColor, QFont, QConicalGradient, QPixmap, QPainterPath
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QMainWindow
from formularios.ui_Login import LoginWindow

class CircularProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.width = 300
        self.height = 300
        self.logowidth = 360
        self.logoheight = 360
        self.progress_color = QColor(229, 191, 137)
        self.background_color = QColor(60, 60, 60)
        self.text_color = QColor(229, 191, 137)
        self.logo_pixmap = None
        self.initUI()

       

    

    def initUI(self):
        self.setMinimumSize(self.width, self.height)
        self.loadLogo()

    def loadLogo(self):
        logo_path = './imagenes/loading.png'
        if not os.path.exists(logo_path):
            QMessageBox.critical(self, "Error", f"Logo file not found: {logo_path}")
            return

        self.logo_pixmap = QPixmap(logo_path)
        if self.logo_pixmap.isNull():
            QMessageBox.critical(self, "Error", f"Failed to load logo image: {logo_path}")

    def setValue(self, value):
        self.value = value
        self.update()

    def paintEvent(self, event):
        width = self.width
        height = self.height
        value = self.value

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw background circle
        pen = QPen()
        pen.setWidth(14)
        pen.setColor(self.background_color)
        painter.setPen(pen)
        painter.drawEllipse(7, 7, width - 14, height - 14)

        # Draw progress circle with rounded ends
        gradient = QConicalGradient(QPointF(width / 2, height / 2), -90)
        gradient.setColorAt(0.0, self.progress_color.lighter())
        gradient.setColorAt(1.0, self.progress_color.darker())
        pen.setBrush(gradient)
        pen.setColor(self.progress_color)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        
        rect = QRectF(7, 7, width - 14, height - 14)
        startAngle = 90
        spanAngle = -360 * (value / 100)

        path = QPainterPath()
        path.arcMoveTo(rect, startAngle)
        path.arcTo(rect, startAngle, spanAngle)
        painter.drawPath(path)

        # Draw logo in the center if it is loaded
        if self.logo_pixmap and not self.logo_pixmap.isNull():
            logo_size = min(self.logowidth, self.logoheight)
            logo_x = (width - logo_size) // 2
            logo_y = (height - logo_size) // 2
            painter.drawPixmap(logo_x, logo_y, logo_size, logo_size, self.logo_pixmap)

        # Draw text (adjusted to be more to the right)
        font = QFont("Arial", 30, QFont.Bold)
        painter.setFont(font)
        painter.setPen(self.text_color)
        text_rect = QRectF(0, 0, width, height)
        text_rect.moveRight(text_rect.right() + 50)
        text_rect.moveTop(text_rect.top() + 10)
        painter.drawText(text_rect, Qt.AlignCenter, f"{int(value)}%")

        # Draw additional text
        font = QFont("Arial", 12, QFont.Bold)
        painter.setFont(font)
        painter.drawText(QRectF(0, height / 2 - 10, width, height / 2), Qt.AlignCenter, "\n\n")

        font.setPointSize(10)
        painter.setFont(font)
        painter.drawText(QRectF(0, height / 2 + 10, width, height / 2), Qt.AlignCenter, "v1.0.0")

class LoadingScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.progressBar = CircularProgressBar()
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(50)
        self.progress = 0


    def updateProgress(self):
        self.progress += 1
        if self.progress > 100:
            self.progress = 0
            self.hide()
            self.timer.stop()
            self.login = LoginWindow()
            self.login.show()
        self.progressBar.setValue(self.progress)

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        widget_geometry = self.frameGeometry()
        x = (screen_geometry.width() - widget_geometry.width()) // 2
        y = (screen_geometry.height() - widget_geometry.height()) // 2
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LoadingScreen()
    demo.show()
    demo.center()  # Center the window after showing it
    sys.exit(app.exec())

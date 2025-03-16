import requests
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QThread, Signal, Qt


class ImageDownloader(QThread):
    imageDownloaded = Signal(QPixmap)

    def __init__(self, url, width, height):
        super().__init__()
        self.url = url
        self.width = width
        self.height = height

    def run(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                image_data = response.content
                image = QImage.fromData(image_data)
                pixmap = QPixmap.fromImage(image).scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.imageDownloaded.emit(pixmap)
        except Exception as e:
            print(f"Error downloading image: {e}")

    


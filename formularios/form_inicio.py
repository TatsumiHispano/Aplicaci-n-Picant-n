import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QListWidget, QListWidgetItem, QStackedWidget, QScrollArea, QFrame
from PySide6.QtGui import QFont, QIcon, QPixmap, QPainter, QImage
from PySide6.QtCore import Qt, QSize
from util.util_image import ImageDownloader
from formularios.form_inicio_productos import RestaurantDetails
from util.util_scrollbar import ModernScrollBar
from formularios.form_map import restaurantmap

class picanton(QMainWindow):
    def __init__(self, id_usuario):
        super().__init__()
        self.id_usuario = id_usuario
        self.downloader_threads = []
        self.setWindowTitle("Picanton")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #ffffff;")


        self.stacked_widget = QStackedWidget()

        self.load_inicio()
        self.load_restaurants()

        self.setCentralWidget(self.stacked_widget)

        self.search_input.textChanged.connect(self.search_restaurants)
        self.results_list.setVerticalScrollBar(ModernScrollBar())

        self.results_list.setStyleSheet("""
        background-color: #ffffff; 
        border-radius: 0px; 
        padding: 0px;
    """)

        self.results_list.itemClicked.connect(self.open_restaurant_details)

    def load_inicio(self):

        # Si ya existe el widget de inicio, elimínalo
        if hasattr(self, 'central_widget'):
            self.stacked_widget.removeWidget(self.central_widget)
            
        self.inicio_layout = QVBoxLayout()

        self.header_layout = QHBoxLayout()
        self.header_layout.setAlignment(Qt.AlignCenter)

        # Crear un widget contenedor para el QHBoxLayout
        header_widget = QWidget()
        header_widget.setLayout(self.header_layout)

        # Aplicar el estilo al widget contenedor
        header_widget.setStyleSheet("background-color: #E5BF89; padding: 20px; border-radius: 0px;")

        # Ahora, puedes agregar el widget contenedor al layout principal
        self.inicio_layout.addWidget(header_widget)

        self.inicio_layout.setContentsMargins(0, 0, 0, 0)
        self.inicio_layout.setSpacing(20)

        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)

        self.location_label = QLabel("Picanton")
        self.location_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.location_label.setStyleSheet("margin-left: 20;")
        self.location_label.setAlignment(Qt.AlignCenter)
        self.header_layout.addWidget(self.location_label)

        self.inicio_layout.addLayout(self.header_layout)

        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Buscar")
        self.search_input.setStyleSheet("padding: 10px; border-radius: 15px;  background-color: #fff; margin-right: 165px; margin-left: 100px;")
        self.header_layout.addWidget(self.search_input)

        self.map = QPushButton()
        self.map.clicked.connect(self.open_restaurant_map)
        self.map.setIcon(QIcon('imagenes/map.png'))
        self.map.setIconSize(QSize(40,40))
        self.map.setStyleSheet("""
            QPushButton {
                border: none;
                margin: 5px;
                text-align: center;
            }
        """)
        self.header_layout.addWidget(self.map)

        self.filter_layout = QHBoxLayout()
        self.filter_layout.setAlignment(Qt.AlignCenter)
        self.inicio_layout.addLayout(self.filter_layout)

        self.add_filter_button("Todos", "imagenes/todo.png")
        self.add_filter_button("Italiano", "imagenes/italian.png")
        self.add_filter_button("Arabe", "imagenes/arabe.png")
        self.add_filter_button("Chino", "imagenes/china.png")
        self.add_filter_button("Americano", "imagenes/americana.png")
        self.add_filter_button("Mexicano", "imagenes/mexican.png")
        self.add_filter_button("Indio", "imagenes/indian.png")
        self.add_filter_button("Japones", "imagenes/japan.png")
        self.add_filter_button("Nacional", "imagenes/nacional.png")

        self.results_label = QLabel("Restaurantes:")
        self.results_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.results_label.setStyleSheet("padding: 10px; margin-right: 680px")
        self.results_label.setAlignment(Qt.AlignCenter)
        self.inicio_layout.addWidget(self.results_label)

        self.results_list = QListWidget(self)
        self.results_list.setStyleSheet("background-color: #ffffff; border-radius: 0px; padding: 10px;")
        self.inicio_layout.addWidget(self.results_list)

        self.conn = sqlite3.connect("tfg.db")
        self.cur = self.conn.cursor()

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.inicio_layout)

        self.stacked_widget.addWidget(self.central_widget)



    def add_filter_button(self, text, icon_path):
        button = QPushButton(self)
        button.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                border: none;
                margin: 5px;
                text-align: center;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
            QLabel {
                background-color: transparent;  /* Fondo transparente para QLabel */
            }
        """)
        button.clicked.connect(lambda: self.filter_restaurants_by_type(text.lower()))

        layout = QVBoxLayout()  # Layout vertical para contener la imagen y el texto
        

        icon_label = QLabel()
        pixmap = QPixmap(icon_path)
        pixmap = pixmap.scaledToHeight(55)  # Escalar la imagen a la altura deseada
        icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignCenter)  # Centrar la imagen horizontalmente
        layout.addWidget(icon_label)

        text_label = QLabel(text)
        text_label.setAlignment(Qt.AlignCenter)  # Centrar el texto horizontalmente
        layout.addWidget(text_label)

        button.setLayout(layout)  # Establecer el layout como el layout del botón
        button.setFixedSize(80, 80)  # Fijar tamaño del botón

        self.filter_layout.addWidget(button)  # Agregar el botón al layout principal




    def load_restaurants(self):
        # Vaciar la lista de restaurantes
        self.results_list.clear()

        self.cur.execute("SELECT id, nempresa, direccion, telefono, logo, descripcion, tipo, correo FROM Empresa")
        restaurants = self.cur.fetchall()
        for restaurant in restaurants:
            self.add_restaurant_to_list(*restaurant)



    def add_restaurant_to_list(self, idempresa, nempresa, direccion, telefono, logo_url, descripcion, tipo, correo):
        item = QListWidgetItem()
        item.setSizeHint(QSize(400, 250))

        widget = QWidget()
        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)

        layout_h = QHBoxLayout()
        layout_h.setAlignment(Qt.AlignCenter)  # Centrar la imagen horizontal y verticalmente
        layout_v1 = QVBoxLayout()
        layout_v2 = QVBoxLayout()
        layout_h.addLayout(layout_v1)
        layout_h.addLayout(layout_v2)

        layout_v1.setContentsMargins(100, 0, 100, 0)
        layout_v1.setSpacing(0)      

        layout_v2.setContentsMargins(100, 0, 100, 0)
        layout_v2.setSpacing(0)     

        # Crear el contenedor vertical para el QFrame de la imagen
        image_container_layout = QVBoxLayout()

        image_container = QFrame()  # Crear un contenedor para la imagen
        image_container.setFixedSize(470, 170)
        image_container.setObjectName("image_container")  # Establecer un nombre para identificarlo en el estilo
        image_container.setStyleSheet("background-color: white; border-radius: 10px;  margin: 0px; padding: 0px;")  # Aplicar estilo con bordes redondeados y sin márgenes ni relleno

        image_container_layout.addWidget(image_container, alignment=Qt.AlignCenter)
        layout_main.addLayout(image_container_layout)  # Agregar el contenedor al layout vertical
        


        image_layout = QVBoxLayout(image_container)  # Crear un layout para la imagen dentro del contenedor
        image_layout.setContentsMargins(0, 0, 0, 0)  # Establecer márgenes para el layout de la imagen a cero
        image_layout.setSpacing(0)  # Establecer espaciado cero

        image_container_layout.setContentsMargins(0, 0, 0, 0)  # Establecer márgenes para el QFrame de la imagen a cero
        image_container_layout.setSpacing(0)  # Establecer espaciado cero


        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)  # Centrar la imagen horizontal y verticalmente
        image_layout.addWidget(image_label)  # Agregar la etiqueta de la imagen al layout de la imagen

        downloader = ImageDownloader(logo_url, 630, 630)  # Tamaño deseado máximo de la imagen
        downloader.imageDownloaded.connect(lambda pixmap: self.on_image_downloaded(pixmap, image_label))
        downloader.start()
        self.downloader_threads.append(downloader)

        self.cur.execute("SELECT AVG(vcomida), AVG(vservicio), AVG(vestablecimiento), AVG(vpresentacion) FROM Resenyas WHERE idempresa = ?" , (idempresa,))
        averages = self.cur.fetchone()  # Obtener la fila de resultados



        name_label = QLabel(nempresa)
        name_label.setFont(QFont("Arial", 16, QFont.Bold))
        name_label.setAlignment(Qt.AlignCenter)
        layout_v1.addWidget(name_label)

        distancia = QLabel("Localizacion")
        distancia.setFont(QFont("Arial", 8))
        distancia.setAlignment(Qt.AlignCenter)
        layout_v1.addWidget(distancia)

        tipo_label = QLabel(tipo)
        tipo_label.setFont(QFont("Arial", 8))
        tipo_label.setAlignment(Qt.AlignCenter)
        layout_v2.addWidget(tipo_label)

        valoracion = QLabel()
        # Verificar si la consulta devuelve resultados
        if averages[0] is not None:
            # Calcular la media global sumando todas las medias y dividiendo por el número de categorías
            global_average = sum(averages) / len(averages)

            # Mostrar la media global en el QLabel
            valoracion.setText(f"Valoración: {global_average:.2f} / 5")
        else:
            # Si no hay reseñas para esta empresa, mostrar un mensaje indicando que no hay datos
            valoracion.setText(f"No hay valoraciones de {nempresa}")

        valoracion.setFont(QFont("Arial", 8))
        valoracion.setAlignment(Qt.AlignCenter)
        layout_v2.addWidget(valoracion)


        layout_main.addLayout(layout_h)

        layout_main.addStretch(1)
        widget.setLayout(layout_main)
        widget.setStyleSheet("""
            QWidget#restaurant_container {
                background-color: #fff;
            }
            QLabel {
                background-color: transparent;
                border: none;
            }
        """)
        widget.setObjectName("restaurant_container")

        item.setData(Qt.UserRole, {
            'idempresa': idempresa,
            'nempresa': nempresa,
            'direccion': direccion,
            'telefono': telefono,
            'logo': logo_url,
            'descripcion': descripcion,
            'tipo': tipo,
            'correo': correo
        })

        self.results_list.addItem(item)
        self.results_list.setItemWidget(item, widget)

    
    def on_image_downloaded(self, pixmap, image_label):
        try:
            # Escalar la imagen manteniendo el aspecto original
            pixmap_resized = pixmap.scaledToWidth(630)  # Cambia el ancho máximo a 300 (o el valor que desees)
            
            # Aplicar bordes redondeados después de escalar la imagen
            rounded_pixmap = self.apply_rounded_corners(pixmap_resized, 30)  # 70 es el radio para los bordes redondeados
            
            # Establecer la imagen en el QLabel y permitir que se ajuste al contenido
            image_label.setPixmap(rounded_pixmap)
            image_label.setScaledContents(True)
            
        except:
            pass


    def apply_rounded_corners(self, pixmap, radius):
        # Convertir el QPixmap a QImage para poder aplicar bordes redondeados
        image = pixmap.toImage()
        
        # Crear una máscara de bordes redondeados
        rounded_image = QImage(pixmap.size(), QImage.Format_ARGB32)
        rounded_image.fill(Qt.transparent)
        painter = QPainter(rounded_image)
        painter.setRenderHint(QPainter.Antialiasing)  # Habilitar el suavizado de bordes
        painter.setBrush(Qt.white)
        painter.setPen(Qt.transparent)
        painter.drawRoundedRect(rounded_image.rect(), radius, radius)  # Dibujar un rectángulo redondeado con el radio especificado
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.drawImage(0, 0, image)  # Dibujar el pixmap original con la composición SourceIn
        painter.end()

        # Convertir la imagen a QPixmap
        rounded_pixmap = QPixmap.fromImage(rounded_image)
        return rounded_pixmap







    def filter_restaurants_by_type(self, selected_cuisine):
        self.results_list.clear()
        if selected_cuisine == "todos":
            self.load_restaurants()
        else:
            self.cur.execute("SELECT id, nempresa, direccion, telefono, logo, descripcion, tipo, correo FROM Empresa WHERE LOWER(tipo) = ?", (selected_cuisine,))
            restaurants = self.cur.fetchall()
            for restaurant in restaurants:
                self.add_restaurant_to_list(*restaurant)

    def search_restaurants(self):
        search_text = self.search_input.text().strip().lower()
        self.results_list.clear()
        if not search_text:
            self.load_restaurants()
        else:
            self.cur.execute("SELECT id, nempresa, direccion, telefono, logo, descripcion, tipo, correo FROM Empresa WHERE LOWER(nempresa) LIKE ?", ('%' + search_text + '%',))
            restaurants = self.cur.fetchall()
            for restaurant in restaurants:
                self.add_restaurant_to_list(*restaurant)


    def open_restaurant_details(self, item):

        # Remover widgets, pero sin pasar de los límites
        for i in range(1, self.stacked_widget.count()):
            if i == 0:
                pass
            else:
                widget = self.stacked_widget.widget(i)
                self.stacked_widget.removeWidget(widget)
                widget.deleteLater()


        restaurant_info = item.data(Qt.UserRole)

        self.details_window = RestaurantDetails(self.id_usuario, restaurant_info)
        self.details_window.volver_button.clicked.connect(self.return_to_inicio)

        self.stacked_widget.addWidget(self.details_window)


        self.stacked_widget.setCurrentIndex(1)

    def open_restaurant_map(self):

        # Remover widgets, pero sin pasar de los límites
        for i in range(1, self.stacked_widget.count()):
            if i == 0:
                pass
            else:
                widget = self.stacked_widget.widget(i)
                self.stacked_widget.removeWidget(widget)
                widget.deleteLater()



        map_window = restaurantmap(self.id_usuario)
        map_window.volver_button.clicked.connect(self.return_to_inicio)

        self.stacked_widget.addWidget(map_window)


        self.stacked_widget.setCurrentIndex(1)

    def closeEvent(self, event):
        for thread in self.downloader_threads:
            thread.quit()
            thread.wait()
        self.conn.close()
        event.accept()

    def detener_descargas(self):
        for thread in self.downloader_threads:
            thread.quit()
            thread.wait()
        self.downloader_threads = []

    def return_to_inicio(self):
        self.stacked_widget.setCurrentIndex(0)
        self.load_restaurants()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = picanton()
    window.show()
    sys.exit(app.exec())

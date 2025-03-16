from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSpinBox, QTextEdit, QHBoxLayout, QGridLayout
from PySide6.QtGui import QFont, QColor, QPalette,QPainter, QImage, QPixmap, QIcon
from PySide6.QtCore import Qt, QSize
from util.util_scrollarea import CustomScrollArea
from util.util_image import ImageDownloader
from util.util_volver import RoundButton
import sqlite3


class RestaurantDetails(QWidget):
    def __init__(self, id_usuario, restaurant_info):
        super().__init__()
        self.downloader_threads = []
        self.id_usuario = id_usuario
        self.restaurant_info = restaurant_info
        self.reviews = []
        self.current_page = 0
        self.init_ui()
        self.downloaded_images = []


    def init_ui(self):
        scroll_area = CustomScrollArea()
        scroll_area.setWidgetResizable(True)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(scroll_area)
        self.setGeometry(100, 100, 800, 600)
        self.layout().setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.layout().setSpacing(0)  # Remove spacing
        self.layout().setAlignment(Qt.AlignCenter)

        # Text color
        self.text_color = "#333333"

        content_widget = QWidget()
        scroll_area.setWidget(content_widget)
        scroll_area.setAlignment(Qt.AlignCenter)

        main_layout = QVBoxLayout(content_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)

        layout_i = QVBoxLayout()
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 0, 25, 50)
        layout.setSpacing(20)

        main_layout.addLayout(layout_i)
        main_layout.addLayout(layout)

        # Set background color and rounded corners
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f5f5f5"))
        content_widget.setPalette(palette)
        content_widget.setAutoFillBackground(True)
        content_widget.setStyleSheet("border-radius: 45x; background-color: #f5f5f5; padding: 0px;")

        # Header
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_widget.setFixedHeight(100)
        header_widget.setStyleSheet("background-color: #E5BF89; padding: 10px; border-radius: 0px;")

        header_layout.setContentsMargins(30, 0, 0, 0)  # Remove margins
        header_layout.setSpacing(0)  # Remove spacing

        # Ajustar el tamaño de los botones y los iconos
        icon_size = QSize(16, 17)  

        self.volver_button = RoundButton()
        self.volver_button.setIcon(QIcon("./imagenes/volver.png"))
        self.volver_button.setStyleSheet("QPushButton {background-color: white; border-radius: 15px; border: none; color: white; font-family: FontAwesome; font-size: 16px; padding: 5px 10px;} QPushButton:hover {background-color: #218838;}")   # Personalizar estilo del botón
        self.volver_button.setIconSize(icon_size)  # Establecer el tamaño del icono
        header_layout.addWidget(self.volver_button)


        header_label = QLabel("Detalles del Restaurante", self)
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("color: #333; margin-right: 50px")

        header_layout.addWidget(header_label)
        layout_i.addWidget(header_widget)

        



        # Add empresa info
        self.info_empresa(layout)

        # Add products section
        self.load_products(layout)

        # Add reviews section
        self.calculate_global_rating(layout)
        self.send_resenyas(layout)
        self.resenyas(layout)
        self.load_reviews()

    def volver(self):
        self.detener_descargas()  # Detener todas las descargas en curso si las hay

        # Ocultar la ventana actual
        self.hide()

        # Mostrar la ventana anterior en el stack
        self.parentWidget().setCurrentIndex(self.parentWidget().currentIndex() - 1)


    def info_empresa(self, layout):
        container_widget_info = QWidget()
        container_widget_info.setStyleSheet("background-color: #ffffff; border-top-right-radius: 45px;  border-top-left-radius: 15px; border-bottom-left-radius: 45px; border-bottom-right-radius: 15px; padding-left: 25px; padding-right: 25px; padding-top: 5px; padding-bottom: 5px; ")

        layout_vertical_main = QVBoxLayout(container_widget_info)
        
        layout_horizontal = QHBoxLayout()
        layout_vertical1 = QVBoxLayout()
        layout_vertical2 = QVBoxLayout()

        # Title
        self.details_title_label = QLabel(self.restaurant_info['nempresa'], self)
        self.details_title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.details_title_label.setAlignment(Qt.AlignCenter)
        self.details_title_label.setStyleSheet("margin-top: 20px; margin-bottom: 20px; color: #333;")
        layout_vertical_main.addWidget(self.details_title_label)

        # Address
        self.details_address_label = QLabel(f"Dirección: {self.restaurant_info['direccion']}", self)
        self.details_address_label.setFont(QFont("Arial", 14))
        self.details_address_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical2.addWidget(self.details_address_label)

        # Phone
        self.details_phone_label = QLabel(f"Teléfono: {self.restaurant_info['telefono']}", self)
        self.details_phone_label.setFont(QFont("Arial", 14))
        self.details_phone_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical1.addWidget(self.details_phone_label)

        # Description
        self.details_description_label = QLabel(f"Descripción: {self.restaurant_info['descripcion']}", self)
        self.details_description_label.setFont(QFont("Arial", 14))
        self.details_description_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical2.addWidget(self.details_description_label)

        # Cuisine type
        self.details_cuisine_label = QLabel(f"Tipo: {self.restaurant_info['tipo']}", self)
        self.details_cuisine_label.setFont(QFont("Arial", 14))
        self.details_cuisine_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical1.addWidget(self.details_cuisine_label)

        # Email
        self.details_email_label = QLabel(f"Correo: {self.restaurant_info['correo']}", self)
        self.details_email_label.setFont(QFont("Arial", 14))
        self.details_email_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical1.addWidget(self.details_email_label)

        layout_horizontal.addLayout(layout_vertical1)
        layout_horizontal.addLayout(layout_vertical2)
        layout_vertical_main.addLayout(layout_horizontal)

        layout.addWidget(container_widget_info)

    def send_resenyas(self, layout):
        self.toggle_review_button = QPushButton("Escribir reseña", self)
        self.toggle_review_button.setStyleSheet("background-color: #E5BF89; color: #fff; border-radius: 5px; padding: 10px;")
        self.toggle_review_button.clicked.connect(self.toggle_review_area)
        layout.addWidget(self.toggle_review_button)
        
        self.review_title_label = QLabel("Escribe tu reseña:", self)
        self.review_title_label.setFont(QFont("Arial", 16))
        self.review_title_label.setStyleSheet(f"color: {self.text_color}; margin-top: 20px;")
        layout.addWidget(self.review_title_label)

        spinbox_style = """
            QSpinBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                margin-bottom: 10px;
            }
        """
        textedit_style = """
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                margin-bottom: 10px;
            }
        """

        self.comida_label = QLabel("Comida:", self)
        layout.addWidget(self.comida_label)
        self.comida_spinbox = QSpinBox()
        self.comida_spinbox.setStyleSheet(spinbox_style)
        layout.addWidget(self.comida_spinbox)

        self.servicio_label = QLabel("Servicio:", self)
        layout.addWidget(self.servicio_label)
        self.servicio_spinbox = QSpinBox()
        self.servicio_spinbox.setStyleSheet(spinbox_style)
        layout.addWidget(self.servicio_spinbox)

        self.establecimiento_label = QLabel("Establecimiento:", self)
        layout.addWidget(self.establecimiento_label)
        self.establecimiento_spinbox = QSpinBox()
        self.establecimiento_spinbox.setStyleSheet(spinbox_style)
        layout.addWidget(self.establecimiento_spinbox)

        self.presentacion_label = QLabel("Presentación:", self)
        layout.addWidget(self.presentacion_label)
        self.presentacion_spinbox = QSpinBox()
        self.presentacion_spinbox.setStyleSheet(spinbox_style)
        layout.addWidget(self.presentacion_spinbox)

        self.review_text_edit = QTextEdit(self)
        self.review_text_edit.setStyleSheet(textedit_style)
        layout.addWidget(self.review_text_edit)

        self.submit_button = QPushButton("Enviar reseña", self)
        self.submit_button.setStyleSheet("background-color: #E5BF89; color: #fff; border-radius: 5px; padding: 10px;")
        self.submit_button.clicked.connect(self.submit_review)
        layout.addWidget(self.submit_button)

        self.review_area_visible = False
        self.review_title_label.setVisible(False)
        self.comida_label.setVisible(False)
        self.comida_spinbox.setVisible(False)
        self.servicio_label.setVisible(False)
        self.servicio_spinbox.setVisible(False)
        self.establecimiento_label.setVisible(False)
        self.establecimiento_spinbox.setVisible(False)
        self.presentacion_label.setVisible(False)
        self.presentacion_spinbox.setVisible(False)
        self.review_text_edit.setVisible(False)
        self.submit_button.setVisible(False)

    def toggle_review_area(self):
        self.review_area_visible = not self.review_area_visible
        self.review_title_label.setVisible(self.review_area_visible)
        self.comida_label.setVisible(self.review_area_visible)
        self.comida_spinbox.setVisible(self.review_area_visible)
        self.servicio_label.setVisible(self.review_area_visible)
        self.servicio_spinbox.setVisible(self.review_area_visible)
        self.establecimiento_label.setVisible(self.review_area_visible)
        self.establecimiento_spinbox.setVisible(self.review_area_visible)
        self.presentacion_label.setVisible(self.review_area_visible)
        self.presentacion_spinbox.setVisible(self.review_area_visible)
        self.review_text_edit.setVisible(self.review_area_visible)
        self.submit_button.setVisible(self.review_area_visible)

    def load_products(self, layout):
        conn = sqlite3.connect("tfg.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM Productos WHERE idempresa = ?", (self.restaurant_info['idempresa'],))
        products = cur.fetchall()
        conn.close()

        if products:
            product_title_label = QLabel("Productos disponibles:", self)
            product_title_label.setFont(QFont("Arial", 16))
            product_title_label.setStyleSheet(f"color: {self.text_color}; margin-top: 20px;")
            layout.addWidget(product_title_label)

            grid_layout = QGridLayout()
            grid_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
            grid_layout.setSpacing(0)  # Remove spacing

            for i, product in enumerate(products):
                row = i // 2
                col = i % 2

                product_widget = QWidget()
                product_widget.setStyleSheet("background-color: #ffffff; border-top-right-radius: 45px;  border-top-left-radius: 15px; border-bottom-left-radius: 45px; border-bottom-right-radius: 15px; padding-left: 15px; padding-right: 15px; padding-top: 8px; padding-bottom: 8px; margin-left: 15px; margin-right: 15px; margin-top: 5px; margin-bottom: 5px;")
                product_layout = QHBoxLayout(product_widget)
                vertical_l = QVBoxLayout()
                

                

                logo_url = product[5]
                
                product_img = QLabel()
                product_img.setFixedSize(150, 100)
                product_layout.addWidget(product_img)

                downloader = ImageDownloader(logo_url, 300, 300) 
                downloader.imageDownloaded.connect(lambda pixmap, img=product_img: self.on_image_downloaded(pixmap, img))
                downloader.start()
                self.downloader_threads.append(downloader)

                product_name_label = QLabel(f"Nombre: {product[2]}", self)
                product_name_label.setStyleSheet(f"color: {self.text_color}; background-color: transparent;")
                vertical_l.addWidget(product_name_label)

                product_description_label = QLabel(f"Descripción: {product[3]}", self)
                product_description_label.setStyleSheet(f"color: {self.text_color};  background-color: transparent;")
                vertical_l.addWidget(product_description_label)

                product_ingredients_label = QLabel(f"Ingredientes: {product[4]}", self)
                product_ingredients_label.setStyleSheet(f"color: {self.text_color}; background-color: transparent; ")
                vertical_l.addWidget(product_ingredients_label)

                product_layout.addLayout(vertical_l)
                grid_layout.addWidget(product_widget, row, col)

            layout.addLayout(grid_layout)

    
    def calculate_global_rating(self, layout):
        container_widget_rating = QWidget()
        container_widget_rating.setStyleSheet("background-color: #ffffff; border-top-right-radius: 45px;  border-top-left-radius: 15px; border-bottom-left-radius: 45px; border-bottom-right-radius: 15px; padding-left: 15px; padding-right: 15px; padding-top: 5px; padding-bottom: 5px; ")

        layout_vertical_main_rating = QVBoxLayout(container_widget_rating)
        layout_horizontal_rating = QHBoxLayout()
        layout_vertical_rating1 = QVBoxLayout()
        layout_vertical_rating2 = QVBoxLayout()
        layout_vertical_rating2.setAlignment(Qt.AlignRight)

        title_label_rating = QLabel("Reseñas del Restaurante")
        title_label_rating.setFont(QFont("Arial", 20, QFont.Bold))
        title_label_rating.setAlignment(Qt.AlignCenter)
        title_label_rating.setStyleSheet("margin-top: 20px; margin-bottom: 20px; color: #333;")
        layout_vertical_main_rating.addWidget(title_label_rating)

        with sqlite3.connect('tfg.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT AVG(vcomida), AVG(vservicio), AVG(vestablecimiento), AVG(vpresentacion) FROM resenyas WHERE idempresa = ?",
                (self.restaurant_info['idempresa'],)
            )
            avg_ratings = cursor.fetchone()

        self.details_comida_label = QLabel(f"Comida: {avg_ratings[0]:.1f}" if avg_ratings[0] else "Comida: No hay reseñas")
        self.details_comida_label.setFont(QFont("Arial", 14))
        self.details_comida_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical_rating1.addWidget(self.details_comida_label)

        self.details_servicio_label = QLabel(f"Servicio: {avg_ratings[1]:.1f}" if avg_ratings[1] else "Servicio: No hay reseñas")
        self.details_servicio_label.setFont(QFont("Arial", 14))
        self.details_servicio_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical_rating1.addWidget(self.details_servicio_label)

        self.details_establecimiento_label = QLabel(f"Establecimiento: {avg_ratings[2]:.1f}" if avg_ratings[2] else "Establecimiento: No hay reseñas")
        self.details_establecimiento_label.setFont(QFont("Arial", 14))
        self.details_establecimiento_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical_rating2.addWidget(self.details_establecimiento_label)

        self.details_presentacion_label = QLabel(f"Presentación: {avg_ratings[3]:.1f}" if avg_ratings[3] else "Presentación: No hay reseñas")
        self.details_presentacion_label.setFont(QFont("Arial", 14))
        self.details_presentacion_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
        layout_vertical_rating2.addWidget(self.details_presentacion_label)

        layout_horizontal_rating.addLayout(layout_vertical_rating1)
        layout_horizontal_rating.addLayout(layout_vertical_rating2)
        layout_vertical_main_rating.addLayout(layout_horizontal_rating)

        layout.addWidget(container_widget_rating)

    def resenyas(self, layout):
        self.reviews_layout = QVBoxLayout()
        layout.addLayout(self.reviews_layout)

    def load_reviews(self):
        with sqlite3.connect('tfg.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT u.nusuario, r.vcomida, r.vservicio, r.vestablecimiento, r.vpresentacion, r.vcomentario, u.foto "
                "FROM Resenyas r JOIN Usuarios u ON r.id_autor = u.id "
                "WHERE r.idempresa = ?",
                (self.restaurant_info['idempresa'],)
            )
            reviews = cursor.fetchall()

        for i, review in enumerate(reviews):
            review_widget = QWidget()
            review_layout = QHBoxLayout(review_widget)
            review_widget.setStyleSheet("background-color: #ffffff; border-radius: 15px; padding: 10px; margin-bottom: 20px;")

            main = QHBoxLayout(review_widget)
            vertical1 = QVBoxLayout()
            vertical2 = QVBoxLayout()
            horizotal = QHBoxLayout()
            main.addLayout(vertical1)
            main.addLayout(vertical2)
            vertical2.addLayout(horizotal)
            
            # Usar la imagen descargada desde la lista
            logo_url = review[6]
            user_img = QLabel()
            user_img.setFixedSize(125, 100)
            user_img.setAlignment(Qt.AlignTop)
            user_img.setStyleSheet("margin-left: 10px")
            downloader = ImageDownloader(logo_url, 300, 300)
            downloader.imageDownloaded.connect(lambda pixmap, img=user_img: self.on_image_downloaded(pixmap, img))
            downloader.start()
            self.downloader_threads.append(downloader)

            vertical1.addWidget(user_img)




            user_label = QLabel(f"Usuario: {review[0]}")
            user_label.setFont(QFont("Arial", 14, QFont.Bold))
            user_label.setStyleSheet(f"color: {self.text_color};")
            user_label.setAlignment(Qt.AlignTop)
            vertical1.addWidget(user_label)

            comida_label = QLabel(f"Comida: {review[1]}")
            comida_label.setFont(QFont("Arial", 14))
            comida_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
            horizotal.addWidget(comida_label)

            servicio_label = QLabel(f"Servicio: {review[2]}")
            servicio_label.setFont(QFont("Arial", 14))
            servicio_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
            horizotal.addWidget(servicio_label)

            establecimiento_label = QLabel(f"Establecimiento: {review[3]}")
            establecimiento_label.setFont(QFont("Arial", 14))
            establecimiento_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
            horizotal.addWidget(establecimiento_label)

            presentacion_label = QLabel(f"Presentación: {review[4]}")
            presentacion_label.setFont(QFont("Arial", 14))
            presentacion_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
            horizotal.addWidget(presentacion_label)

            comentario_label = QLabel(f"Comentario: {review[5]}")
            comentario_label.setFont(QFont("Arial", 14))
            comentario_label.setStyleSheet(f"color: {self.text_color}; margin-bottom: 10px;")
            vertical2.addWidget(comentario_label)

            
            review_layout.addLayout(main)
            self.reviews_layout.addWidget(review_widget)

    def on_image_downloaded(self, pixmap, user_img):
            try:
                # Escalar la imagen manteniendo el aspecto original
                pixmap_resized = pixmap.scaledToWidth(300)  # Cambia el ancho máximo a 300 (o el valor que desees)
                
                # Aplicar bordes redondeados después de escalar la imagen
                rounded_pixmap = self.apply_rounded_corners(pixmap_resized, 30)  # 70 es el radio para los bordes redondeados

                # Agregar la imagen descargada a la lista
                self.downloaded_images.append(rounded_pixmap)
                
                # Establecer la imagen en el QLabel y permitir que se ajuste al contenido
                user_img.setPixmap(rounded_pixmap)
                user_img.setScaledContents(True)
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

    def submit_review(self):
        comida = self.comida_spinbox.value()
        servicio = self.servicio_spinbox.value()
        establecimiento = self.establecimiento_spinbox.value()
        presentacion = self.presentacion_spinbox.value()
        comentario = self.review_text_edit.toPlainText()

        with sqlite3.connect('tfg.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO resenyas (idempresa, id_autor, vcomida, vservicio, vestablecimiento, vpresentacion, vcomentario) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (self.restaurant_info['idempresa'], self.id_usuario, comida, servicio, establecimiento, presentacion, comentario)
            )
            conn.commit()

        # Clear the review form after submission
        self.comida_spinbox.setValue(0)
        self.servicio_spinbox.setValue(0)
        self.establecimiento_spinbox.setValue(0)
        self.presentacion_spinbox.setValue(0)
        self.review_text_edit.clear()

        # Reload the reviews to show the new one
        for i in reversed(range(self.reviews_layout.count())):
            widget_to_remove = self.reviews_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)
        self.load_reviews()

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

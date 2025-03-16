import sys
from PySide6.QtCore import Qt, QPoint, QSize, Signal, QPropertyAnimation, QEasingCurve, QTimer, QCoreApplication
from PySide6.QtGui import QFont, QIcon, QPixmap, QPainter, QBrush, QMovie
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy
)
import sqlite3, requests

# Importación de los colores desde el archivo config
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_ajustes import FormularioAjustesDesign
from formularios.form_usuario import UsuarioFormulario
from formularios.form_menu_empresa import MenuEmpresa
from formularios.form_adminmenu import MenuAdmin
from formularios.form_inicio import picanton
from util.util_roundbutton import RoundButton
from util.util_clickablelabel import ClickableLabel

class FormularioMaestroDesign(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.logo = QPixmap("./imagenes/logo.png")
        self.perfil = QPixmap("./imagenes/default_avatar.png")
        self.img_sitio_construccion = QPixmap("./imagenes/sitio_construccion.png")
        self.setWindowTitle("Picanton")
        self.setWindowIcon(QIcon("./imagenes/logo.ico"))
        self.resize(1324, 750)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Establecer ventana sin marco
        self.setAttribute(Qt.WA_TranslucentBackground)  # Hacer el fondo de la ventana transparente

        # Variables de estado para controlar el estado del GIF y el botón

        self.gif_running = False
        self.stop_at_half = False

        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

        self.draggable = False
        self.old_pos = QPoint()

        self.botones_menu = []  # Lista para almacenar los botones del menú lateral
        self.boton_actual = None  # Para almacenar el botón actualmente activo

        



    def config_window(self):
        self.setStyleSheet("border-radius: 10px;")

    def paneles(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)

        self.layout_barra_superior = QHBoxLayout()
        self.layout_menu_cuerpo = QHBoxLayout()

        self.central_layout.addLayout(self.layout_barra_superior)
        self.central_layout.addLayout(self.layout_menu_cuerpo)

        self.barra_superior = QWidget()
        self.barra_superior.setStyleSheet(f"background-color: {COLOR_BARRA_SUPERIOR}; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        self.barra_superior.setFixedHeight(50)

        self.menu_lateral = QWidget()
        self.menu_lateral.setStyleSheet(f"background-color: {COLOR_MENU_LATERAL}; border-top-left-radius: 0px; border-bottom-left-radius: 10px; border-top-right-radius: 0px; border-bottom-right-radius: 0px; ")
        size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.menu_lateral.setSizePolicy(size_policy)
        self.menu_lateral.setFixedWidth(55)
        self.menu_lateral.setContentsMargins(0, 0, 0, 0)

        self.cuerpo_principal = QWidget()
        self.cuerpo_principal.setStyleSheet(f"background-color: {COLOR_CUERPO_PRINCIPAL}; border-top-right-radius: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.cuerpo_principal.setMinimumSize(250, 150)
        self.cuerpo_principal.setContentsMargins(0, 0, 0, 0)

        # Ajustar el margen izquierdo del cuerpo principal
        self.central_layout.setContentsMargins(0, 0, 0, 0)  # Margen izquierdo negativo
        self.central_layout.setSpacing(0)

        self.layout_barra_superior.addWidget(self.barra_superior)

        self.layout_menu_cuerpo.addWidget(self.menu_lateral)  # Añade la barra lateral primero
        self.layout_menu_cuerpo.addWidget(self.cuerpo_principal)  # Luego añade el cuerpo principal
        self.layout_menu_cuerpo.setContentsMargins(0, 0, 0, 0)
        self.layout_menu_cuerpo.setSpacing(0)

    def controles_barra_superior(self):
        layout_barra_superior = QHBoxLayout(self.barra_superior)

        label_titulo = QLabel("Picanton")
        label_titulo.setStyleSheet("color: white;")
        label_titulo.setFont(QFont("Roboto", 15))
        layout_barra_superior.addWidget(label_titulo)

        label_menu_lateral = ClickableLabel()
        movie = QMovie("./imagenes/menu.gif")
        movie.setScaledSize(QSize(25, 25))  # Ajustar el tamaño del GIF
        label_menu_lateral.setMovie(movie)
        movie.start()
        label_menu_lateral.setMaximumSize(QSize(25, 25))  # Ajustar tamaño máximo
        layout_barra_superior.addWidget(label_menu_lateral)

        layout_barra_superior.addStretch()  # Añadir espacio para alinear los botones a la derecha

        label_info = QLabel("servicio@picanton.es")
        label_info.setStyleSheet("color: white; margin-right: 10px;")
        label_info.setFont(QFont("Roboto", 10))
        layout_barra_superior.addWidget(label_info)

        # Ajustar el tamaño de los botones y los iconos
        icon_size = QSize(8, 8)  # Tamaño del icono

        button_minimizar = RoundButton()
        button_minimizar.setIcon(QIcon("./imagenes/minimizar.png"))
        button_minimizar.setStyleSheet("QPushButton {background-color: #28a745; border-radius: 15px; border: none; color: white; font-family: FontAwesome; font-size: 16px; padding: 5px 10px;} QPushButton:hover {background-color: #218838;}")   # Personalizar estilo del botón
        button_minimizar.setIconSize(icon_size)  # Establecer el tamaño del icono
        button_minimizar.clicked.connect(self.showMinimized)
        layout_barra_superior.addWidget(button_minimizar)

        button_maximizar = RoundButton()
        button_maximizar.setIcon(QIcon("./imagenes/maximizar.png"))
        button_maximizar.setStyleSheet("QPushButton {background-color: #007bff; border-radius: 15px; border: none; color: white; font-family: FontAwesome; font-size: 16px; padding: 5px 10px;} QPushButton:hover {background-color: #0056b3;}")   # Personalizar estilo del botón
        button_maximizar.setIconSize(icon_size)  # Establecer el tamaño del icono
        button_maximizar.clicked.connect(self.toggleMaximized)
        layout_barra_superior.addWidget(button_maximizar)

        button_cerrar = RoundButton()  # Icono de x
        button_cerrar.setIcon(QIcon("./imagenes/cerrar.png"))      
        button_cerrar.setStyleSheet("QPushButton {background-color: #dc3545; border-radius: 15px; border: none; color: white; font-family: FontAwesome; font-size: 16px; padding: 5px 10px;} QPushButton:hover {background-color: #830000;}") # Personalizar estilo del botón
        button_cerrar.setIconSize(icon_size)  # Establecer el tamaño del icono
        button_cerrar.clicked.connect(self.close)
        layout_barra_superior.addWidget(button_cerrar)

        self.barra_superior.mouseMoveEvent = self.mouseMoveEvent
        self.barra_superior.mousePressEvent = self.mousePressEvent
        self.barra_superior.mouseReleaseEvent = self.mouseReleaseEvent

        self.maximizado = False

    def toggleMaximized(self):
        if self.isMaximized():
            self.showNormal()
            self.maximizado = False
        else:
            self.showMaximized()
            self.maximizado = True

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.draggable = True
            self.old_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.draggable:
            if self.maximizado == False:
                delta = event.pos() - self.old_pos
                self.move(self.pos() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False


    def controles_menu_lateral(self):
        self.botones_menu = []  # Inicialización de la lista de botones del menú lateral
        self.boton_actual = None  # Para almacenar el botón actualmente activo
        self.layout_menu_lateral = QVBoxLayout(self.menu_lateral)
        

        buttons_info = [
            ("Inicio", "🌶", self.abrir_panel_inicial),
            ("Perfil", "👤", self.abrir_panel_usuario),
            ("Ajustes", "🔧", self.abrir_panel_ajustes),
            ("Info", "🔍", self.abrir_panel_info)
        ]

        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT permisos FROM Usuarios WHERE id=?", (self.user_id,))
        permisos = cursor.fetchone()[0]

        if permisos == "empresa":
            buttons_info.insert(2, ("Empresa", "💼", self.abrir_panel_empresa))

        if permisos == "admin":
            buttons_info.insert(2, ("Empresa", "💼", self.abrir_panel_empresa))
            buttons_info.insert(6, ("Administracion", "💻", self.abrir_panel_admin))

        cursor.execute("SELECT foto FROM Usuarios WHERE id=?", (self.user_id,))
        self.logo_url = cursor.fetchone()[0]


        # Imagen de perfil
        try:
            response = requests.get(self.logo_url)
            if response.status_code == 200:
                image_data = response.content
                self.pixmap = QPixmap()
                self.pixmap.loadFromData(image_data)

                self.image_label = QLabel()

                self.pixmap = self.pixmap.scaled(30, 30)  
                self.image_label.setPixmap(self.pixmap)
                

                self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.image_label.setContentsMargins(0, 0, 0, 0)
                self.image_label.setAlignment(Qt.AlignCenter)

                self.layout_menu_lateral.addWidget(self.image_label)
            else:
                 # Cargar la imagen desde el archivo
                image_path = "./imagenes/default_avatar.png"
                self.pixmap = QPixmap(image_path)

                if self.pixmap.isNull():
                    print("Error: No se pudo cargar la imagen.")
                    return

                # Crear una etiqueta para mostrar la imagen
                self.image_label = QLabel()
                self.pixmap = self.pixmap.scaled(30, 30)
                self.image_label.setPixmap(self.pixmap)
                self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.image_label.setContentsMargins(0, 0, 0, 0)
                self.image_label.setAlignment(Qt.AlignCenter)

                self.layout_menu_lateral.addWidget(self.image_label)
                
        except Exception as e:
            
            # Cargar la imagen desde el archivo
            image_path = "./imagenes/default_avatar.png"
            self.pixmap = QPixmap(image_path)

            if self.pixmap.isNull():
                print("Error: No se pudo cargar la imagen.")
                return

            # Crear una etiqueta para mostrar la imagen
            self.image_label = QLabel()
            self.pixmap = self.pixmap.scaled(30, 30)
            self.image_label.setPixmap(self.pixmap)
            self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.image_label.setContentsMargins(0, 0, 0, 0)
            self.image_label.setAlignment(Qt.AlignCenter)

            self.layout_menu_lateral.addWidget(self.image_label)


        # Creacion de boton gif menu

        self.label_menu = QLabel()
        self.movie = QMovie("./imagenes/menu-sb.gif")
        self.movie.setScaledSize(QSize(30, 30))
        self.movie.start()
        self.movie.stop()
        self.label_menu.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.label_menu.setAlignment(Qt.AlignCenter)
        self.label_menu.setMovie(self.movie)
        self.label_menu.mousePressEvent = lambda event: self.toggle_animation()  # Utiliza una función lambda para pasar self y el evento



        self.layout_menu_lateral.addWidget(self.label_menu)

        # Creacion de botones
        
        for text, icon, callback in buttons_info:
            button = QPushButton()
            button.setText(f"{icon} {text}")  # Añadimos el texto al icono
            button.setStyleSheet("""
                QPushButton {
                    color: #333; /* Color del texto */
                    font-family: FontAwesome;
                    border: none;
                    padding: 10px; /* Ajustar el tamaño del botón */
                    text-align: left;
                }
                QPushButton:hover {
                    color: #555; /* Color del texto al pasar el cursor */
                    background-color: rgba(50, 50, 50, 0.2); /* Color de fondo transparente al pasar el cursor */
                }
            """)
            button.clicked.connect(lambda button=button, cb=callback: self.click_menu_button(button, cb))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.layout_menu_lateral.addWidget(button)
            self.botones_menu.append(button)  # Agregar el botón a la lista

        self.button_cerrar_sesion = QPushButton()
        self.button_cerrar_sesion.setText("")
        self.button_cerrar_sesion.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: orange;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: darkorange;
            }
        """)
        self.button_cerrar_sesion.setIcon(QIcon("./imagenes/cerrar_s.png"))
        self.button_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.layout_menu_lateral.addWidget(self.button_cerrar_sesion)

        self.layout_menu_lateral.setSpacing(0)
        conexion.close()
        




    def toggle_animation(self):
        
        if self.menu_lateral.width() == 55:
            if not self.gif_running:
                # Si el GIF no está en ejecución, iniciar la animación
                self.movie.jumpToFrame(0)  # Saltar al primer frame
                self.movie.start()  # Iniciar la animación
                self.gif_running = True

                total_frames = self.movie.frameCount()
                half_frame = total_frames // 2

                # Crear un QTimer para controlar la animación
                self.animation_timer = QTimer()
                self.animation_timer.timeout.connect(self.update_animation)
                self.animation_timer.start(50)  # Actualizar cada 50 milisegundos

                self.target_frame = half_frame  # Establecer el frame objetivo en la mitad

        else:
            # Si la animación ya está en ejecución, continuar desde donde se detuvo
            # Si la animación se detuvo en la mitad, establecer el target_frame al último frame
            if self.menu_lateral.width() == 150:
                if self.movie.currentFrameNumber() >= self.target_frame:
                    self.target_frame = self.movie.frameCount() - 1  # Establecer el frame objetivo al final
                    
                    self.animation_timer.start(30)  # Actualizar cada 50 milisegundos
                    self.gif_running = False

        self.double_def()


    def update_animation(self):
        self.current_frame = self.movie.currentFrameNumber()
        if self.current_frame >= self.target_frame:
            # Si el frame actual es igual o mayor que el frame objetivo, detener la animación
            self.movie.stop()
            self.animation_timer.stop()  # Detener el QTimer
        else:
            # Si la animación no ha alcanzado el frame objetivo, actualizar el frame actual
            self.movie.jumpToNextFrame()
            self.repaint()  # Repintar la interfaz gráfica para mostrar el nuevo frame

    def double_def(self):
        try:
            self.modify_perfil()
        except Exception as e:
            print(f"Error downloading image: {e}")
            
        self.toggle_panel()
        

    def modify_perfil(self):

        if self.menu_lateral.width() == 55:  # Si el menú está contraído
            self.pixmap = self.pixmap.scaled(60, 60)
            self.button_cerrar_sesion.setText("Cerrar Sesión")
            self.image_label.setPixmap(self.pixmap)

        elif self.menu_lateral.width() == 150:  # Si el menú está expandido
            self.pixmap = self.pixmap.scaled(30, 30)
            self.button_cerrar_sesion.setText("")
            self.image_label.setPixmap(self.pixmap)




    def click_menu_button(self, button, callback):
        # Restaurar el estilo predeterminado del botón actualmente activo, si existe
        if self.boton_actual:
            self.boton_actual.setStyleSheet("""
                QPushButton {
                    color: #333; /* Color del texto */
                    font-family: FontAwesome;
                    border: none;
                    padding: 10px; /* Ajustar el tamaño del botón */
                    text-align: left;
                }
                QPushButton:hover {
                    color: #555; /* Color del texto al pasar el cursor */
                    background-color: rgba(50, 50, 50, 0.2); /* Color de fondo transparente al pasar el cursor */
                }
            """)

        # Establecer el nuevo botón como botón actual
        self.boton_actual = button

        # Cambiar el estilo del botón clicado
        button.setStyleSheet("""
            QPushButton {
                color: #fff; /* Cambiar el color del texto */
                font-family: FontAwesome;
                border: none;
                padding: 10px; /* Ajustar el tamaño del botón */
                text-align: left;
                background-color: rgba(50, 50, 50, 0.6); /* Cambiar el color de fondo */
            }
            QPushButton:hover {
                color: #555; /* Color del texto al pasar el cursor */
                background-color: rgba(50, 50, 50, 0.2); /* Color de fondo transparente al pasar el cursor */
            }
        """)

        # Llamar al callback asociado al botón
        callback()

    def controles_cuerpo(self):
        self.layout_cuerpo_principal = QVBoxLayout(self.cuerpo_principal)
        self.layout_cuerpo_principal.setContentsMargins(0, 0, 0, 0)
        self.layout_cuerpo_principal.setSpacing(0)

        label = QLabel()
        label.setPixmap(self.logo)
        label.setAlignment(Qt.AlignCenter)
        self.layout_cuerpo_principal.addWidget(label)


    def abrir_panel_ajustes(self):
        self.limpiar_panel(self.cuerpo_principal)
        formulario_ajustes = FormularioAjustesDesign(self)
        self.layout_cuerpo_principal.addWidget(formulario_ajustes)
        formulario_ajustes.show()

    def abrir_panel_usuario(self):
        # Limpiar el panel principal
        self.limpiar_panel(self.cuerpo_principal)
        
        # Crear una instancia del formulario de usuario
        formulario_usuario = UsuarioFormulario(self.user_id)
        
        # Agregar el formulario al layout del cuerpo principal
        self.layout_cuerpo_principal.addWidget(formulario_usuario)
        
        # Mostrar la ventana
        self.show()

    def abrir_panel_inicial(self):
        # Limpiar el panel principal
        self.limpiar_panel(self.cuerpo_principal)
        
        # Detener todos los hilos de descarga de imágenes en la instancia actual de picanton
        if hasattr(self, 'window_picanton'):
            self.window_picanton.detener_descargas()
        
        # Crear una nueva instancia del formulario de picanton
        self.window_picanton = picanton(self.user_id)
        
        # Agregar el formulario al layout del cuerpo principal
        self.layout_cuerpo_principal.addWidget(self.window_picanton)
        
        # Mostrar la ventana
        self.show()



    def abrir_panel_empresa(self):
        # Limpiar el panel principal
        self.limpiar_panel(self.cuerpo_principal)
        
        # Crear una instancia del formulario de usuario
        formulario_empresa = MenuEmpresa(self.user_id)
        
        # Agregar el formulario al layout del cuerpo principal
        self.layout_cuerpo_principal.addWidget(formulario_empresa)
        
        # Mostrar la ventana
        self.show()
    
    def abrir_panel_admin(self):
        # Limpiar el panel principal
        self.limpiar_panel(self.cuerpo_principal)
        
        # Crear una instancia del formulario de usuario
        formulario_admin = MenuAdmin()
        
        # Agregar el formulario al layout del cuerpo principal
        self.layout_cuerpo_principal.addWidget(formulario_admin)
        
        # Mostrar la ventana
        self.show()

    def abrir_panel_info(self):
        self.info = FormularioInfoDesign()
        self.info.show()

    def limpiar_panel(self, panel):
        for widget in panel.findChildren(QWidget):
            widget.deleteLater()

    def toggle_panel(self):
        
        if self.menu_lateral.width() == 55:  # Si el menú está contraído
            self.animate_menu(150)  # Expandir el menú con animación
        elif self.menu_lateral.width() == 150:  # Si el menú está expandido
            self.animate_menu(55)  # Contraer el menú con animación

        if self.menu_lateral.isVisible():
            self.cuerpo_principal.setStyleSheet(f"background-color: {COLOR_CUERPO_PRINCIPAL}; border-top-right-radius: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        else: 
            self.cuerpo_principal.setStyleSheet(f"background-color: {COLOR_CUERPO_PRINCIPAL}; border-top-right-radius: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")

    def animate_menu(self, widthExtended):
        width = self.menu_lateral.width()
        self.animation = QPropertyAnimation(self.menu_lateral, b"minimumWidth")
        self.animation.setDuration(1000)  # ms
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuint)
        self.animation.start()

    def cambiar_color_barra_superior(self, color):
        self.barra_superior.setStyleSheet(f"background-color: {color}; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px; border-top-left-radius: 10px; border-top-right-radius: 10px;")

    def cambiar_color_menu_lateral(self, color):
        self.menu_lateral.setStyleSheet(f"background-color: {color}; border-top-left-radius: 0px; border-bottom-left-radius: 10px; border-top-right-radius: 0px; border-bottom-right-radius: 0px; ")

    def cambiar_color_cuerpo_principal(self, color):
        self.cuerpo_principal.setStyleSheet(f"background-color: {color}; border-top-right-radius: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
    
    def cerrar_sesion(self):

        from formularios.ui_Login import LoginWindow
        
        self.hide()
        self.register_window = LoginWindow()
        self.register_window.show()

    def closeEvent(self, event):
        sys.exit()


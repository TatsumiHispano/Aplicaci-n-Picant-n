from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QColorDialog, QLabel, QSizePolicy
from PySide6.QtGui import QColor, QFont, Qt


class FormularioAjustesDesign(QMainWindow):
    def __init__(self, formulario_principal):
        super().__init__()
        self.formulario_principal = formulario_principal
        self.setWindowTitle("Ajustes")
        self.setMinimumSize(250, 150)

        # Crear el layout principal
        layout_principal = QVBoxLayout()
        layout_principal.setAlignment(Qt.AlignCenter)

        # Crear "islas" blancas para cada sección
        isla_barra_superior = self.crear_isla_blanca()
        isla_menu_lateral = self.crear_isla_blanca()
        isla_cuerpo_principal = self.crear_isla_blanca()

        # Layouts para las "islas" blancas
        layout_isla_barra_superior = QVBoxLayout(isla_barra_superior)
        layout_isla_menu_lateral = QVBoxLayout(isla_menu_lateral)
        layout_isla_cuerpo_principal = QVBoxLayout(isla_cuerpo_principal)

        # Crear etiquetas para los títulos de sección
        lbl_barra_superior = QLabel("Barra Superior")
        lbl_menu_lateral = QLabel("Menú Lateral")
        lbl_cuerpo_principal = QLabel("Cuerpo Principal")

        # Aplicar estilos a las etiquetas de título
        self.estilo_titulo(lbl_barra_superior)
        self.estilo_titulo(lbl_menu_lateral)
        self.estilo_titulo(lbl_cuerpo_principal)

        # Crear botones para cambiar colores
        btn_color_barra_superior = QPushButton("Cambiar Color")
        btn_color_menu_lateral = QPushButton("Cambiar Color")
        btn_color_cuerpo_principal = QPushButton("Cambiar Color")

        # Estilo para los botones de cambio de color
        self.estilo_boton(btn_color_barra_superior)
        self.estilo_boton(btn_color_menu_lateral)
        self.estilo_boton(btn_color_cuerpo_principal)

        # Conectar los botones a las funciones correspondientes
        btn_color_barra_superior.clicked.connect(self.cambiar_color_barra_superior)
        btn_color_menu_lateral.clicked.connect(self.cambiar_color_menu_lateral)
        btn_color_cuerpo_principal.clicked.connect(self.cambiar_color_cuerpo_principal)

        # Agregar elementos a las "islas" blancas
        layout_isla_barra_superior.addWidget(lbl_barra_superior, alignment=Qt.AlignCenter)
        layout_isla_barra_superior.addWidget(btn_color_barra_superior)
        layout_isla_menu_lateral.addWidget(lbl_menu_lateral, alignment=Qt.AlignCenter)
        layout_isla_menu_lateral.addWidget(btn_color_menu_lateral)
        layout_isla_cuerpo_principal.addWidget(lbl_cuerpo_principal, alignment=Qt.AlignCenter)
        layout_isla_cuerpo_principal.addWidget(btn_color_cuerpo_principal)

        # Agregar las "islas" blancas al layout principal
        layout_principal.addWidget(isla_barra_superior)
        layout_principal.addWidget(isla_menu_lateral)
        layout_principal.addWidget(isla_cuerpo_principal)

        # Configurar el widget central
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        # Hacer que los botones sean responsivos
        btn_color_barra_superior.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_color_menu_lateral.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_color_cuerpo_principal.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def estilo_titulo(self, label):
        label.setStyleSheet("font-weight: bold; font-size: 16px; margin-bottom: 5px;")

    def estilo_boton(self, button):
        button.setStyleSheet("padding: 0px; font-size: 14px; background-color: #E5BF89; color: white; border: none; border-radius: 5px;")

    def crear_isla_blanca(self):
        isla = QWidget()
        isla.setStyleSheet("background-color: white; border-radius: 10px; padding: 20px; margin-left: 20px; margin-right: 20px;")
        return isla
    
    def abrir_seleccion_color(self):
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()
        if color.isValid():
            return color.name()

    def cambiar_color_barra_superior(self):
        color = self.abrir_seleccion_color()
        if color:
            self.formulario_principal.cambiar_color_barra_superior(color)

    def cambiar_color_menu_lateral(self):
        color = self.abrir_seleccion_color()
        if color:
            self.formulario_principal.cambiar_color_menu_lateral(color)

    def cambiar_color_cuerpo_principal(self):
        color = self.abrir_seleccion_color()
        if color:
            self.formulario_principal.cambiar_color_cuerpo_principal(color)

    def cerrar_sesion(self):
        self.close()

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt
from formularios.form_empresa import EmpresaFormulario  
from formularios.form_productos import ProductoFormulario  

class MenuEmpresa(QMainWindow):
    def __init__(self, user_id):
        super().__init__()

        self.user_id = user_id

        # Configuración de la ventana principal
        self.setWindowTitle("Main Formulario")
        self.resize(300, 200)

        # Crear el layout principal
        layout = QVBoxLayout()
        

        # Crear titulo

        titulo = QLabel("Administración de Empresa")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 40px; font-weight: bold; color: #333333; padding: 0px;")

        # Crear los botones
        btn_admin_usuarios = QPushButton("Administrar datos empresa")
        btn_admin_usuarios.clicked.connect(self.abrir_admin_formulario_usuarios)
        self.estilo_boton(btn_admin_usuarios)

        btn_admin_empresas = QPushButton("Administrar productos empresa")
        btn_admin_empresas.clicked.connect(self.abrir_admin_formulario_empresas)
        self.estilo_boton(btn_admin_empresas)

        # Agregar los botones y titulo al layout principal
        layout.addWidget(titulo)
        layout.addWidget(btn_admin_usuarios)
        layout.addWidget(btn_admin_empresas)

        # Crear un widget para el formulario principal
        self.widget_principal = QWidget()
        self.widget_principal.setLayout(layout)
        

        # Crear un stacked widget para almacenar varios formularios
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.widget_principal)

        # Crear el formulario de administración de usuarios y agregarlo al stacked widget
        self.admin_formulario_usuarios = EmpresaFormulario(self.user_id)
        self.admin_formulario_usuarios.btn_volver.clicked.connect(self.volver_atras)
        self.stacked_widget.addWidget(self.admin_formulario_usuarios)

        # Crear el formulario de administración de empresas y agregarlo al stacked widget
        self.admin_formulario_empresas = ProductoFormulario(self.user_id)
        self.admin_formulario_empresas.btn_volver.clicked.connect(self.volver_atras)
        self.stacked_widget.addWidget(self.admin_formulario_empresas)

        # Establecer el stacked widget como el widget central
        self.setCentralWidget(self.stacked_widget)

        # Aplicar el diseño de ajustes a los colores de los elementos
        self.aplicar_diseno_ajustes()

    def estilo_boton(self, boton):
        boton.setStyleSheet("QPushButton {"
                            "background-color: #E5BF89;"
                            "border: none;"
                            "color: white;"
                            "padding: 10px 20px;"
                            "border-radius: 15px;"
                            "}"
                            "QPushButton:hover {"
                            "background-color: #C49F4E;"
                            "}")

    def abrir_admin_formulario_usuarios(self):
        # Cambiar al formulario de administración de usuarios
        self.stacked_widget.setCurrentIndex(1)

    def abrir_admin_formulario_empresas(self):
        # Cambiar al formulario de administración de empresas
        self.stacked_widget.setCurrentIndex(2)

    def volver_atras(self):
        # Regresar al formulario principal
        self.stacked_widget.setCurrentIndex(0)

    def aplicar_diseno_ajustes(self):
        # Colores de los elementos
        color_principal = "#FFFFFF"

        # Aplicar colores a los botones
        self.estilo_boton(self.admin_formulario_usuarios.btn_volver)
        self.estilo_boton(self.admin_formulario_empresas.btn_volver)

        # Aplicar colores al formulario principal
        self.widget_principal.setStyleSheet(f"background-color: {color_principal}; border-radius: 10px; padding: 20px; margin: 20px;")



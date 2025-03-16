import sys
from PySide6.QtWidgets import QApplication

# Importa las clases de la ventana de loadingscreen
from formularios.ui_Loadingbar import LoadingScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Crea e inicia la ventana de inicio de sesión
    window = LoadingScreen()
    window.show()
    window.center()
    
    sys.exit(app.exec())

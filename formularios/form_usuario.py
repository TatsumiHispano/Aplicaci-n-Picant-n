import sys
import sqlite3
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout
from PySide6.QtGui import QPixmap
from util.util_popup import CustomMessageBox



class UsuarioFormulario(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Datos de Usuario")
        self.resize(400, 500)

        # Crear el layout principal
        layout_principal = QVBoxLayout()

        # Crear una isla blanca para el formulario
        isla_formulario = crear_isla_blanca()

        # Crear un formulario para los datos del usuario
        form_layout = QFormLayout()
        form_layout.setVerticalSpacing(0)

        # Crear campos de entrada para cada atributo del usuario
        self.txt_nombre = QLineEdit()
        self.txt_papellido = QLineEdit()
        self.txt_sapellido = QLineEdit()
        self.txt_correo = QLineEdit()
        self.txt_telefono = QLineEdit()
        self.txt_direccion = QLineEdit()
        self.txt_contrasena = QLineEdit()
        self.txt_confirmar_contrasena = QLineEdit()
        self.txt_foto = QLineEdit()
        self.txt_longitud = QLineEdit()
        self.txt_latitud = QLineEdit()

        # Definir el estilo para los QLineEdit
        self.txt_nombre.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_papellido.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_sapellido.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_correo.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_telefono.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_direccion.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_contrasena.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_confirmar_contrasena.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_foto.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_longitud.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_latitud.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")

        # Agregar los campos al formulario
        form_layout.addRow("Nombre:", self.txt_nombre)
        form_layout.addRow("Primer Apellido:", self.txt_papellido)
        form_layout.addRow("Segundo Apellido:", self.txt_sapellido)
        form_layout.addRow("Correo:", self.txt_correo)
        form_layout.addRow("Teléfono:", self.txt_telefono)
        form_layout.addRow("Dirección:", self.txt_direccion)
        form_layout.addRow("Contraseña:", self.txt_contrasena)
        form_layout.addRow("Confirmar Contraseña:", self.txt_confirmar_contrasena)
        form_layout.addRow("Foto:", self.txt_foto)
        form_layout.addRow("Longitud:", self.txt_longitud)
        form_layout.addRow("Latitud:", self.txt_latitud)

        # Crear botones para guardar y cancelar cambios
        btn_guardar = QPushButton("Guardar")
        btn_guardar.setStyleSheet("background-color: #E5BF89; color: white; padding: 10px 24px; border: none; border-radius: 15px; margin-top: 15px; ")

        # Conectar los botones a las funciones correspondientes
        btn_guardar.clicked.connect(self.guardar_cambios)

        # Agregar el formulario y los botones al layout principal
        isla_formulario.setLayout(form_layout)
        layout_principal.addWidget(isla_formulario)
        layout_principal.addWidget(btn_guardar)

        # Crear un widget central y establecer el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        # Autocompletar los campos con la información del usuario
        self.autocompletar_campos()

    def autocompletar_campos(self):
        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()

        try:
            # Obtener los datos del usuario de la tabla Usuarios
            cursor.execute("SELECT * FROM Usuarios WHERE id=?", (self.user_id,))
            usuario = cursor.fetchone()

            # Autocompletar los campos del formulario con la información del usuario
            if usuario:
                self.txt_nombre.setText(str(usuario[2]))
                self.txt_papellido.setText(str(usuario[3]))
                self.txt_sapellido.setText(str(usuario[4]))
                self.txt_correo.setText(str(usuario[5]))
                self.txt_telefono.setText(str(usuario[6]))  # Convertir a cadena
                self.txt_direccion.setText(str(usuario[7]))
                # No autocompletar la contraseña ni la confirmación de contraseña por motivos de seguridad
                self.txt_foto.setText(str(usuario[10]))
                self.txt_longitud.setText(str(usuario[11]))
                self.txt_latitud.setText(str(usuario[12]))

        except sqlite3.Error as error:
            # Mostrar un mensaje de error en caso de que ocurra un problema al obtener los datos del usuario
            CustomMessageBox.critical(self, "Error", f"Error al obtener los datos del usuario de la base de datos: {error}")

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def guardar_cambios(self):
        # Obtener los valores de los campos de entrada
        nombre = self.txt_nombre.text()
        papellido = self.txt_papellido.text()
        sapellido = self.txt_sapellido.text()
        correo = self.txt_correo.text()
        telefono = self.txt_telefono.text()
        direccion = self.txt_direccion.text()
        contrasena = self.txt_contrasena.text()
        confirmar_contrasena = self.txt_confirmar_contrasena.text()
        foto = self.txt_foto.text()
        longitud = self.txt_longitud.text()
        latitud = self.txt_latitud.text()

        # Verificar si el teléfono tiene exactamente 9 dígitos y no contiene letras
        if telefono and not re.match(r'^\d{9}$', telefono):
            CustomMessageBox.warning(self, "Advertencia", "El teléfono debe tener exactamente 9 números y no debe contener letras.")
            return

        # Verificar si el correo contiene el símbolo '@'
        correo_valido = re.match(r'^.+@.+\..+$', correo)
        if correo and not correo_valido:
            CustomMessageBox.warning(self, "Advertencia", "El correo electrónico debe ser válido y contener el símbolo '@'. Por favor, inténtelo de nuevo.")
            return

        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()

        try:
            # Crear una lista de tuplas de campos y valores para actualizar
            campos_valores = []
            if nombre:
                campos_valores.append(('nombre', nombre))
            if papellido:
                campos_valores.append(('papellido', papellido))
            if sapellido:
                campos_valores.append(('sapellido', sapellido))
            if correo:
                campos_valores.append(('correo', correo))
            if telefono:
                campos_valores.append(('telefono', telefono))
            if direccion:
                campos_valores.append(('direccion', direccion))
            if contrasena:
                if contrasena != confirmar_contrasena:
                    CustomMessageBox.warning(self, "Advertencia", "Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")
                    return
                campos_valores.append(('contrasena', contrasena))
            if foto:
                campos_valores.append(('foto', foto))
            
            if longitud:
                campos_valores.append(('longitud', longitud))

            if latitud:
                campos_valores.append(('latitud', latitud))

            # Generar la sentencia SQL de actualización
            set_clause = ', '.join([f'{campo}=?' for campo, _ in campos_valores])

            # Actualizar los datos del usuario en la tabla Usuarios
            cursor.execute(f'UPDATE Usuarios SET {set_clause} WHERE id=?', [valor for _, valor in campos_valores] + [self.user_id])

            # Guardar los cambios en la base de datos
            conexion.commit()

            # Mostrar un mensaje de éxito
            CustomMessageBox.information(self, "Éxito", "Los datos del usuario se han actualizado correctamente.")

        except sqlite3.Error as error:
            # Mostrar un mensaje de error en caso de que ocurra un problema al guardar los datos
            CustomMessageBox.critical(self, "Error", f"Error al actualizar datos en la tabla Usuarios: {error}")

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

def crear_isla_blanca():
    isla = QWidget()
    isla.setStyleSheet("background-color: white; border-radius: 10px; padding: 20px; margin: 0px;")
    return isla

# Instanciar y ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = UsuarioFormulario(1)
    ventana.show()
    sys.exit(app.exec())

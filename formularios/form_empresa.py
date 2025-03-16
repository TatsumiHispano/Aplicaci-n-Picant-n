import sys
import sqlite3
import re  # Importar el módulo de expresiones regulares
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from util.util_popup import CustomMessageBox
import re, requests

def crear_isla_blanca():
    isla = QWidget()
    isla.setStyleSheet("background-color: white; border-radius: 10px; padding: 20px; margin: 0px;")
    return isla

class EmpresaFormulario(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Datos de Empresa")
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
        self.txt_correo = QLineEdit()
        self.txt_telefono = QLineEdit()
        self.txt_direccion = QLineEdit()
        self.txt_foto = QLineEdit()
        self.txt_descripcion = QLineEdit()
        self.txt_tipo = QLineEdit()
        self.txt_longitud = QLineEdit()
        self.txt_latitud = QLineEdit()

        # Definir el estilo para los QLineEdit
        self.txt_nombre.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_correo.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px;  margin-top: 13px")
        self.txt_telefono.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px;  margin-top: 13px")
        self.txt_direccion.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px;  margin-top: 13px")
        self.txt_foto.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px;  margin-top: 13px")
        self.txt_descripcion.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_tipo.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px;  margin-top: 13px")
        self.txt_longitud.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")
        self.txt_latitud.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")

        # Agregar los campos al formulario
        form_layout.addRow("Nombre de empresa:", self.txt_nombre)
        form_layout.addRow("Correo:", self.txt_correo)
        form_layout.addRow("Teléfono:", self.txt_telefono)
        form_layout.addRow("Dirección:", self.txt_direccion)
        form_layout.addRow("Descripcion:", self.txt_descripcion)
        form_layout.addRow("Tipo de empresa:", self.txt_tipo)
        form_layout.addRow("Logo de empresa:", self.txt_foto)
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

        self.btn_volver = QPushButton("Volver Atrás")
        self.btn_volver.setStyleSheet("background-color: #E5BF89; color: white; border: none; padding: 10px 20px; border-radius: 15px;")  # Estilo aplicado correctamente
        layout_principal.addWidget(self.btn_volver)
    

    def autocompletar_campos(self):
        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()

        try:
            # Obtener los datos del usuario de la tabla Usuarios
            cursor.execute("SELECT * FROM Empresa WHERE id_usuario=?", (self.user_id,))
            usuario = cursor.fetchone()

        
            # Autocompletar los campos del formulario con la información del usuario
            if usuario:
                self.txt_nombre.setText(str(usuario[1]))
                self.txt_descripcion.setText(str(usuario[6]))
                self.txt_tipo.setText(str(usuario[7]))
                self.txt_correo.setText(str(usuario[4]))
                self.txt_telefono.setText(str(usuario[3]))  # Convertir a cadena
                self.txt_direccion.setText(str(usuario[2]))
                self.txt_foto.setText(str(usuario[5]))
                self.txt_longitud.setText(str(usuario[9]))
                self.txt_latitud.setText(str(usuario[10]))

        except sqlite3.Error as error:
            # Mostrar un mensaje de error en caso de que ocurra un problema al obtener los datos del usuario
            CustomMessageBox.critical(self, "Error", f"Error al obtener los datos de la Empresa de la base de datos: {error}")

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def guardar_cambios(self):
        # Obtener los valores de los campos de entrada
        nombre = self.txt_nombre.text()
        descripcion = self.txt_descripcion.text()
        tipo = self.txt_tipo.text()
        correo = self.txt_correo.text()
        telefono = self.txt_telefono.text()
        direccion = self.txt_direccion.text()
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
            # Verificar si la empresa ya existe
            cursor.execute('SELECT COUNT(*) FROM Empresa WHERE id_usuario=?', (self.user_id,))
            existe_empresa = cursor.fetchone()[0]

            if existe_empresa:
                # La empresa existe, generar la sentencia SQL de actualización
                campos_valores = []
                if nombre:
                    campos_valores.append(('nempresa', nombre))
                if descripcion:
                    campos_valores.append(('descripcion', descripcion))
                if tipo:
                    campos_valores.append(('tipo', tipo))
                if correo:
                    campos_valores.append(('correo', correo))
                if telefono:
                    campos_valores.append(('telefono', telefono))
                if direccion:
                    campos_valores.append(('direccion', direccion))
                if foto:
                    campos_valores.append(('logo', foto))
                
                if longitud:
                    campos_valores.append(('longitud', longitud))

                if latitud:
                    campos_valores.append(('latitud', latitud))

                set_clause = ', '.join([f'{campo}=?' for campo, _ in campos_valores])

                # Actualizar los datos de la empresa en la tabla Empresa
                cursor.execute(f'UPDATE Empresa SET {set_clause} WHERE id_usuario=?', [valor for _, valor in campos_valores] + [self.user_id])
            else:
                # La empresa no existe, insertar una nueva fila
                cursor.execute('INSERT INTO Empresa (nempresa, descripcion, tipo, correo, telefono, direccion, logo, id_usuario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                            (nombre, descripcion, tipo, correo, telefono, direccion, foto, self.user_id))

            # Guardar los cambios en la base de datos
            conexion.commit()

            # Mostrar un mensaje de éxito
            CustomMessageBox.information(self, "Éxito", "Los datos de la Empresa se han guardado correctamente.")

        except sqlite3.Error as error:
            # Mostrar un mensaje de error en caso de que ocurra un problema al guardar los datos
            CustomMessageBox.critical(self, "Error", f"Error al guardar datos en la tabla Empresa: {error}")

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()


# Instanciar y ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EmpresaFormulario(1)
    ventana.show()
    sys.exit(app.exec())

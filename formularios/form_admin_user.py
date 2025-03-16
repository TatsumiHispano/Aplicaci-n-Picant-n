import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from util.util_popup import CustomMessageBox

class AdminFormulario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Búsqueda y Modificación de Usuarios")

        # Crear los campos de entrada para el nombre de usuario y los resultados
        self.txt_nombre_busqueda = QLineEdit()
        self.txt_nombre_busqueda.setPlaceholderText("Nombre de Usuario")
        self.txt_nombre_busqueda.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 10px; margin-bottom: 10px;")

        self.campos_edit = [
            QLineEdit(),  # Nombre
            QLineEdit(),  # Primer Apellido
            QLineEdit(),  # Segundo Apellido
            QLineEdit(),  # Correo
            QLineEdit(),  # Teléfono
            QLineEdit(),  # Dirección
            QLineEdit(),  # Permisos
            QLineEdit(),  # Contraseña
            QLineEdit()   # Fotos
        ]
        for campo in self.campos_edit:
            campo.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 10px; margin-bottom: 10px;")

        # Crear los botones para buscar, guardar cambios, eliminar usuario y volver atrás
        self.btn_buscar = QPushButton("Buscar")
        self.btn_buscar.setStyleSheet("background-color: #E5BF89; color: white; border: none; padding: 10px 20px; border-radius: 15px;")
        self.btn_buscar.clicked.connect(self.buscar_usuarios)

        self.btn_guardar = QPushButton("Guardar Cambios")
        self.btn_guardar.setStyleSheet("background-color: #E5BF89; color: white; border: none; padding: 10px 20px; border-radius: 15px;")
        self.btn_guardar.clicked.connect(self.guardar_cambios)

        self.btn_eliminar = QPushButton("Borrar Usuario")
        self.btn_eliminar.setStyleSheet("background-color: #E5BF89; color: white; border: none; padding: 10px 20px; border-radius: 15px;")
        self.btn_eliminar.clicked.connect(self.eliminar_usuario)

        self.btn_volver = QPushButton("Volver Atrás")
        self.btn_volver.setStyleSheet("background-color: #E5BF89; color: white; border: none; padding: 10px 20px; border-radius: 15px;")  # Estilo aplicado correctamente

        # Crear las etiquetas para los campos de usuario
        self.labels = [
            QLabel("Nombre:"),
            QLabel("Primer Apellido:"),
            QLabel("Segundo Apellido:"),
            QLabel("Correo:"),
            QLabel("Teléfono:"),
            QLabel("Dirección:"),
            QLabel("Permisos:"),
            QLabel("Contraseña:"),
            QLabel("Fotos:")
        ]
        for label in self.labels:
            label.setStyleSheet("font-weight: bold; color: #333333; margin-bottom: 5px;")

        # Crear el layout principal y agregar los elementos
        self.layout_principal = QVBoxLayout()
        self.layout_horizontal = QHBoxLayout()

        # Crear dos columnas
        columna_izquierda = QVBoxLayout()
        columna_izquierda.setContentsMargins(10, 10, 10, 10)
        columna_derecha = QVBoxLayout()
        columna_derecha.setContentsMargins(10, 10, 10, 10)

        # Agregar campos y etiquetas a cada columna
        for label, campo_edit in zip(self.labels[:len(self.labels)//2], self.campos_edit[:len(self.campos_edit)//2]):
            columna_izquierda.addWidget(label)
            columna_izquierda.addWidget(campo_edit)

        for label, campo_edit in zip(self.labels[len(self.labels)//2:], self.campos_edit[len(self.campos_edit)//2:]):
            columna_derecha.addWidget(label)
            columna_derecha.addWidget(campo_edit)

        # Agregar columnas al layout principal
        self.layout_horizontal.addLayout(columna_izquierda)
        self.layout_horizontal.addLayout(columna_derecha)

        # Agregar widgets adicionales
        self.layout_principal.addWidget(self.txt_nombre_busqueda)
        self.layout_principal.addWidget(self.btn_buscar)
        self.layout_principal.addLayout(self.layout_horizontal)
        self.layout_principal.addWidget(self.btn_guardar)
        self.layout_principal.addWidget(self.btn_eliminar)
        self.layout_principal.addWidget(self.btn_volver)

        # Crear un widget central y establecer el layout principal
        self.widget_central = QWidget()
        self.widget_central.setLayout(self.layout_principal)
        self.setCentralWidget(self.widget_central)

    def buscar_usuarios(self):
        # Obtener el nombre de usuario para buscar
        nombre = self.txt_nombre_busqueda.text().strip()

        # Realizar la búsqueda en la base de datos
        usuarios_encontrados = self.buscar_en_base_de_datos(nombre)

        # Mostrar los resultados de la búsqueda
        self.mostrar_resultados(usuarios_encontrados)

    def buscar_en_base_de_datos(self, nombre):
        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()

        try:
            # Construir la consulta SQL para buscar usuarios por nombre de usuario
            consulta = "SELECT * FROM Usuarios WHERE nusuario = ?"
            parametros = [nombre]

            # Ejecutar la consulta SQL
            cursor.execute(consulta, parametros)
            usuarios_encontrados = cursor.fetchall()

            return usuarios_encontrados

        except sqlite3.Error as error:
            # Manejar cualquier error de base de datos
            CustomMessageBox.critical(self, "Error", f"Error al buscar usuarios en la base de datos: {error}")
            return []

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def mostrar_resultados(self, usuarios_encontrados):
        # Si no se encontraron usuarios, mostrar un mensaje
        if not usuarios_encontrados:
            mensaje = QLabel("No se encontraron usuarios.")
            self.layout_principal.addWidget(mensaje)
            return

        # Llenar los campos de entrada con la información del primer usuario encontrado
        usuario = usuarios_encontrados[0]
        for campo_edit, valor in zip(self.campos_edit, usuario[2:]):
            campo_edit.setText(str(valor))

    def guardar_cambios(self):
        # Obtener el nombre de usuario para identificar al usuario a actualizar
        nombre_usuario = self.txt_nombre_busqueda.text().strip()

        # Obtener los valores de los campos de entrada
        valores = [campo.text() for campo in self.campos_edit]

        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()

        try:
            # Generar la sentencia SQL para actualizar los datos del usuario
            consulta = "UPDATE Usuarios SET nombre=?, papellido=?, sapellido=?, correo=?, telefono=?, direccion=?, permisos=?, contrasena=?, foto=? WHERE nusuario = ?"

            # Ejecutar la consulta SQL
            cursor.execute(consulta, valores + [nombre_usuario])

            # Confirmar la transacción y guardar los cambios en la base de datos
            conexion.commit()

            # Mostrar un mensaje de éxito
            CustomMessageBox.information(self, "Éxito", "Los cambios se han guardado correctamente.")

        except sqlite3.Error as error:
            # Mostrar un mensaje de error en caso de fallo en la actualización
            CustomMessageBox.critical(self, "Error", f"Error al guardar cambios en la base de datos: {error}")

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def eliminar_usuario(self):
        # Obtener el nombre de usuario para eliminar
        nombre_usuario = self.txt_nombre_busqueda.text().strip()

        # Confirmar si el usuario realmente desea eliminar al usuario
        respuesta = CustomMessageBox.question(self, "Confirmar Eliminación", f"¿Está seguro de eliminar al usuario '{nombre_usuario}'?",
                                        CustomMessageBox.Yes | CustomMessageBox.No)

        if respuesta == CustomMessageBox.Yes:
            # Conectar a la base de datos SQLite
            conexion = sqlite3.connect('tfg.db')
            cursor = conexion.cursor()

            try:
                # Generar la sentencia SQL para eliminar al usuario
                consulta = "DELETE FROM Usuarios WHERE nusuario = ?"

                # Ejecutar la consulta SQL
                cursor.execute(consulta, [nombre_usuario])

                # Confirmar la transacción y guardar los cambios en la base de datos
                conexion.commit()

                # Mostrar un mensaje de éxito
                CustomMessageBox.information(self, "Éxito", f"El usuario '{nombre_usuario}' ha sido eliminado correctamente.")

                # Limpiar los campos de búsqueda y resultados
                self.txt_nombre_busqueda.clear()
                self.mostrar_resultados([])

            except sqlite3.Error as error:
                # Mostrar un mensaje de error en caso de fallo en la eliminación
                CustomMessageBox.critical(self, "Error", f"Error al eliminar usuario de la base de datos: {error}")

            finally:
                # Cerrar la conexión a la base de datos
                conexion.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = AdminFormulario()
    ventana.show()
    sys.exit(app.exec_())

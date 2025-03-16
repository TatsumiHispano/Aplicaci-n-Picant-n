import sys
import sqlite3
import re  # Importar el módulo de expresiones regulares
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFormLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from util.util_popup import CustomMessageBox

def crear_isla_blanca():
    isla = QWidget()
    isla.setStyleSheet("background-color: white; border-radius: 10px; padding: 20px; margin: 0px;")
    return isla

class ProductoFormulario(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.setWindowTitle("Datos de productos")
        self.resize(400, 500)

        # Crear el layout principal
        layout_principal = QVBoxLayout()

        # Crear una isla blanca para el formulario
        isla_formulario = crear_isla_blanca()

        # Crear un formulario para los datos del producto
        form_layout = QFormLayout()
        form_layout.setVerticalSpacing(0)

        # Crear campos de entrada para cada atributo del producto
        self.txt_id_busqueda = QLineEdit()
        self.txt_id = QLineEdit()
        self.txt_nombre = QLineEdit()
        self.txt_descripcion = QLineEdit()
        self.txt_ingredientes = QLineEdit()
        self.txt_foto = QLineEdit()

        # Definir el estilo para los QLineEdit
        for line_edit in [self.txt_id_busqueda, self.txt_id, self.txt_nombre, self.txt_descripcion, self.txt_ingredientes, self.txt_foto]:
            line_edit.setStyleSheet("background-color: #FFFFFF; border: 2px solid #E5BF89; border-radius: 15px; padding: 5px; margin-top: 13px")

        # Agregar los campos al formulario
        form_layout.addRow("ID de producto a buscar:", self.txt_id_busqueda)
        form_layout.addRow("ID producto:", self.txt_id)
        form_layout.addRow("Nombre:", self.txt_nombre)
        form_layout.addRow("Descripcion:", self.txt_descripcion)
        form_layout.addRow("Ingredientes:", self.txt_ingredientes)
        form_layout.addRow("Foto:", self.txt_foto)

        # Crear botones para buscar y guardar cambios
        btn_buscar = QPushButton("Buscar")
        btn_buscar.setStyleSheet("background-color: #E5BF89; color: white; padding: 10px 24px; border: none; border-radius: 15px; margin-top: 15px; ")
        btn_guardar = QPushButton("Guardar")
        btn_guardar.setStyleSheet("background-color: #E5BF89; color: white; padding: 10px 24px; border: none; border-radius: 15px; margin-top: 15px; ")

        # Conectar los botones a las funciones correspondientes
        btn_buscar.clicked.connect(self.autocompletar_campos)
        btn_guardar.clicked.connect(self.guardar_cambios)

        # Agregar el formulario y los botones al layout principal
        isla_formulario.setLayout(form_layout)
        layout_principal.addWidget(isla_formulario)
        layout_principal.addWidget(btn_buscar)
        layout_principal.addWidget(btn_guardar)

        # Crear un widget central y establecer el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        self.btn_volver = QPushButton("Volver Atrás")
        self.btn_volver.setStyleSheet("background-color: #E5BF89; color: white; border: none; padding: 10px 20px; border-radius: 15px;")  # Estilo aplicado correctamente
        layout_principal.addWidget(self.btn_volver)

    def autocompletar_campos(self):
        # Obtener el ID del usuario actual
        user_id = self.user_id

        # Obtener el ID del producto a buscar
        id_busqueda = self.txt_id_busqueda.text()

        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()

        try:
            # Obtener los datos del producto de la tabla Productos
            cursor.execute("""
                SELECT *
                FROM Productos
                WHERE idproducto = ? AND idempresa = (
                    SELECT id
                    FROM Empresa
                    WHERE id_usuario = ?
                )
                """, (id_busqueda, user_id))

            producto = cursor.fetchone()

            # Autocompletar los campos del formulario con la información del producto
            if producto:
                self.txt_id.setText(str(producto[1]))
                self.txt_nombre.setText(str(producto[2]))
                self.txt_descripcion.setText(str(producto[3]))
                self.txt_ingredientes.setText(str(producto[4]))
                self.txt_foto.setText(str(producto[5]))
            else:
                respuesta = CustomMessageBox.question(self, "Producto no encontrado", "El producto no existe. ¿Quieres crear un nuevo producto?")
                if respuesta == CustomMessageBox.Yes:
                    self.txt_id.setText(id_busqueda)
                    self.txt_nombre.clear()
                    self.txt_descripcion.clear()
                    self.txt_ingredientes.clear()
                    self.txt_foto.clear()

        except sqlite3.Error as error:
            # Mostrar un mensaje de error en caso de que ocurra un problema al obtener los datos del producto
            CustomMessageBox.critical(self, "Error", f"Error al obtener los datos del producto de la base de datos: {error}")

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

    def guardar_cambios(self):
        # Obtener el ID del usuario actual
        user_id = self.user_id

        # Obtener el ID del producto a buscar
        id_busqueda = self.txt_id_busqueda.text()

        # Obtener los valores de los campos de entrada
        id_producto = self.txt_id.text()
        nombre = self.txt_nombre.text()
        descripcion = self.txt_descripcion.text()
        ingredientes = self.txt_ingredientes.text()
        foto = self.txt_foto.text()

        # Conectar a la base de datos SQLite
        conexion = sqlite3.connect('tfg.db')
        cursor = conexion.cursor()

        try:
            # Verificar si el nuevo ID del producto ya existe para esta empresa
            cursor.execute("""
                SELECT COUNT(*)
                FROM Productos
                WHERE idproducto = ? AND idempresa = (
                    SELECT id
                    FROM Empresa
                    WHERE id_usuario = ?
                )
                """, (id_producto, user_id))

            id_producto_existe = cursor.fetchone()[0]

            if id_producto_existe > 0 and id_producto != id_busqueda:
                CustomMessageBox.critical(self, "Error", "El ID del producto ya existe. No puedes usar este ID.")
                return

            # Verificar si el producto a buscar existe
            cursor.execute("""
                SELECT COUNT(*)
                FROM Productos
                WHERE idproducto = ? AND idempresa = (
                    SELECT id
                    FROM Empresa
                    WHERE id_usuario = ?
                )
                """, (id_busqueda, user_id))

            existe = cursor.fetchone()[0]

            if existe > 0:
                # Actualizar los datos del producto en la tabla Productos
                cursor.execute("""
                    UPDATE Productos
                    SET idproducto = ?, nombreproducto = ?, descripcion = ?, ingredientes = ?, foto = ?
                    WHERE idproducto = ? AND idempresa = (
                        SELECT id
                        FROM Empresa
                        WHERE id_usuario = ?
                    )
                    """, (id_producto, nombre, descripcion, ingredientes, foto, id_busqueda, user_id))
            else:
                # Insertar un nuevo producto en la tabla Productos
                cursor.execute("""
                    INSERT INTO Productos (idproducto, nombreproducto, descripcion, ingredientes, foto, idempresa)
                    VALUES (?, ?, ?, ?, ?, (
                        SELECT id
                        FROM Empresa
                        WHERE id_usuario = ?
                    ))
                    """, (id_producto, nombre, descripcion, ingredientes, foto, user_id))

            # Guardar los cambios en la base de datos
            conexion.commit()

            # Mostrar un mensaje de éxito
            CustomMessageBox.information(self, "Éxito", "Los datos del producto se han guardado correctamente.")

        except sqlite3.Error as error:
            # Mostrar un mensaje de error en caso de que ocurra un problema al guardar los datos
            CustomMessageBox.critical(self, "Error", f"Error al actualizar datos en la tabla Productos: {error}")

        finally:
            # Cerrar la conexión a la base de datos
            conexion.close()

# Instanciar y ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ProductoFormulario(1)
    ventana.show()
    sys.exit(app.exec())

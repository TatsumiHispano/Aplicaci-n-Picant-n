import sys
import asyncio
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QSize, Qt, QUrl
from PySide6.QtGui import QIcon, QFont
from folium import Map, Popup, DivIcon, Marker
from geopy.distance import geodesic
from PIL import Image
import base64, io, sqlite3, requests
from util.util_volver import RoundButton
from PySide6.QtCore import QObject, QThread, Signal

class Worker(QObject):
    finished = Signal()

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.map = None

    def run(self):
        # Realizar operaciones de red y cálculos aquí
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.load_data())
        loop.close()
        self.finished.emit()

    async def load_data(self):
        # Tu código que carga los datos desde la base de datos y realiza operaciones de red
        conn = sqlite3.connect('tfg.db')
        cursor = conn.cursor()

        cursor.execute("SELECT latitud, longitud FROM Usuarios WHERE id=?", (self.user_id,))
        user_coordinates = cursor.fetchone()

        if user_coordinates and user_coordinates[0] is not None and user_coordinates[1] is not None:
            tu_ubicacion = [float(user_coordinates[0]), float(user_coordinates[1])]
        else:
            tu_ubicacion = [40.4168, -3.7038]

        cursor.execute("SELECT id, nempresa, latitud, longitud, logo FROM Empresa")
        empresas = cursor.fetchall()

        m = Map(location=tu_ubicacion, zoom_start=6)

        distancia_minima = float('inf')
        empresa_mas_cercana = None

        for empresa in empresas:
            id_empresa, nombre, latitud, longitud, logo_url = empresa

            if latitud is not None and longitud is not None:
                if logo_url:
                    response = requests.get(logo_url)
                    if response.status_code == 200:
                        logo_bytes = response.content
                        logo_img = Image.open(io.BytesIO(logo_bytes))
                        logo_img.thumbnail((50, 50))
                        buffer = io.BytesIO()
                        logo_img.save(buffer, format='PNG')
                        logo_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
                        icon_html = f"""
                        <div style="
                            background-image: url('data:image/png;base64,{logo_data}');
                            background-size: cover;
                            width: 25px;
                            height: 25px;
                            border-radius: 50%;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                        ">
                        </div>
                        """
                        icon = DivIcon(html=icon_html)
                    else:
                        print(f"No se pudo descargar el logo para la empresa: {nombre}")
                else:
                    print(f"La empresa {nombre} no tiene URL de logo especificada, se omite.")

                coordenadas_empresa = [float(latitud), float(longitud)]

                distancia = geodesic(tu_ubicacion, coordenadas_empresa).kilometers
                if distancia < distancia_minima:
                    distancia_minima = distancia
                    empresa_mas_cercana = empresa

                if tu_ubicacion != [40.4168, -3.7038]:
                    popup_html = f"<b>{nombre}</b><br>Distancia: {distancia:.2f} km"
                    marker = Marker(location=coordenadas_empresa, popup=Popup(popup_html, max_width=300), icon=icon)
                    m.add_child(marker)
                else: 
                    popup_html = f"<b>{nombre}</b>"
                    marker = Marker(location=coordenadas_empresa, popup=Popup(popup_html, max_width=300), icon=icon)
                    m.add_child(marker)
            else:
                print(f"La empresa {nombre} no tiene coordenadas especificadas, se omite.")

        cursor.execute("SELECT foto FROM Usuarios WHERE id=?", (self.user_id,))
        user_profile_picture_url = cursor.fetchone()

        if user_profile_picture_url:
            response = requests.get(user_profile_picture_url[0])
            if response.status_code == 200:
                user_profile_picture_bytes = response.content
                user_profile_picture_base64 = base64.b64encode(user_profile_picture_bytes).decode('utf-8')
                if tu_ubicacion != [40.4168, -3.7038]:
                    popup_html = f"<b>Tu Ubicación</b><br>Distancia a la empresa más cercana: {distancia_minima:.2f} km"
                else:
                    popup_html = "<b>Centro de España</b>"
                icon_html = f"""
                <img src='data:image/png;base64,{user_profile_picture_base64}' style='width: 25px; height: 25px; border-radius: 50%;'>
                """
                icon = DivIcon(html=icon_html)
                marker = Marker(location=tu_ubicacion, popup=Popup(popup_html), icon=icon)
                m.add_child(marker)
            else:
                print("No se pudo descargar la imagen de perfil del usuario.")
        else:
            if tu_ubicacion != [40.4168, -3.7038]:
                popup_html = f"<b>Tu Ubicación</b><br>Distancia a la empresa más cercana: {distancia_minima:.2f} km"
            else:
                popup_html = "<b>Centro de España</b>"
            icon = DivIcon(html="<div style='font-size: 20px; color: blue;'>&#x1F6CD;</div>")
            marker = Marker(location=tu_ubicacion, popup=Popup(popup_html), icon=icon)
            m.add_child(marker)

        self.map = m


class restaurantmap(QMainWindow):
    def __init__(self, user_id):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.central_widget.setLayout(self.layout)

        self.map_view = QWebEngineView()

        self.map_view.setContentsMargins(0, 0, 0, 0)

        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_widget.setFixedHeight(100)
        header_widget.setStyleSheet("background-color: #E5BF89; padding: 10px; border-radius: 0px;")

        header_layout.setContentsMargins(30, 0, 0, 0)
        header_layout.setSpacing(0)

        self.volver_button = RoundButton()
        self.volver_button.setIcon(QIcon("./imagenes/volver.png"))
        self.volver_button.setStyleSheet("QPushButton {background-color: white; border-radius: 15px; border: none; color: white; font-family: FontAwesome; font-size: 16px; padding: 5px 10px;} QPushButton:hover {background-color: #218838;}")
        header_layout.addWidget(self.volver_button)

        header_label = QLabel("Mapa", self)
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("color: #333; margin-right: 50px")

        header_layout.addWidget(header_label)
        self.layout.addWidget(header_widget)

        # Agregar el mapa a un layout horizontal
        map_layout = QHBoxLayout()
        map_layout.addWidget(self.map_view)
        self.layout.addLayout(map_layout)

        # Iniciar el hilo de trabajo
        self.worker = Worker(user_id)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.on_worker_finished)
        self.worker_thread.start()

    def on_worker_finished(self):
        # Una vez que el trabajo en el hilo haya terminado, cargar el mapa
        m = self.worker.map
        html_map = m.get_root().render()
        self.map_view.setHtml(html_map)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = restaurantmap()
    window.show()
    sys.exit(app.exec())


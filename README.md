Desarrollado por:

 Juan Jose Montero Solano

 Luis Rebollo Diaz
 
 Adrian Aznar Madrid

 Picantón - Aplicación para la Gestión de Restaurantes

 ![Captura de pantalla 2025-03-16 125316](https://github.com/user-attachments/assets/de9315f9-7431-4cd9-b792-020204d6ee17)
 
![Captura de pantalla 2025-03-16 125337](https://github.com/user-attachments/assets/ee23427a-b1b0-465b-bf3a-8d2d3f56b773)

![Captura de pantalla 2025-03-16 125428](https://github.com/user-attachments/assets/f365b108-e54c-4b43-bfde-e18095cac699)

![Captura de pantalla 2025-03-16 125442](https://github.com/user-attachments/assets/fe672ca1-4996-4f12-8975-a6bd02c1062a)

![Captura de pantalla 2025-03-16 125457](https://github.com/user-attachments/assets/f13a187d-09c2-4535-9b16-8b701fc2f344)

![Captura de pantalla 2025-03-16 125513](https://github.com/user-attachments/assets/a95387af-4987-4bc1-8631-96c9ab0c4756)

![Captura de pantalla 2025-03-16 125557](https://github.com/user-attachments/assets/26dc9f05-b7e3-45ff-81a9-d1bc7cd7a627)

![Captura de pantalla 2025-03-16 125610](https://github.com/user-attachments/assets/223470dc-652b-4693-b185-be2db1307e0c)

![Captura de pantalla 2025-03-16 125626](https://github.com/user-attachments/assets/b14de7fd-fe87-4633-9a82-0aaf7d1e9761)

![Captura de pantalla 2025-03-16 125642](https://github.com/user-attachments/assets/4e94f515-32e7-40ec-879a-40181ac5fede)

![Captura de pantalla 2025-03-16 125655](https://github.com/user-attachments/assets/26962ae1-db20-43c6-a0d1-7cf3cff23175)

![Captura de pantalla 2025-03-16 125705](https://github.com/user-attachments/assets/4564f513-f2f9-41b1-9c3e-e571fb96c8eb)



🐔 Picantón

Picantón es una aplicación desarrollada en Python que funciona como un buscador y comparador de restaurantes, similar a plataformas como Just Eat. Está diseñada tanto para usuarios que buscan opciones gastronómicas como para propietarios de restaurantes que desean promocionar sus negocios.

🎯 Objetivos

Para usuarios:
Obtener información general sobre restaurantes de forma rápida y sencilla.

Crear perfiles para guardar preferencias y opiniones personales.

Buscar restaurantes cercanos mediante un mapa interactivo.

Aplicar filtros por tipo de gastronomía.

Leer y dejar reseñas y comentarios.

Disfrutar de una interfaz personalizable para mejorar la experiencia.

Usar una herramienta práctica, atractiva y útil para decidir dónde comer.

Para restaurantes:
Compartir información detallada del negocio.

Publicar y actualizar menús y servicios.

Aumentar su visibilidad y captar nuevos clientes.

Recibir retroalimentación directa a través de reseñas.

Organizar y gestionar mejor sus servicios.

Incrementar ventas y mejorar la competitividad local.

🧩 Estructura del Proyecto

La aplicación está organizada en módulos y clases desarrolladas en Python con PySide6 y PyQt6. A continuación se detallan los principales componentes:

Módulos de Interfaz de Usuario (UI):
form_info_design.py
Muestra información sobre la aplicación y los autores.

form_ajustes.py
Permite personalizar la interfaz (colores y estilo).

form_adminmenu.py
Panel principal de administración con navegación entre formularios.

ui_Register.py
Registro de usuarios con validación de datos y almacenamiento en SQLite.

ui_Login.py
Inicio de sesión con navegación al registro o a la app principal.

form_usuario.py
Gestión de información personal del usuario.

form_admin_user.py
Administración de usuarios: búsqueda, edición y eliminación.

form_admin_empresa.py
Administración de empresas registradas.

ui_Loadingbar.py
Pantalla de carga animada con barra de progreso.

form_menu_empresa.py
Panel de administración para empresas, con acceso a gestión de productos y usuarios.

form_maestro_design.py
Construcción de interfaz de escritorio avanzada con PySide6.

form_inicio.py
Vista principal de búsqueda y exploración de restaurantes.

form_inicio_productos.py
Detalles del restaurante, productos y reseñas.

form_empresa.py
Edición y gestión de información empresarial.

form_productos.py
Gestión de productos asociados a los restaurantes.

🛠️ Tecnologías Utilizadas
Python – Lenguaje principal del proyecto

PySide6 / PyQt6 – Desarrollo de interfaces gráficas

SQLite – Base de datos local para gestión de usuarios, restaurantes y productos

Visual Studio Code – Entorno de desarrollo

🚀 Funcionalidades Clave

Registro e inicio de sesión con autenticación segura.

Gestión de perfiles de usuario y preferencias.

Búsqueda por cercanía, tipo de comida y nombre.

Visualización detallada de cada restaurante, incluyendo ubicación en el mapa, menú y opiniones.

Sistema completo de reseñas y comentarios.

Panel de administración para empresas.

Personalización de la interfaz por parte del usuario.

Carga dinámica de contenido y experiencia fluida.

✅ Conclusión
Picantón es una solución digital funcional e intuitiva para conectar a los amantes de la gastronomía con los restaurantes de su zona. Con un enfoque centrado en la experiencia del usuario y una arquitectura robusta, ofrece una herramienta potente tanto para el consumidor final como para los negocios del sector.




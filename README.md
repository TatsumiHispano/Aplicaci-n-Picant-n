Desarrollado por:

 Juan Jose Montero Solano

 Luis Rebollo Diaz
 
 Adrian Aznar Madrid

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

Picantón - Aplicación para la Gestión de Restaurantes

Descripción General

Picantón es una aplicación desarrollada en Python, similar a Just Eat, diseñada para facilitar la búsqueda y comparación de restaurantes. 

La aplicación está dirigida tanto a usuarios que buscan opciones gastronómicas como a propietarios de restaurantes que desean promocionar sus negocios.

Objetivos

Los principales objetivos de Picantón son:

Para los usuarios:

Proporcionar información general de los restaurantes de forma rápida y sencilla.

Facilitar la creación de perfiles de usuario para guardar preferencias y opiniones.

Mostrar restaurantes cercanos a la ubicación del usuario a través de un mapa.

Permitir la búsqueda de restaurantes mediante filtros por tipo de gastronomía.

Ofrecer una plataforma para que los usuarios expresen sus opiniones y comentarios sobre los restaurantes.

Mejorar la experiencia del usuario proporcionando una herramienta sencilla y útil para elegir restaurantes.

Permitir la personalización de la interfaz de usuario según las preferencias del usuario.

Para los restaurantes:

Ayudar a los restaurantes a compartir información detallada de su establecimiento.

Permitir la publicación y actualización de menús y servicios.

Facilitar la captación de nuevos clientes.

Mejorar la competitividad en el sector de la hostelería local.

Mejorar la organización y control de sus servicios.

Obtener retroalimentación directa de los clientes a través de reseñas y comentarios.

Facilitar el crecimiento económico mediante el incremento de ventas y la obtención de nuevos clientes.

Estructura del Proyecto

La aplicación Picantón se compone de varios módulos y clases en Python, cada uno con una función específica. A continuación, se describen los principales componentes:

Módulos de la Interfaz de Usuario (UI)

form_info_design.py:
Crea una ventana principal con el título "Info Picantón" y un icono.

Muestra la versión de la aplicación y los nombres de los autores mediante etiquetas (QLabel).

form_ajustes.py:
Crea una ventana de ajustes que permite al usuario cambiar los colores de la barra superior, el menú lateral y el cuerpo principal de la interfaz de usuario.
Utiliza un diálogo de selección de color para permitir la personalización.

form_adminmenu.py:
Crea una ventana principal que permite navegar entre diferentes formularios de administración.

Utiliza un QStackedWidget para gestionar la navegación entre formularios.

Incluye botones estilizados para abrir los formularios de administración de usuarios y empresas.

ui_Register.py:
Define una ventana de registro de usuarios con validación de entradas y un estilo personalizado.

Permite a los usuarios registrar su nombre de usuario, correo electrónico y contraseña.

Maneja la interacción con una base de datos SQLite para almacenar los datos de los usuarios.

Utiliza técnicas de interfaz gráfica avanzadas, como ventanas sin bordes y ventanas movibles.

ui_Login.py:
Implementa una ventana de inicio de sesión.

Interactúa con una base de datos SQLite para autenticar usuarios.

Incluye navegación a la ventana de registro y a la aplicación principal.

form_usuario.py:
Crea una interfaz gráfica para que los usuarios ingresen y actualicen su información personal.

Utiliza una base de datos SQLite para almacenar y recuperar los datos de los usuarios.

form_admin_user.py:
Proporciona una aplicación para la gestión de usuarios en una base de datos SQLite.

Incluye funcionalidades de búsqueda, edición y eliminación de usuarios.

Maneja errores y considera aspectos de seguridad.

form_admin_empresa.py:
Proporciona una aplicación para la gestión de empresas en una base de datos SQLite.

Incluye funcionalidades de búsqueda, edición y eliminación de empresas.

Maneja errores y considera aspectos de seguridad.

ui_Loadingbar.py:
Crea una pantalla de carga animada con una barra de progreso circular y un logotipo.

Se muestra mientras se cargan los recursos de la aplicación.

Muestra la ventana de inicio de sesión una vez completada la carga.

form_menu_empresa.py:
Crea una ventana principal con un menú para administrar datos relacionados con la empresa.

Permite navegar entre diferentes formularios para administrar usuarios, productos y otras entidades de la empresa.

Utiliza estilos CSS personalizados para mejorar la apariencia de la interfaz de usuario.

form_maestro_design.py:
Crea una aplicación de escritorio utilizando el framework PySide6.

Se centra en la creación de una interfaz de usuario (UI) dinámica y atractiva.

form_inicio.py:
Proporciona los fundamentos para una aplicación de búsqueda y listado de restaurantes.

Utiliza una interfaz gráfica PyQt6.

Maneja interacciones de usuario, operaciones de base de datos y carga asincrónica de imágenes.

form_inicio_productos.py:
Muestra detalles de un restaurante, incluyendo productos disponibles y reseñas de usuarios.

Ofrece una interfaz de usuario bien diseñada y funcionalidad interactiva.

form_empresa.py:
Crea una interfaz gráfica de usuario para que los usuarios ingresen o editen información sobre una empresa.

Guarda los cambios realizados en una base de datos SQLite.

form_productos.py:
Crea una interfaz gráfica de usuario que permite a los usuarios buscar y editar información sobre productos.

Guarda los cambios realizados en la base de datos SQLite.

Tecnologías Utilizadas

Python: Lenguaje de programación principal utilizado para el desarrollo de la aplicación.

PySide6: Biblioteca de Python para el desarrollo de aplicaciones gráficas basadas en el conjunto de herramientas Qt.

SQLite: Sistema de gestión de bases de datos utilizado para el almacenamiento y gestión de datos.

Visual Studio Code: Entorno de desarrollo integrado (IDE) utilizado para el desarrollo de la aplicación.

Funcionalidades Principales

La aplicación Picantón ofrece las siguientes funcionalidades principales:

Registro e inicio de sesión de usuarios: Los usuarios pueden crear cuentas y acceder a la aplicación de forma segura.

Gestión de perfiles de usuario: Los usuarios pueden gestionar su información personal y preferencias.

Búsqueda y visualización de restaurantes: Los usuarios pueden buscar restaurantes cercanos, ver información detallada, menús y reseñas.

Gestión de empresas: Los propietarios de restaurantes pueden registrar y gestionar la información de sus negocios, menús y servicios.

Sistema de reseñas: Los usuarios pueden escribir y leer reseñas de restaurantes para compartir sus opiniones y experiencias.

Personalización de la interfaz de usuario: Los usuarios pueden cambiar los colores y el estilo de la aplicación según sus preferencias.

Visualización de mapas: Los usuarios pueden ver la ubicación de los restaurantes en un mapa.

Conclusión

Picantón es una aplicación completa y funcional que cumple con los objetivos propuestos. Proporciona una solución eficaz para la búsqueda y comparación de restaurantes, tanto para usuarios como para propietarios de negocios. El uso de Python y las bibliotecas y herramientas adecuadas ha permitido desarrollar una aplicación robusta, eficiente y fácil de usar.




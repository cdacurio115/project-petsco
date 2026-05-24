# Petscop 🐾

Petscop es una aplicación web para una fundación de adopción de mascotas. Permite a los usuarios explorar publicaciones de mascotas disponibles para adopción, registrarse, iniciar sesión, crear publicaciones y marcar mascotas para adopción.

## Funcionalidades

- Registro e inicio de sesión de usuarios
- Crear, editar y eliminar publicaciones de mascotas
- Subir imágenes a las publicaciones
- Ver publicaciones de forma individual
- Buscar mascotas por título o contenido
- Paginación de publicaciones
- Sistema de check para marcar mascotas en proceso de adopción
- Apartado de adopciones en proceso (solo usuarios registrados)
- Health check endpoint (`GET /health`)
- UI responsiva para móvil y escritorio

## Tecnologías usadas

- Python 3.11
- Flask
- SQLAlchemy
- MySQL Server 8.0
- PyMySQL
- Werkzeug
- python-dotenv

## Requisitos previos

- Python 3.11
- MySQL Server 8.0 (y opcionalmente MySQL Workbench para visualizar la base de datos)

## Configuración local

1. Clona el repositorio:
git clone https://github.com/cdacurio115/project-petsco.git
cd project-petsco

2. Crea y activa el entorno virtual:
python -m venv .venv
.venv\Scripts\activate

3. Instala las dependencias:
pip install -r requirements.txt

4. Crea la base de datos. Desde MySQL Workbench o la consola de MySQL ejecuta:
```sql
CREATE DATABASE blog_db;
```

5. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

DATABASE_URL=mysql+pymysql://root:root@localhost:3306/blog_db
SECRET_KEY=dev

6. Las credenciales por defecto de MySQL son:
- Usuario: `root`
- Contraseña: `root`
- Puerto: `3306`

7. Corre la aplicación:
py main.py

La app estará disponible en http://127.0.0.1:5000

## Credenciales de demo

- Usuario: `lexons`
- Contraseña: `12345`

- Usuario: `luis`
- Contraseña: `12345`

- Usuario: `adriana`
- Contraseña: `123`

## Correr las pruebas

pytest tests/

## estructura del proyecto
petscop/
├── myblog/
│   ├── models/
│   │   ├── user.py
│   │   ├── post.py
│   │   └── adopcion.py
│   ├── views/
│   │   ├── user.py
│   │   └── blog.py
│   ├── templates/
│   │   ├── autentic/
│   │   └── blog/
│   └── static/
│       ├── css/
│       ├── img/
│       └── uploads/
├── tests/
│   └── test_app.py
├── config.py
├── main.py
├── requirements.txt
└── .env
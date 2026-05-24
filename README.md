# Petscop 🐾

Petscop es una aplicación web para una fundación de adopción de mascotas. Permite a los usuarios explorar publicaciones de mascotas disponibles para adopción, registrarse, iniciar sesión y crear sus propias publicaciones.

## Tecnologías usadas

- Python 3.11
- Flask
- SQLAlchemy
- MySQL Server 8.0
- PyMySQL
- Werkzeug

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

5. Las credenciales por defecto en `config.py` son:
- Usuario: `root`
- Contraseña: `root`
- Puerto: `3306`

Si tu configuración es diferente, actualiza esta línea en `config.py`:
```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/blog_db"
```

6. Corre la aplicación:
py main.py

La app estará disponible en http://127.0.0.1:5000

## Credenciales de demo

- Usuario: `lexons`
- Contraseña: `12345`

## Correr las pruebas

pytest tests/

## Estructura del proyecto
petscop/
├── myblog/
│   ├── models/
│   │   ├── user.py
│   │   └── post.py
│   ├── views/
│   │   ├── user.py
│   │   └── blog.py
│   ├── templates/
│   └── static/
├── config.py
├── main.py
└── requirements.txt


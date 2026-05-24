from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#CARGAR CONFIGURACION
app.config.from_object("config.developmentconfig")
db = SQLAlchemy(app)

#tabla de user
from myblog.models.user import User

#tabla de post
from myblog.models.post import Post

#tabla de adopciones
from myblog.models.adopcion import Adopcion

with app.app_context():
    db.create_all()

#importar vistas
from myblog.views.user import user
app.register_blueprint(user)

#importar
from myblog.views.blog import blog
app.register_blueprint(blog)



import os
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static/uploads")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB máximo


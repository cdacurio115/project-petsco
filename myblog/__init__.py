from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#CARGAR CONFIGURACION
app.config.from_object("config.developmentconfig")
db = SQLAlchemy(app)


from myblog.models.user import User
from myblog.models.post import Post

with app.app_context():
    db.create_all()

#importar vistas
from myblog.views.user import user
app.register_blueprint(user)

#importar
from myblog.views.blog import blog
app.register_blueprint(blog)
from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for, 
)
import functools 
user = Blueprint("user", __name__, url_prefix="/user")

from werkzeug.security import check_password_hash, generate_password_hash

from myblog.models.user import User

from myblog import db 
#registrar un usuario
@user.route("/register", methods= ("GET", "POST"))
def register():
    if request.method == "POST":
        username =request.form.get("username")
        password =request.form.get("password")
        
        user = User(username, generate_password_hash(password))

        error = None
        if not username:
            error = "nombre de ususario requerido"
        elif not password:
            error = "se requiere una contraseña"
        
        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            error = f"El usuario {username} ya esta registrado"
        flash(error)
        return render_template("autentic/register.html"), 409

    return render_template("autentic/register.html")




#Iniciar sesion un usuario
@user.route("/login", methods= ("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        error = None

        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "El usuario no existe"
        elif not check_password_hash(user.password, password):
            error = "La contraseña es incorrecta"

        if error is None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("blog.index"))

        flash(error)
        return render_template("autentic/login.html"), 401

    return render_template("autentic/login.html")


@user.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

#cierre de sesion

@user.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("blog.index"))

#necesidad de usuario

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("user.login"))
        return view(**kwargs)
    return wrapped_view




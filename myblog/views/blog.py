from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for, current_app
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

import os

from myblog.models.post import Post
from myblog.models.user import User

from myblog.views.user import login_required

from myblog import db

blog = Blueprint("blog", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

#obtener un usuario
def get_user(id):
    result = db.session.get(User, id)
    return result


@blog.route("/")
def index():
    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    
    if search:
        posts = Post.query.filter(
            Post.title.contains(search) | Post.body.contains(search)
        ).paginate(page=page, per_page=5)
    else:
        posts = Post.query.paginate(page=page, per_page=5)
    
    return render_template("blog/index.html", posts=posts, get_user=get_user)


#crear un post
@blog.route("/blog/create", methods= ("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        image_filename = None

        if "image" in request.files:
            file = request.files["image"]
            if file and allowed_file(file.filename):
                image_filename = secure_filename(file.filename)
                file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], image_filename))

        post = Post(g.user.id, title, body, image_filename)

        error = None
        if not title:
            error = "Se requiere un titulo"
        elif not body:
            error = "se requiere una descripción"
        if error is not None:
            flash(error)
            return render_template("blog/create.html"), 400
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")

def get_post(id, check_autor=True):
    post = Post.query.get(id)
    if post is None:
        abort(404, f"Id {id} de la publicacion no existe.")
    
    if check_autor and post.autor != g.user.id:
        abort(403)
        
    return post

#actualizar un post
@blog.route("/blog/update/<int:id>", methods= ("GET", "POST"))
@login_required
def update(id):
    post = get_post(id)

    if request.method == "POST":
        post.title = request.form.get("title")
        post.body = request.form.get("body")

        error = None
        if not post.title:
            error = "Se requiere un titulo"
        elif not post.body:
            error = "se requiere una descripción"
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("blog.index"))
        
        flash(error)

    return render_template("blog/update.html", post=post)


#eliminar un post
@blog.route("/blog/delete/<int:id>")
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("blog.index"))


#health check
@blog.route("/health")
def health():
    return {"status": "ok"}


#visualizar post de forma individual
@blog.route("/blog/<int:id>")
def detail(id):
    from myblog.models.adopcion import Adopcion
    post = db.session.get(Post, id)
    if post is None:
        abort(404)
    author = get_user(post.autor)
    adopcion = Adopcion.query.filter_by(post_id=id).first()
    return render_template("blog/detail.html", post=post, author=author, adopcion=adopcion)


#marcar o desmarcar el check de adopcion
@blog.route("/blog/<int:id>/adoptar", methods=("POST",))
@login_required
def adoptar(id):
    from myblog.models.adopcion import Adopcion
    post = db.session.get(Post, id)
    if post is None:
        abort(404)

    adopcion = Adopcion.query.filter_by(post_id=id).first()

    if adopcion is None:
        nueva = Adopcion(post_id=id, user_id=g.user.id)
        db.session.add(nueva)
        db.session.commit()
    elif adopcion.user_id == g.user.id:
        db.session.delete(adopcion)
        db.session.commit()

    return redirect(url_for("blog.detail", id=id))


#adopciones en proceso
@blog.route("/adopciones")
@login_required
def adopciones():
    from myblog.models.adopcion import Adopcion
    adopciones = Adopcion.query.all()
    return render_template("blog/adopciones.html", adopciones=adopciones, get_user=get_user)
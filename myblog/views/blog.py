from flask import(
    render_template, Blueprint, flash, g, redirect, request, url_for
)
from werkzeug.exceptions import abort

from myblog.models.post import Post
from myblog.models.user import User

from myblog.views.user import login_required

from myblog import db

blog = Blueprint("blog", __name__)

#obtener un usuario
def get_user(id):
    result = db.session.get(User, id)
    return result


@blog.route("/")
def index():
    posts = Post.query.all()
    db.session.commit
    return render_template("blog/index.html", posts = posts, get_user = get_user)



#crear un post
@blog.route("/blog/create", methods= ("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title =request.form.get("title")
        body =request.form.get("body")
        
        post = Post(g.user.id, title, body)

        error = None
        if not title:
            error = "Se requiere un titulo"
        elif not body:
            error = "se requiere una descripción"
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("blog.index"))
        
        flash(error)

    return render_template("blog/create.html")

def get_post(id, check_autor = True):
    post = Post.query.get(id)
    if post is None:
        abort(404, f"Id {id} de la publicacion no existe. ")
    
    if check_autor and post.autor != g.user.id:
        abort(404)
        
    return post 

#actualizar un post
@blog.route("/blog/update/<int:id>", methods= ("GET", "POST"))
@login_required
def update(id):
    post = get_post(id)

    if request.method == "POST":
        post.title =request.form.get("title")
        post.body =request.form.get("body")
        

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

    return render_template("blog/update.html", post = post)


#eliminar un post
@blog.route("/blog/delete/<int:id>")
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("blog.index"))

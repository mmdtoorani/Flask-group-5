from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from WebBlog.db import User, Post
from WebBlog.LoginRequired import login_required

user_bp = Blueprint('user', __name__)


@login_required
@user_bp.route("/create", methods=("GET", "POST"))
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title_form = request.form["title"]
        body_form = request.form["body"]
        user_id_form = session['user_id']
        f = request.files.get('image')
        fname = secure_filename(f.filename)
        f.save('WebBlog/static/' + fname)
        image = fname
        error = None
        if not title_form:
            error = "Title is required."
        if error is not None:
            flash(error)
        else:
            post_created = Post(title=title_form, body=body_form, user=User.objects(id=user_id_form)[0], photo=image)
            post_created.save()
            return redirect(url_for("blog.home"))

    return render_template("create.html")


@user_bp.route("/profile/")
def profile():
    pass


@user_bp.route("/posts-list/")
def posts_list():
    pass


@user_bp.route("/edit-post/<post_id>")
def edit():
    pass


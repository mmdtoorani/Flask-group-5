import functools

from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from WebBlog.db import User, Post

blog_bp = Blueprint('blog', __name__)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("blog.login"))

        return view(**kwargs)

    return wrapped_view


@blog_bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = User.objects(id=user_id)[0]



@blog_bp.route('/')
@blog_bp.route('/home')
def home():
    return render_template("home.html")


@blog_bp.route("/login/", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username_form = request.form["username"]
        password_form = request.form["password"]
        error = None
        if User.objects(username=username_form):
            user = User.objects(username=username_form)[0]
            if check_password_hash(user.password, password_form):
                error = "Incorrect password."
        else:
            error = "Incorrect username."
        if error is None:
            session.clear()
            session["user_id"] = str(user.id)
            return redirect(url_for("blog.home"))

        flash(error)
    return render_template("login.html")


@blog_bp.route("/signup/", methods=("GET", "POST"))
def sign_up():
    if request.method == "POST":
        username_form = request.form["username"]
        first_name_form = request.form["first_name"]
        last_name_form = request.form["first_name"]
        email_form = request.form["first_name"]
        phone_form = request.form["phone"]
        password_form = request.form["password"]
        error = None

        if not username_form:
            error = "Username is required."

        elif not password_form:
            error = "Password is required."

        elif User.objects(username=username_form):
            error = f"User {username_form} is already registered."

        if error is None:
            user_created = User(username=username_form, email=email_form, first_name=first_name_form,
                                last_name=last_name_form,
                                phone_number=phone_form, password=generate_password_hash(password_form))
            user_created.save()

            return redirect(url_for("blog.login"))

        flash(error)
    return render_template('signup.html')


@login_required
@blog_bp.route("/create", methods=("GET", "POST"))
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
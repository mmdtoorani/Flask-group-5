from flask import Blueprint, render_template, request, url_for, redirect, flash, session

from WebBlog.db import User

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
@blog_bp.route('/home')
def home():
    return render_template('base.html')


@blog_bp.route("/login/")
def login():

    return render_template('login.html')


@blog_bp.route("/signup/", methods=("GET", "POST"))
def sign_up():
    if request.method == "POST":
        username_form = request.form["username"]
        first_name_form = request.form["first_name"]
        last_name_form = request.form["first_name"]
        email_form = request.form["first_name"]
        phone_form = request.form["phone"]
        password_form = str(hash(request.form["password"]))
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
                                phone_number=phone_form, password=password_form)
            user_created.save()

            return redirect(url_for("blog.login"))

        flash(error)
    return render_template('signup.html')

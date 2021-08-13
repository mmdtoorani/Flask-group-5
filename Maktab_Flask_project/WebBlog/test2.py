from flask import Blueprint, render_template, request, redirect, url_for, flash

from WebBlog.db import *

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
                                phone_number=phone_form)
            user_created.save()

            return redirect(url_for("blog.login"))

        flash(error)

    return render_template('signup.html')


-------------------


{% extends 'base.html' %}

{% block title %}{% endblock %}
{% block main %}
    <div class="container">
        <div class="row">
            <div class="col-sm-9 col-md-7 col-lg-5 mx-auto" id="card-container">
                <div class="card border-0 shadow rounded-3 my-5">
                    <div class="card-body p-4 p-sm-5">
                        <h5 class="card-title text-center mb-5 fw-light fs-5"><b>Sign up</b></h5>
                        <form method="post" action="{{ url_for('blog.sign_up') }}">
                            <div class="form-floating mb-3">
                                <input type="text" class="form-control" name="username" id="username" required>

                                <label for="floatingInput">Username</label>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="text" class="form-control" name="first_name" id="first_name" required>

                                <label for="floatingInput">First Name</label>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="text" class="form-control" name="last_name" id="last_name" required>

                                <label for="floatingInput">Last Name</label>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="email" class="form-control" name="email" id="email">

                                <label for="floatingInput">Email</label>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="text" class="form-control" name="phone" id="phone">

                                <label for="floatingInput">Phone</label>
                            </div>
                            <div class="form-floating mb-3">
                                <input type="password" class="form-control" name="password" id="password"
                                       placeholder="Password" required>
                                <label for="floatingPassword">Password</label>
                            </div>

                            <div class="d-grid">
                                <button class="btn btn-primary btn-login text-uppercase fw-bold" type="submit">Sign Up
                                </button>
                            </div>
                            <hr class="my-4">
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
{% block extra_footer %}{% endblock %}




---------------------




from mongoengine import *

connect(host="mongodb://127.0.0.1:27017/my_db")


class User(DynamicDocument):
    username = StringField(max_length=50)
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone_number = StringField(max_length=50)



-----------------------
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



@blog_bp.route('/home')
def home():
    return render_template("home.html")


@blog_bp.route("/login/", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username_form = request.form["username"]
        password_form = request.form["password"]
        print('hello1')
        error = None
        if User.objects(username=username_form):
            user = User.objects(username=username_form)[0]

            if check_password_hash(user.password, password_form):
                error = "Incorrect password."

        else:
            error = "Incorrect username."
            print('hello4')
        if error is None:
            session.clear()
            session["user_id"] = str(user.id)
            print('hello5')
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
        else:
            post_created = Post(title=title_form, body=body_form, user=User.objects(id=user_id_form)[0], photo=image)
            post_created.save()
            return redirect(url_for("blog.home"))

    return render_template("create.html")


@blog_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("blog.home"))

########################################################################################


from mongoengine import *

connect(host="mongodb://127.0.0.1:27017/my_db")


class Category(DynamicDocument):
    name = StringField(max_length=50)
    parent_cat = ReferenceField('self', required=False)


class Tag(DynamicDocument):
    name = StringField(max_length=50)


class User(DynamicDocument):
    username = StringField(max_length=50)
    email = StringField(max_length=50, required=False)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone_number = StringField(max_length=50)
    password = StringField(max_length=250)


class Post(DynamicDocument):
    title = StringField(max_length=50)
    body = StringField(max_length=250)
    status = IntField()
    photo = StringField(max_length=250)
    likes = ListField()
    dislikes = ListField()
    user = ReferenceField('User', reverse_delete_rule=CASCADE)
    cat = ReferenceField('Category', reverse_delete_rule=CASCADE)
    tags = ListField()


# tag1 = Tag(name='johnny depp')
#
# tag2 = Tag(name='pirate')
#
#
# cat1 = Category(name='film')
# cat2 = Category(name='comedy', parent_cat=cat1)
#
# user1 = User(username='mohammad', email='mohammad@gmail.com', first_name='mohammad', lastname='mohammad',
#              phone_number='09371418637', password='mohammad')
#
#
# post1 = Post(title='pirates', body='loskvmkffvakflv', status=3, user=user1, cat=cat2, likes=[user1])


# print(cat2.id)
# print(post1.tags)
# print(post1.likes)
# x = user1.id
# print(User.objects(id=x)[0].username)

# how to add a picture in mongoengine
# class Animal(Document):
#     genus = StringField()
#     family = StringField()
#     photo = FileField()
#
# marmot = Animal(genus='Marmota', family='Sciuridae'
# with open('marmot.jpg', 'rb') as fd:
#     marmot.photo.put(fd, content_type = 'image/jpeg')
# marmot.save()
# for user in User.objects:
#     print(user.id)



#########################################################################################



<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css"
          crossorigin="anonymous">
    <link rel="stylesheet" href="{{ url_for('static', filename='/css/base.css') }}">
    <link rel="stylesheet" href="{% block css_href %}{% endblock %}">
    <title>{% block title %}{% endblock %}</title>
    {% block style %}{% endblock %}
    {% block extra_head %}{% endblock %}
</head>
<body>
<div class="main-container">
    <div class="header">
        <nav class="container-fluid nav">


            <div class="left_items_in_nav">
                <a href="{{ url_for('blog.home') }}">
        <button type="button" class="btn navs-button">Home</button>
    </a>
    <a href="{{ url_for('blog.login') }}">
        <button type="button" class="btn navs-button">Login</button>
    </a>
    <a href="{{ url_for('blog.sign_up') }}">
        <button type="button" class="btn navs-button">Sign up</button>
    </a>
    <a href="{{ url_for('blog.logout') }}">
        <button type="button" class="btn navs-button">Logout</button>
    </a>
                {% block left_items_in_nav %}{% endblock %}
            </div>

            <div class="right-items-in-nav">
                {% block right_items_in_nav %}{% endblock %}
                <div class="logo-container">
                    <a href="{{ url_for('blog.home') }}">
                        <img src="{{ url_for('static', filename='/img/W.png') }}" class="navbar-logo" alt="w logo">
                    </a>
                </div>
            </div>
        </nav>
        {% block extra_header %}{% endblock %}
    </div>

    <div class="container component">
        <div class="col">
            {% block main %}{% endblock %}
        </div>
    </div>

    <div class="container-fluid footer" id="footer">
        <p style="color: white">This is footer</p> <!--delete this line -->
        {% block extra_footer %}{% endblock %}
    </div>
</div>
</body>
</html>



###################################################################


{% extends 'base.html' %}


<h1>New Post</h1>


{% block main %}
    <div class="container">
        <div class="row">
            <div class="col-sm-9 col-md-7 col-lg-5 mx-auto" id="card-container">
                <div class="card border-0 shadow rounded-3 my-5">
                    <div class="card-body p-4 p-sm-5">
                        <h5 class="card-title text-center mb-5 fw-light fs-5"><b>create post</b></h5>
                        <form action="{{ url_for('blog.create') }}" method="post" enctype="multipart/form-data">
                            <div class="form-floating mb-3">
                                <label for="title">title</label>
                                <input type="text" class="form-control" name='title' id="title">

                            </div>
                            <div class="form-floating mb-3">
                                <label for="password">content of post</label>
                                <textarea name="body" id="body" rows='10' cols="33"></textarea>

                            </div>
                            <div class="form-floating mb-3">
                                <label for="image">image</label><br>
                                <input type="file" name="image" id="image" required style="border-top: 1px solid  black; padding-top: 2px">
                            </div>

                            <div class="d-grid">
                                <button class="btn btn-primary btn-login text-uppercase fw-bold" type="submit">Create
                                    Post
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



###################################################################################################


{% extends 'base.html' %}

{% block title %}
    WebBlog | Home
{% endblock %}

{% block left_items_in_nav %}
    {% if g.user %}
        <a href="{{ url_for('blog.create') }}">
        <button type="button" class="btn navs-button">New</button>
    </a>

    {% endif %}
{% endblock %}
{% block main %}

{% endblock %}
{% block right_items_in_nav %}

    <form class="form-inline search">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn my-2 my-sm-0" type="button">Search</button>
    </form>

{% endblock %}



###############################################################################################


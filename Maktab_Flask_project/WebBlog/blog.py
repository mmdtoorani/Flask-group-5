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
        password_form = hash(request.form["password"])
        error = None



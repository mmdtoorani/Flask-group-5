from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def home():
    return render_template('home.html')

@blog_bp.route("/login/")
def login():
    return render_template('login.html')

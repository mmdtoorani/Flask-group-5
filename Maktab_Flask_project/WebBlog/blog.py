from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
@blog_bp.route('/home')
def home():
    return render_template('base.html')



@blog_bp.route("/login/")
def login():
    return render_template('login.html')


@blog_bp.route("/signup/")
def sign_up():
    return render_template('signup.html')

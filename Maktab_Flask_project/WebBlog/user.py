from flask import Blueprint, render_template, request, url_for, redirect, flash, session
from werkzeug.utils import secure_filename

from WebBlog.LoginRequired import login_required
from WebBlog.db import User, Post, Tag

user_bp = Blueprint('user', __name__)


def get_tags(list_of_names):
    list_of_ids = []
    for tag in Tag.objects:
        if tag.name in list_of_names:
            list_of_ids.append(str(tag.id))
            list_of_names.remove(tag.name)
    if list_of_names:
        for name in list_of_names:
            tag_created = Tag(name= name)
            tag_created.save()
            list_of_ids.append(str(tag_created.id))
    return list_of_ids


@login_required
@user_bp.route("/create", methods=("GET", "POST"))
def create():
    """Create a new post for the current user."""
    if request.method == "POST":
        title_form = request.form["title"]
        body_form = request.form["body"]
        user_id_form = session['user_id']
        f = request.files.get('image')
        tags_form = request.form['tags']
        print(tags_form)
        tags_form_ids = get_tags(tags_form.split(','))
        print(tags_form_ids)
        fname = secure_filename(f.filename)
        f.save('WebBlog/static/img' + fname)
        image = fname
        error = None
        if not title_form:
            error = "Title is required."
        if error is not None:
            flash(error)
        else:
            post_created = Post(
                title=title_form,
                body=body_form,
                user=User.objects(id=user_id_form)[0],
                photo=image,
                tags=tags_form_ids,
            )
            post_created.save()
            return redirect(url_for("blog.home"))
    tags = Tag.objects()
    return render_template("create.html", tags=tags)


@user_bp.route("/posts-list/")
def posts_list():
    """Show all of post that created by the current user."""
    current_users_post = User.objects(id=session["user_id"])[0]
    posts = Post.objects(user=current_users_post)
    return render_template("posts_list.html", posts=posts)


@user_bp.route("/profile/")
def profile():
    current_user = User.objects(id=session["user_id"])[0]
    return render_template("profile.html", user=current_user)


@login_required
@user_bp.route("/edit/<post_id>", methods=("GET", "POST"))
def edit(post_id):
    post = Post.objects(id=post_id)[0]
    if request.method == "POST":
        title_form = request.form["title"]
        body_form = request.form["body"]
        error = None

        if not title_form:
            error = "Title is required."

        if error:
            flash(error)
        else:
            post.title = title_form
            post.body = body_form
            post.save()
            return redirect(url_for("user.posts_list"))

    return render_template("edit.html", post=post)

from flask import Flask
import json
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from db import Post

api_bp = Blueprint('api', __name__)


@api_bp.route("/post_list/")
def list_post():
    posts = []
    for post in Post.objects:
        context = {
            '_id': str(post.id),
            'user_id': str(post.user),
            'title': post.title,
            'photo': post.photo,
            'body': post.body,
        }
        posts.append(context)

    json_post = json.loads(json.dumps(posts))
    return jsonify(json_post)


@api_bp.route("/post_delete/<post_id>")
def post_delete(post_id):
    if request.method == "GET":
        Post.objects(id=post_id).delete()
        return render_template('posts_list.html')


@api_bp.route("/post-deactive/<post_id>")
def post_deactive(post_id):
    status = {
        'ACTIVE': 1,
        'DEACTIVE': 0
    }
    if request.method == "GET":
        if Post.objects(status=status['ACTIVE']):
            Post.objects(status=status['DEACTIVE'])
        return render_template('posts_list.html')


@api_bp.route("/categories-list/")
def list_categories():
    pass


@api_bp.route("/tags-list/")
def list_tags():
    pass


@api_bp.route("/search/")
def search():
    pass


@api_bp.route("/user-profile/<user_id>")
def user_profile(user_id):
    pass

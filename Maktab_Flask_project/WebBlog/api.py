from flask import Blueprint, session, render_template, request, url_for, redirect, jsonify
from WebBlog.db import Post, User
import json
import pprint
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


@api_bp.route("/post-delete/<post_id>")
def post_delete(post_id):
    return Post.objects(id=post_id).delete()


@api_bp.route("/post-deactive/<post_id>")
def post_deactive(post_id):
    pass


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

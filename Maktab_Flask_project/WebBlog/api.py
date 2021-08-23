import json

from flask import Blueprint, jsonify

from WebBlog.db import Post, Tag, Category

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


@api_bp.route("/postdelete/")
def post_delete():
    pass


@api_bp.route("/post-deactive/<post_id>")
def post_deactive(post_id):
    pass


@api_bp.route("/categories-list/")
def list_categories():
    categories_1 = []
    categories_2 = []
    for cat1 in Category.objects(parent_cat=None):
        for cat2 in Category.objects(parent_cat=cat1):
            context2 = {
                'id': str(cat2.id),
                'name': cat2.name
            }
            categories_2.append(context2)
        context1 = {
            'id': str(cat1.id),
            'name': cat1.name,
            'children': categories_2
        }
        categories_1.append(context1)

    json_categories = json.loads(json.dumps(categories_1))
    return jsonify(json_categories)


@api_bp.route("/tags-list/")
def list_tags():
    tags = []
    for tag in Tag.objects:
        context = {
            'id': str(tag.id),
            'name': tag.name,
            'posts': tag.posts,
        }
        tags.append(context)

    json_tags = json.loads(json.dumps(tags))
    return jsonify(json_tags)


@api_bp.route("/search/")
def search():
    pass


@api_bp.route("/user-profile/<user_id>")
def user_profile(user_id):
    pass



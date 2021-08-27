from flask import Flask
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
import json
from WebBlog.db import Post, Tag, Category

api_bp = Blueprint('api', __name__)


@api_bp.route("/post_list/")
def list_post():
    posts = []
    for post in Post.objects:
        img_name = post['photo']
        img_path = f'static/img/{img_name}'
        context = {
            '_id': str(post.id),
            'user_id': str(post.user),
            'title': post.title,
            'photo': post.photo,
            'img_path': img_path,
            'body': post.body,
            'status': post.status,
            'tags': post.tags,
            'num_of_likes': post.num_of_likes,
            'num_of_dislikes': post.num_of_dislikes
        }
        posts.append(context)

    json_post = json.loads(json.dumps(posts))
    return jsonify(json_post)


@api_bp.route("/post_delete/<post_id>")
def post_delete(post_id):
    if request.method == "GET":
        Post.objects(id=post_id).delete()
        return render_template('posts_list.html')


STATUS = {
        'ACTIVE': 1,
        'DEACTIVE': 0
    }


@api_bp.route("/post_deactive/<post_id>")
def post_deactive(post_id):
    if request.method == "GET":
        for post in Post.objects(id=post_id):
            if post.status == STATUS['ACTIVE']:
                # print('THIS IS ACTIVE')
                Post.objects(id=post_id).update(
                    status=STATUS['DEACTIVE']
                )
            elif post.status == STATUS['DEACTIVE']:
                # print('THIS IS DEACTIVE')
                Post.objects(id=post_id).update(
                    status=STATUS['ACTIVE']
                )
        return render_template('posts_list.html')


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


@api_bp.route("/search/<keyword>")
def search(keyword):
    posts = []
    for post in Post.objects:
        if ((keyword in post.tags) or (keyword in post.title) or (keyword in post.body)) and\
                post.status == STATUS['ACTIVE']:
            # print(1)
            # context = {
            #     '_id': str(post.id),
            #     'user_id': str(post.user),
            #     'title': post.title,
            #     'photo': post.photo,
            #     'body': post.body,
            #     'status': post.status,
            #     'tags': post.tags,
            # }
            posts.append(post)
    print(posts)
    # json_post = json.loads(json.dumps(posts))
    return render_template('search_ajax.html', posts=posts)





@api_bp.route("/user-profile/<user_id>")
def user_profile(user_id):
    pass



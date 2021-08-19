from flask import Blueprint, render_template, request, url_for, redirect

api_bp = Blueprint('api', __name__)


@api_bp.route("/post_list/")
def list_post():
    pass


@api_bp.route("/post-delete/<post_id>")
def post_delete():
    pass


@api_bp.route("/post-deactive/<post_id>")
def post_deactive():
    pass


@api_bp.route("/categories-list/")
def list_categories():
    pass


@api_bp.route("/tags-list/")
def list_tags():
    pass


@user_bp.route("/search/")
def search():
    pass


@user_bp.route("/user-profile/<user_id>")
def user_profile():
    pass

import functools
from flask import g, url_for, redirect


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("blog.login"))
        return view(**kwargs)
    return wrapped_view


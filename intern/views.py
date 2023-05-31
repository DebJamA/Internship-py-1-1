from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return "Posts Page"

""" temporarily commented out so app will run
@views.route('/post/<int: post_id>/')
def user_profile(post_id):
    return "Single Page"
"""
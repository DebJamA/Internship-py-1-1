from flask import Flask, Blueprint, render_template, redirect, url_for
from jinja2 import Environment, PackageLoader, select_autoescape
from firebase_admin import db

views = Blueprint("views", __name__)

app = Flask(__name__)

env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

@views.route('/')
def index():
    template = env.get_template('posts.html')
    # Get database reference
    ref = db.reference('blog')
    # Get all articles from reference
    articles = ref.order_by_child('date_posted').get()
    return template.render(articles=articles)

@views.route('/article/<int:post_id>')
def article_single(post_id):
    template = env.get_template('single.html')
    # Get database reference
    ref = db.reference('blog')
    # Get all records from reference
    records = ref.get()
    # Define article variable
    article = {}
    # Iterate all records as item
    for item in records:
        # Check if item has property post_id equal to post_id, if so, add item as article value
        if item.get('post_id') == post_id:
            article = item
            # Break for loop
            break

    return template.render(article=article)

# the following routes just fill the navbar
@views.route("/create")
def create():
    return render_template('create.html')

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/register")
def register():
    return render_template("login.html")

@views.route("/logout")
def logout():
    return redirect(url_for("views.login"))
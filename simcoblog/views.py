from flask import Flask, Blueprint, render_template, redirect, url_for, json
from jinja2 import Environment, PackageLoader, select_autoescape

views = Blueprint("views", __name__)

app = Flask(__name__)

env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

@views.route('/')
def index():
    template = env.get_template('posts.html')
    with open('simcoblog/static/blog.json', 'r') as file:
        articles = json.load(file)
        posts = articles['blog'][0]
    return template.render(articles=posts)

@views.route("/article")
def article_single():
    return render_template('single.html')

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

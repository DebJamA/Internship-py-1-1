from flask import Flask, Blueprint, render_template, redirect, url_for, json
from firebase import firebase
from jinja2 import Environment, PackageLoader, select_autoescape

views = Blueprint("views", __name__)

app = Flask(__name__)
firebase = firebase.FirebaseApplication("https://simco-financial-analyst-blog-default-rtdb.firebaseio.com/", None)

env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# use custom method argument
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods
@views.route('/', methods=['GET', 'POST'])
def index():
    result = firebase.get("/data", None)
    data = json.loads(result)
    return render_template("posts.html", result=data)

@views.route('/article/<int:post_id>')
def article_single(post_id):
    data = firebase.get("simco-financial-analyst-blog-default-rtdb")
    template = env.get_template('single.html')
    return template.render(item=json.loads(data))

# the following routes do not have real functionality
# the buttons redirect to views.index or views.login
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

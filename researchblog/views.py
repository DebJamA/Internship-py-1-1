import os
from flask import Flask, Blueprint, render_template, json

#from jinja2 import Environment, PackageLoader, select_autoescape

views = Blueprint("views", __name__)

app = Flask(__name__)

@views.route('/')
def index():
    """filename = os.path.join(app.static_folder, 'blog_data.json')
    data = 0;
    with open(filename, 'r') as f:
        data = json.load(f)
        f.close()
    return render_template('posts.html', data=data)"""
    return render_template('posts.html')

@views.route('/post/<int:post_id>/')
def article_single(post_id):
    return render_template('single.html')

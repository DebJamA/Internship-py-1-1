from flask import Flask, Blueprint

views = Blueprint("views", __name__)

app = Flask(__name__)

@views.route ('/')
def index ():
    return 'List of Articles' \
           '<br>' \
           'Cant Click Article' \
           '<br>' \
           '<a href="/testing/int:post_id">Click This Fake Article</a>' \
           '<br>' \
           'Cant Go To Article'

@views.route ('/article/int:post_id')
def article_single ():
    return 'This Fake Article' \
           '<br>' \
           'This Fake Article Analysis'

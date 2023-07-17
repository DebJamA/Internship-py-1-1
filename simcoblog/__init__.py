from flask import Flask
import firebase_admin
from firebase_admin import credentials

# fetch service account key JSON file
cred = credentials.Certificate('fbserviceconfig.json')

# initialize SDK with admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://simco-financial-analyst-blog-default-rtdb.firebaseio.com/"
})

def create_app():
    app = Flask(__name__)

    # import blueprints
    from .views import views

    # register blueprints
    app.register_blueprint(views, url_prefix="/")

    return app

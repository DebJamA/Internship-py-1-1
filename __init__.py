from flask import Flask

def create_app():
    app = Flask(__name__)

# import blueprints
    from .views import views

# register blueprints
    app.register_blueprint(views, url_prefix="/")

    return app
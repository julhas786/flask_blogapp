from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .views import views
from .auth import auth


def create_app():
    app = Flask(__name__)    
    # Initialize your app with configurations, blueprints, etc.
    app.config['SECRET_KEY'] = "myblogapp"    


    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
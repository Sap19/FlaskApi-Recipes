#initializing the application
import os
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from itsdangerous import URLSafeTimedSerializer



api = Api()
url = URLSafeTimedSerializer('recipes')


def create_app(test_config=None, instance_relative_config=False):
    app = Flask(__name__, instance_relative_config=True)
    api.init_app(app)
    app.config.from_object("config.Config")
    register_blueprints(app)

    return app

def register_extensions(app, db):
    CORS(app)
    return None

def register_blueprints(app):
    #routes
    from recipes.routes import recipes
    app.register_blueprint(recipes)
    return None



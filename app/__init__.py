from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Bootstrap(app)

    return app
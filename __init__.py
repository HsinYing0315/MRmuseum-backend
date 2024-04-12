from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

from .config import config

db = SQLAlchemy()

def create_app(config_mode):
    app = Flask(__name__)
    Swagger(app)
    app.config.from_object(config[config_mode])

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
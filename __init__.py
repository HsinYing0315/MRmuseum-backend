from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# from config import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://melody:nccu306@postgres:5432/graduation'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

import sys, os
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

# from config import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://melody:nccu306@localhost:5432/graduation'

    db.init_app(app)
    Migrate(app, db)
    with app.app_context():
        db.create_all()

    return app
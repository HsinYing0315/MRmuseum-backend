from fastapi import FastAPI
from database import Base, engine
# from migrate import Migrate

import sys, os
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

def create_app():
    app = FastAPI()

    # Migrate(app, db)
    Base.metadata.create_all(bind=engine)

    return app
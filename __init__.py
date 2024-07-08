from fastapi import FastAPI
from database import Base, engine

import sys, os
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

def create_app():
    app = FastAPI()

    from models.visitor import Visitor
    from models.exhibit.exhibit import Exhibit
    from models.exhibit.exhibitGroup import ExhibitGroup
    from models.exhibit.time import Time
    from models.exhibit.area import Area
    from models.test.test import Test
    from models.test.answer import Answer
    from models.interaction import Interaction
    from models.questionnaire import Questionnaire
    Base.metadata.create_all(bind=engine)

    return app
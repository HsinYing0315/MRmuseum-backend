from flask import jsonify, request
import uuid
from models.questionnaire import Questionnaire
from __init__ import db

def create_Questionnaire():
    data = request.json
    id = str(uuid.uuid4())
    new_interaction = Questionnaire(
                          id             = id,
                          interactionScore    = data['interactionScore'],
                          educationScore      = data['educationScore'],
                          entertainmentScore  = data['entertainmentScore'],
                          overallScore        = data['overallScore'],
                          willVisitAgain      = data['willVisitAgain'],
                          visitorID       = data['visitorID'],
                          )
    db.session.add(new_interaction)
    db.session.commit()

    response = Questionnaire.query.get(id).toDict()
    return jsonify(response)

from flask import jsonify, request
import uuid
from ..models.questionnaire import Questionnaire
from .. import db

def create_Questionnaire():
    request_form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_interaction = Questionnaire(
                          id             = id,
                          interactionScore    = request_form['interactionScore'],
                          educationScore      = request_form['educationScore'],
                          entertainmentScore  = request_form['entertainmentScore'],
                          overallScore        = request_form['overallScore'],
                          willVisitAgain      = request_form['willVisitAgain'],
                          visitorID       = request_form['visitorID'],
                          )
    db.session.add(new_interaction)
    db.session.commit()

    response = Questionnaire.query.get(id).toDict()
    return jsonify(response)

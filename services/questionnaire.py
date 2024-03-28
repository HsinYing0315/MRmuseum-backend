from flask import jsonify
from ..models.questionnaire import Questionnaire

def list_all_questionnaires():
    questionnaires = Questionnaire.query.all()
    response = []
    for questionnaire in questionnaires: response.append(questionnaire.toDict())
    return jsonify(response)
 
def get_questionnaire(questionnaire_id):
    response = Questionnaire.query.get(questionnaire_id).toDict()
    return jsonify(response)
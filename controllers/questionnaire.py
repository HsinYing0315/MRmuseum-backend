from flask import Blueprint
from ..services.questionnaire import list_all_questionnaires, get_questionnaire

questionnaire_blueprint = Blueprint('questionnaire_blueprint', __name__)

@questionnaire_blueprint.route('/', methods=['GET'])
def list_all_questionnaires_controller():
    
    return list_all_questionnaires()

@questionnaire_blueprint.route('/<questionnaire_id>', methods=['GET'])
def get_questionnaire_controller(questionnaire_id):
    return get_questionnaire(questionnaire_id)
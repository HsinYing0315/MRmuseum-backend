from flask import Blueprint
from ..services.questionnaire import create_Questionnaire

questionnaire_blueprint = Blueprint('questionnaire_blueprint', __name__)

@questionnaire_blueprint.route('/add', methods=['POST'])
def add_questionnaire_controller():
    
    return create_Questionnaire()
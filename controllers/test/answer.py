from flask import Blueprint
from ...services.test.answer import list_all_answers, get_answer

answer_blueprint = Blueprint('answer_blueprint', __name__)

@answer_blueprint.route('/', methods=['GET'])
def list_all_answers_controller():
    
    return list_all_answers()

@answer_blueprint.route('/<answer_id>', methods=['GET'])
def get_answer_controller(answer_id):
    return get_answer(answer_id)
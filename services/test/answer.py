from flask import jsonify
from models.test.answer import Answer

def list_all_answers():
    answers = Answer.query.all()
    response = []
    for answer in answers: response.append(answer.toDict())
    return jsonify(response)
 
def get_answer(answer_id):
    response = Answer.query.get(answer_id).toDict()
    return jsonify(response)
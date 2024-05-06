from flask import Blueprint
from services.test.test import list_all_tests, get_test

test_blueprint = Blueprint('test_blueprint', __name__)

@test_blueprint.route('/', methods=['GET'])
def list_all_tests_controller():
    
    return list_all_tests()

@test_blueprint.route('/<test_id>', methods=['GET'])
def get_test_controller(test_id):
    return get_test(test_id)
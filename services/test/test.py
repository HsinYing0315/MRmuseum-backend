from flask import jsonify
from ...models.test.test import Test

def list_all_tests():
    tests = Test.query.all()
    response = []
    for test in tests: response.append(test.toDict())
    return jsonify(response)
 
def get_test(test_id):
    response = Test.query.get(test_id).toDict()
    return jsonify(response)
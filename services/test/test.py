from fastapi.responses import JSONResponse
from models.test.test import Test

def list_all_tests():
    tests = Test.query.all()
    response = []
    for test in tests: response.append(test.toDict())
    return JSONResponse(content=response)
 
def get_test(test_id):
    if (Test.query.filter_by(id=test_id).first() is None):
        return JSONResponse(status_code=404, content={"message": "Test with id " + test_id + " is not found"})
    
    response = Test.query.get(test_id).toDict()
    return JSONResponse(content=response)
from fastapi.responses import JSONResponse
from database import session
from models.test.test import Test

def list_all_tests():
    tests = session.query(Test).all()
    response = []
    for test in tests: response.append(test.toDict())
    return JSONResponse(content=response)
 
def get_test(test_id):
    if (session.query(Test).filter_by(id=test_id).first() is None):
        return JSONResponse(status_code=404, content={"message": "Test with id " + test_id + " is not found"})
    
    response = session.query(Test).get(test_id).toDict()
    return JSONResponse(content=response)
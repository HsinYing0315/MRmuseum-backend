from fastapi.responses import JSONResponse
from database import session
from models.test.test import Test

def list_all_tests():
    tests = session.query(Test).all()
    response = []
    for test in tests: 
        test = test.toDict()
        test['created'] = test['created'].strftime("%Y-%m-%d %H:%M:%S")
        test['updated'] = test['updated'].strftime("%Y-%m-%d %H:%M:%S")
        response.append(test)
    return JSONResponse(content=response)
 
def get_test(test_id):
    if (session.query(Test).filter_by(id=test_id).first() is None):
        return JSONResponse(status_code=404, content={"message": "Test with id " + test_id + " is not found"})
    
    response = session.query(Test).get(test_id).toDict()
    response['created'] = response['created'].strftime("%Y-%m-%d %H:%M:%S")  
    response['updated'] = response['updated'].strftime("%Y-%m-%d %H:%M:%S")
    return JSONResponse(content=response)
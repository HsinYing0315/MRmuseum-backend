from fastapi.responses import JSONResponse
from database import session
from models.test.answer import Answer

def list_all_answers():
    answers = session.query(Answer).all()
    response = []
    for answer in answers: 
        answer = answer.toDict()
        answer['created'] = answer['created'].strftime("%Y-%m-%d %H:%M:%S")
        answer['updated'] = answer['updated'].strftime("%Y-%m-%d %H:%M:%S")
        response.append(answer)
    return JSONResponse(content=response)
 
def get_answer(answer_id):
    if (session.query(Answer).filter_by(id=answer_id).first() is None):
        return JSONResponse(status_code=404, content={"message": "Answer with id " + answer_id + " is not found"})
    
    response = session.query(Answer).get(answer_id).toDict()
    response['created'] = response['created'].strftime("%Y-%m-%d %H:%M:%S") 
    response['updated'] = response['updated'].strftime("%Y-%m-%d %H:%M:%S")
    return JSONResponse(content=response)
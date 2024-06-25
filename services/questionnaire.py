from fastapi.responses import JSONResponse
import uuid
from models.questionnaire import Questionnaire
from database import session

def create_Questionnaire():
    data = request.json
    id = str(uuid.uuid4())
    new_interaction = Questionnaire(
                          id             = id,
                          interactionScore    = data['interactionScore'],
                          educationScore      = data['educationScore'],
                          entertainmentScore  = data['entertainmentScore'],
                          overallScore        = data['overallScore'],
                          willVisitAgain      = data['willVisitAgain'],
                          visitorID       = data['visitorID'],
                          )
    session.add(new_interaction)
    session.commit()

    response = session.query(Questionnaire).get(id).toDict()
    return JSONResponse(content=response)

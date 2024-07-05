from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid
from models.questionnaire import Questionnaire
from database import Session

class QuestionnaireSchema(BaseModel):
    interactionScore: int
    educationScore: int
    entertainmentScore: int
    overallScore: int
    willVisitAgain: bool
    visitorID: str
def create_Questionnaire(questionnaire: QuestionnaireSchema):
    id = str(uuid.uuid4())
    new_interaction = Questionnaire(
                          id             = id,
                          interactionScore    = questionnaire.interactionScore,
                          educationScore      = questionnaire.educationScore,
                          entertainmentScore  = questionnaire.entertainmentScore,
                          overallScore        = questionnaire.overallScore,
                          willVisitAgain      = questionnaire.willVisitAgain,
                          visitorID       = questionnaire.visitorID,
                          )
    
    with Session() as session:
        session.add(new_interaction)
        session.commit()

    return JSONResponse(content="Questionnaire recorded")

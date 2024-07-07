from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid
from models.questionnaire import Questionnaire
from database import session, commit

import matplotlib.pyplot as plt
from io import BytesIO

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
    
    with commit():
        session.add(new_interaction)

    return JSONResponse(content="Questionnaire recorded")

def get_average_score():
    if (len(session.query(Questionnaire).all()) == 0): return None
    total = len(session.query(Questionnaire).all())
    interactions = 0
    educations = 0
    entertainments = 0
    overalls = 0
    
    for score in session.query(Questionnaire.interactionScore).all(): interactions += score[0]
    for score in session.query(Questionnaire.educationScore).all(): educations += score[0]
    for score in session.query(Questionnaire.entertainmentScore).all(): entertainments += score[0]
    for score in session.query(Questionnaire.overallScore).all(): overalls += score[0]
    
    plt.bar(['Interaction', 'Education', 'Entertainment', 'Overall'], [interactions / total, educations / total, entertainments / total, overalls / total])
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    
    # Return as a file response
    return buffer
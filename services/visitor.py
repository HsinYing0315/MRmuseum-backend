from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid

from database import session, commit
from models.visitor import Visitor
from models import Interaction, Questionnaire

def get_visitors():
    visitors = session.query(Visitor).all()
    response = []
    for visitor in visitors: 
        visitor = visitor.toDict()
        
        interactions = session.query(Interaction).filter_by(visitorID=visitor['id']).all()
        questionnaire = session.query(Questionnaire).filter_by(visitorID=visitor['id']).first()
        
        visitor['interaction'] = []
        for interaction in interactions:
            interaction = interaction.toDict()
            visitor['interaction'].append(interaction)
            
        visitor['questionnaire'] = questionnaire
        response.append(visitor)
    return JSONResponse(content=response)

def get_visitor(id: str):
    response = session.query(Visitor).get(id)
    if (response is None):
        return JSONResponse(status_code=404, content={"message": "Visitor with id " + id + " is not found"})
    
    interactions = session.query(Interaction).filter_by(visitorID=id).all()
    questionnaire = session.query(Questionnaire).filter_by(visitorID=id).first()
   
    visitor = response.toDict()
    visitor['interaction'] = []
    for interaction in interactions:
        interaction = interaction.toDict()
        visitor['interaction'].append(interaction)
        
    visitor['questionnaire'] = questionnaire
    visitor['created'] = visitor['created'].strftime("%Y-%m-%d %H:%M:%S")
    visitor['updated'] = visitor['updated'].strftime("%Y-%m-%d %H:%M:%S")
    return JSONResponse(content=visitor)

class VisitorSchema(BaseModel):
    age: int
    count: str
    type: str
    interests: str
    gender: str
def create_visitor(visitor: VisitorSchema):
    id = str(uuid.uuid4())
    new_visitor = Visitor(
                          id             = id,
                          age          = visitor.age,
                          count       = visitor.count,
                          type        = visitor.type,
                          interests   = visitor.interests,
                          gender      = visitor.gender
                          )
    with commit():
        session.add(new_visitor)
    return JSONResponse(content={"id": id})

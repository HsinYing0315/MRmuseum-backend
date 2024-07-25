from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid

from database import session, commit
from models.visitor import Visitor

def get_visitors():
    visitors = session.query(Visitor).all()
    if (visitors is None):
        return JSONResponse(status_code=404, content={"message": "No visitors found"})
    response = []
    for visitor in visitors: 
        visitor = visitor.toDict()
        response.append(visitor)
    return JSONResponse(content=response)

def get_visitor(id: str):
    response = session.query(Visitor).get(id)
    if (response is None):
        return JSONResponse(status_code=404, content={"message": "Visitor with id " + id + " is not found"})
    
    visitor = response.toDict()
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

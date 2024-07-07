from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid

from database import session, commit
from models.visitor import Visitor

class VisitorSchema(BaseModel):
    age: int
    count: str
    type: str
def create_visitor(visitor: VisitorSchema):
    id = str(uuid.uuid4())
    new_visitor = Visitor(
                          id             = id,
                          age          = visitor.age,
                          count       = visitor.count,
                          type        = visitor.type,
                          )
    with commit():
        session.add(new_visitor)
    return JSONResponse(content={"id": id})

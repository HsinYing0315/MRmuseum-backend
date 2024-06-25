from fastapi.responses import JSONResponse
import uuid

from database import session
from models.visitor import Visitor

def create_visitor():
    data = request.json

    id = str(uuid.uuid4())
    new_visitor = Visitor(
                          id             = id,
                          age          = data.get('age'),
                          count       = data.get('count'),
                          type        = data.get('type'),
                          )
    session.add(new_visitor)
    session.commit()

    response = Visitor.query.get(id).toDict()
    return JSONResponse(content=response)

from fastapi.responses import JSONResponse
from database import session
from models.exhibit.area import Area

def get_area(name):
    if (session.query(Area).filter_by(name=name).first() is None):
        return JSONResponse(status_code=404, content={"message": "Area with name " + name + " is not found"})
    response = session.query(Area).filter_by(name=name).first().toDict()
    
    area = {
        'name': response['name'],
        'introduction': response['introduction'],
    }

    return JSONResponse(status_code=200, content=area)

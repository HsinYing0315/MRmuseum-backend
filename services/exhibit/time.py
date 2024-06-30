from fastapi.responses import JSONResponse
from database import session
from models.exhibit.time import Time

def get_time(area_id, name):
    response = session.query(Time).filter_by(areaID=area_id, name=name).first().toDict()
    if (response is None):
        return JSONResponse(status_code=404, content={"message": "Time with name " + name + " is not found"})
    response['created'] = response['created'].strftime("%Y-%m-%d %H:%M:%S")
    response['updated'] = response['updated'].strftime("%Y-%m-%d %H:%M:%S")
    return JSONResponse(content=response)

from fastapi.responses import JSONResponse
from database import session
from models.exhibit.exhibit import Exhibit
def list_all_exhibits_by_time(time_id):
    exhibits = session.query(Exhibit).filter_by(timeID=time_id).all()
    if (exhibits is None):
        return JSONResponse(status_code=404, content={"message": "Exhibits with time " + time_id + " is not found"})
    response = []
    for exhibit in exhibits: response.append(exhibit.toDict())
    return JSONResponse(content=response)


def get_exhibit(exhibit_id):
    response = session.query(Exhibit).get(exhibit_id).toDict()
    if (response is None):
        return JSONResponse(status_code=404, content={"message": "Exhibit with id " + exhibit_id + " is not found"})
    return JSONResponse(content=response)

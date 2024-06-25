from fastapi.responses import JSONResponse
from database import session
from models.exhibit.exhibitGroup import ExhibitGroup

def list_all_exhibitGroups():
    exhibitGroups = session.query(ExhibitGroup).all()
    response = []
    for exhibitGroup in exhibitGroups: response.append(exhibitGroup.toDict())
    return JSONResponse(content=response)
 
def get_exhibitGroup(exhibitGroup_id):
    response = session.query(ExhibitGroup).get(exhibitGroup_id).toDict()
    if (response is None):
        return JSONResponse(status_code=404, content={"message": "ExhibitGroup with id " + exhibitGroup_id + " is not found"})
    return JSONResponse(content=response)

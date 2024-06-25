from fastapi.responses import JSONResponse
from models.exhibit.exhibitGroup import ExhibitGroup

def list_all_exhibitGroups():
    exhibitGroups = ExhibitGroup.query.all()
    response = []
    for exhibitGroup in exhibitGroups: response.append(exhibitGroup.toDict())
    return JSONResponse(content=response)
 
def get_exhibitGroup(exhibitGroup_id):
    response = ExhibitGroup.query.get(exhibitGroup_id).toDict()
    if (response is None):
        return JSONResponse(status_code=404, content={"message": "ExhibitGroup with id " + exhibitGroup_id + " is not found"})
    return JSONResponse(content=response)

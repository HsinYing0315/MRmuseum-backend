from flask import jsonify

from ..models.area import Area

def list_all_areas():
    areas = Area.query.all()
    response = []
    for area in areas: response.append(area.toDict())
    return jsonify(response)
 
def get_area(area_id):
    response = Area.query.get(area_id).toDict()
    return jsonify(response)

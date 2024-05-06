from flask import jsonify

from models.exhibit.exhibitGroup import ExhibitGroup

def list_all_exhibitGroups():
    exhibitGroups = ExhibitGroup.query.all()
    response = []
    for exhibitGroup in exhibitGroups: response.append(exhibitGroup.toDict())
    return jsonify(response)
 
def get_exhibitGroup(exhibitGroup_id):
    response = ExhibitGroup.query.get(exhibitGroup_id).toDict()
    return jsonify(response)

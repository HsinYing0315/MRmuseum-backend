from flask import jsonify

from ...models.exhibit.exhibit import Exhibit

def list_all_exhibits():
    exhibits = Exhibit.query.all()
    response = []
    for exhibit in exhibits: response.append(exhibit.toDict())
    return jsonify(response)
 
def get_exhibit(exhibit_id):
    response = Exhibit.query.get(exhibit_id).toDict()
    return jsonify(response)

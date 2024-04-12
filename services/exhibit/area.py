from flask import jsonify

from ...models.exhibit.area import Area

def get_area(location):
    response = Area.query.get(location).toDict()
    return jsonify(response)

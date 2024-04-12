from flask import jsonify

from ...models.exhibit.time import Time

def get_time(area_id, location):
    times = Time.query.filter_by(areaID=area_id, location=location).all()
    if (times is None):
        return jsonify([])
    response = []
    for time in times: response.append(time.toDict())
    return jsonify(response)

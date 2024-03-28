from flask import jsonify

from ...models.exhibit.time import Time

def list_all_times():
    times = Time.query.all()
    response = []
    for time in times: response.append(time.toDict())
    return jsonify(response)
 
def get_time(time_id):
    response = Time.query.get(time_id).toDict()
    return jsonify(response)

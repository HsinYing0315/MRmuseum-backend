from flask import jsonify

from ...models.exhibit.exhibit import Exhibit
def list_all_exhibits_by_time(time_id):
    exhibits = Exhibit.query.filter_by(timeID=time_id).all()
    if (exhibits is None):
        return jsonify([])
    response = []
    for exhibit in exhibits: response.append(exhibit.toDict())
    return jsonify(response)


def get_exhibit(exhibit_id):
    response = Exhibit.query.get(exhibit_id).toDict()
    return jsonify(response)

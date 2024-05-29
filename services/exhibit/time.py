from flask import jsonify

from models.exhibit.time import Time

def get_time(area_id, name):
    response = Time.query.filter_by(areaID=area_id, name=name).first().toDict()
    if (response is None):
        return jsonify({})
    
    time = jsonify({
        'name': response['name'],
        'introduction': response['introduction'],
    })
    
    return time

from flask import jsonify

from models.exhibit.area import Area

def get_area(name):
    if (Area.query.filter_by(name=name).first() is None):
        return jsonify({})
    response = Area.query.filter_by(name=name).first().toDict()
    
    area = jsonify({
        'name': response['name'],
        'introduction': response['introduction'],
    })

    return area

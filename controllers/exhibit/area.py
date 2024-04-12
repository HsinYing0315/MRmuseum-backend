from flask import Blueprint
from ...services.exhibit.area import get_area

area_blueprint = Blueprint('area_blueprint', __name__)

@area_blueprint.route('/<location>', methods=['GET'])
def get_area_controller(location):
    return get_area(location)
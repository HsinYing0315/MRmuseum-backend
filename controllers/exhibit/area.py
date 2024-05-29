from flask import Blueprint
from services.exhibit.area import get_area

area_blueprint = Blueprint('area_blueprint', __name__)

@area_blueprint.route('/<name>', methods=['GET'])
def get_area_controller(name):
    return get_area(name)
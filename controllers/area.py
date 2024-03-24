from flask import Blueprint
from ..services.area import list_all_areas, get_area

area_blueprint = Blueprint('area_blueprint', __name__)

@area_blueprint.route('/', methods=['GET'])
def list_all_areas_controller():
    
    return list_all_areas()

@area_blueprint.route('/<area_id>', methods=['GET'])
def get_area_controller(area_id):
    return get_area(area_id)
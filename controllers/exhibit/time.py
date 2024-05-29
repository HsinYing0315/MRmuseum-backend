from flask import Blueprint
from services.exhibit.time import get_time

time_blueprint = Blueprint('time_blueprint', __name__)

@time_blueprint.route('/<area_id>/<name>', methods=['GET'])
def get_time_controller(area_id, name):
    
    return get_time(area_id, name)
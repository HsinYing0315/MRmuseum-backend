from flask import Blueprint
from ...services.exhibit.time import list_all_times, get_time

time_blueprint = Blueprint('time_blueprint', __name__)

@time_blueprint.route('/', methods=['GET'])
def list_all_times_controller():
    
    return list_all_times()

@time_blueprint.route('/<time_id>', methods=['GET'])
def get_time_controller(time_id):
    return get_time(time_id)
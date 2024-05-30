from flask import Blueprint
from services.exhibit.exhibit import get_exhibit, list_all_exhibits_by_time

exhibit_blueprint = Blueprint('exhibit_blueprint', __name__)

@exhibit_blueprint.route('/<time_id>', methods=['GET'])
def get_all_exhibits_controller(time_id):
    return list_all_exhibits_by_time(time_id)

@exhibit_blueprint.route('/<exhibit_id>', methods=['GET'])
def get_exhibit_controller(exhibit_id):
    return get_exhibit(exhibit_id)
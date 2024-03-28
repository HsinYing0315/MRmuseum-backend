from flask import Blueprint
from ...services.exhibit.exhibit import list_all_exhibits, get_exhibit

exhibit_blueprint = Blueprint('exhibit_blueprint', __name__)

@exhibit_blueprint.route('/', methods=['GET'])
def list_all_exhibits_controller():
    
    return list_all_exhibits()

@exhibit_blueprint.route('/<exhibit_id>', methods=['GET'])
def get_exhibit_controller(exhibit_id):
    return get_exhibit(exhibit_id)
from flask import Blueprint
from services.exhibit.exhibit import get_exhibit

exhibit_blueprint = Blueprint('exhibit_blueprint', __name__)

@exhibit_blueprint.route('/<exhibit_id>', methods=['GET'])
def get_exhibit_controller(exhibit_id):
    return get_exhibit(exhibit_id)
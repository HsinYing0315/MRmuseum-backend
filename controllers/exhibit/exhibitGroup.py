from flask import Blueprint
from services.exhibit.exhibitGroup import list_all_exhibitGroups, get_exhibitGroup

exhibitGroup_blueprint = Blueprint('exhibitGroup_blueprint', __name__)

@exhibitGroup_blueprint.route('/', methods=['GET'])
def list_all_exhibitGroups_controller():
    
    return list_all_exhibitGroups()

@exhibitGroup_blueprint.route('/<exhibitGroup_id>', methods=['GET'])
def get_exhibitGroup_controller(exhibitGroup_id):
    return get_exhibitGroup(exhibitGroup_id)
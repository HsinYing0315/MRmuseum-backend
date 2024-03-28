from flask import Blueprint, request
from ..services.interaction import list_all_interactions, get_interaction, create_interaction 

interaction_blueprint = Blueprint('interaction_blueprint', __name__)

@interaction_blueprint.route('/', methods=['GET'])
def list_all_interactions_controller():
    
    return list_all_interactions()

@interaction_blueprint.route('/<interaction_id>', methods=['GET'])
def get_interaction_controller(interaction_id):
    
    return get_interaction(interaction_id)
    
@interaction_blueprint.route('/add', methods=['POST'])
def add_interaction_controller():
    
    return create_interaction()

from flask import Blueprint, request
from services.interaction import create_interaction 

interaction_blueprint = Blueprint('interaction_blueprint', __name__)
   
@interaction_blueprint.route('/add', methods=['POST'])
def add_interaction_controller():
    
    return create_interaction()

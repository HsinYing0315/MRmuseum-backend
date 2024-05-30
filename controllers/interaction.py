from flask import Blueprint, request
from services.interaction import create_interaction 

interaction_blueprint = Blueprint('interaction_blueprint', __name__)
   
@interaction_blueprint.route('/add', methods=['POST'])
def add_interaction_controller():
    data = request.json
    interaction = {
        'type': data['type'],
        'content': data['content'],
        'visitorID': data['visitorID'],
        'exhibitID': data['exhibitID']
    }
    
    return create_interaction(interaction)

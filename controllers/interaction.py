from flask import Blueprint, request
from services.interaction import create_interaction, get_interaction_count, get_interaction_duration 

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

@interaction_blueprint.route('/count/<visitorID>', methods=['GET'])
def get_interaction_count_controller(visitorID):
    return get_interaction_count(visitorID)

@interaction_blueprint.route('/duration/<visitorID>', methods=['GET'])
def get_interaction_duration_controller(visitorID):
    return get_interaction_duration(visitorID)

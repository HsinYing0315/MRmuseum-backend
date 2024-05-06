from flask import Blueprint
from services.NPC import meet_NPC, interact_NPC 

NPC_blueprint = Blueprint('NPC_blueprint', __name__)
   
@NPC_blueprint.route('/<NPC_id>', methods=['GET'])
def meet_NPC_controller():
    
    return meet_NPC()

@NPC_blueprint.route('/<NPC_id>', methods=['GET'])
def interact_NPC_controller():
    
    return interact_NPC()

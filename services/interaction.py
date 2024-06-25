from flask import jsonify
import uuid

from __init__ import db
from models.interaction import Interaction

def create_interaction(interaction):
    
    id = str(uuid.uuid4())
    new_interaction = Interaction(
                          id             = id,
                          type            = interaction['type'],
                          content        = interaction['content'],
                          visitorID       = interaction['visitorID'],
                          exhibitID       = interaction['exhibitID'],
                          )
    db.session.add(new_interaction)
    db.session.commit()

    response = Interaction.query.get(id).toDict()
    return jsonify(response)

def get_interaction_count(visitorID):
    interactions = Interaction.query.filter_by(visitorID=visitorID).all()
    return len(interactions)

def get_interaction_duration(visitorID):
    interactions = Interaction.query.filter_by(visitorID=visitorID, type='duration').all()
    if (interactions is None):
        return 0
    total = 0
    for interaction in interactions:
        interaction = interaction.toDict()
        total += interaction['content']
        
    return total / len(interactions)

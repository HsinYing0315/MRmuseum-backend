from flask import request, jsonify
import uuid

from __init__ import db
from models.interaction import Interaction

def create_interaction(interaction):
    
    id = str(uuid.uuid4())
    new_interaction = Interaction(
                          id             = id,
                          question        = interaction['question'],
                          visitorID       = interaction['visitorID'],
                          exhibitID       = interaction['exhibitID'],
                          )
    db.session.add(new_interaction)
    db.session.commit()

    response = Interaction.query.get(id).toDict()
    return jsonify(response)

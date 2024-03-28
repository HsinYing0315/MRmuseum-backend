from flask import request, jsonify
import uuid

from .. import db
from ..models.interaction import Interaction

def list_all_interactions():
    interactions = Interaction.query.all()
    response = []
    for interaction in interactions: response.append(interaction.toDict())
    return jsonify(response)
 
def create_interaction():
    request_form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_interaction = Interaction(
                          id             = id,
                          age          = request_form['age'],
                          count       = request_form['count'],
                          )
    db.session.add(new_interaction)
    db.session.commit()

    response = Interaction.query.get(id).toDict()
    return jsonify(response)

def get_interaction(interaction_id):
    response = Interaction.query.get(interaction_id).toDict()
    return jsonify(response)
from flask import request, jsonify
import uuid

from __init__ import db
from models.interaction import Interaction

def create_interaction():
    request_form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_interaction = Interaction(
                          id             = id,
                          question        = request_form['question'],
                          visitorID       = request_form['visitorID'],
                          exhibitID       = request_form['exhibitID'],
                          )
    db.session.add(new_interaction)
    db.session.commit()

    response = Interaction.query.get(id).toDict()
    return jsonify(response)

from flask import request, jsonify
import uuid

from __init__ import db
from models.visitor import Visitor

def create_visitor():
    data = request.json

    id = str(uuid.uuid4())
    new_visitor = Visitor(
                          id             = id,
                          age          = data.get('age'),
                          count       = data.get('count'),
                          type        = data.get('type'),
                          )
    db.session.add(new_visitor)
    db.session.commit()

    response = Visitor.query.get(id).toDict()
    return jsonify(response)

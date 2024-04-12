from flask import request, jsonify
import uuid

from .. import db
from ..models.visitor import Visitor

def create_visitor():
    request_form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_visitor = Visitor(
                          id             = id,
                          age          = request_form['age'],
                          count       = request_form['count'],
                          )
    db.session.add(new_visitor)
    db.session.commit()

    response = Visitor.query.get(id).toDict()
    return jsonify(response)

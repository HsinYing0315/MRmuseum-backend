from flask import request, jsonify
import uuid

from .. import db
from ..models.visitor import Visitor

def list_all_visitors():
    visitors = Visitor.query.all()
    response = []
    for visitor in visitors: response.append(visitor.toDict())
    return jsonify(response)
 
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

def get_visitor(visitor_id):
    response = Visitor.query.get(visitor_id).toDict()
    return jsonify(response)

def delete_visitor(visitor_id):
    Visitor.query.filter_by(id=visitor_id).delete()
    db.session.commit()

    return ('visitor with Id "{}" deleted successfully!').format(visitor_id)
from flask import Blueprint, request
from ..services.visitor import list_all_visitors, get_visitor, delete_visitor, create_visitor 

visitor_blueprint = Blueprint('visitor_blueprint', __name__)

@visitor_blueprint.route('/', methods=['GET'])
def list_all_visitors_controller():
    
    return list_all_visitors()

@visitor_blueprint.route('/<visitor_id>', methods=['GET', 'DELETE'])
def get_visitor_controller(visitor_id):
    if request.method == 'GET': return get_visitor(visitor_id)
    elif request.method == 'DELETE': return delete_visitor(visitor_id)
    else: return 'method not allowed'
    
@visitor_blueprint.route('/add', methods=['POST'])
def add_visitor_controller():
    
    return create_visitor()

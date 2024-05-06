from flask import Blueprint
from flasgger.utils import swag_from
from services.visitor import create_visitor 

visitor_blueprint = Blueprint('visitor_blueprint', __name__)
    
@visitor_blueprint.route('/add', methods=['POST'])
@swag_from('../docs/visitor.yml')
def add_visitor_controller():
    
    return create_visitor()

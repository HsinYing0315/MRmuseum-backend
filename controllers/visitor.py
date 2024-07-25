from fastapi import APIRouter
from services.visitor import create_visitor, get_visitors, get_visitor, VisitorSchema

visitor_router = APIRouter(prefix='/visitor', tags=['visitor'])
    

@visitor_router.get('')
def get_visitors_controller():
    
    return get_visitors()

@visitor_router.get('/{id}')
def get_visitor_controller(id: str):
    
    return get_visitor(id)

@visitor_router.post('/add')
def add_visitor_controller(visitor: VisitorSchema):
    
    return create_visitor(visitor)

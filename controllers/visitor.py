from fastapi import APIRouter
from services.visitor import create_visitor, VisitorSchema

visitor_router = APIRouter(prefix='/visitor', tags=['visitor'])
    
@visitor_router.post('/add')
def add_visitor_controller(visitor: VisitorSchema):
    
    return create_visitor(visitor)

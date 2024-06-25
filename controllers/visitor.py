from fastapi import APIRouter
from services.visitor import create_visitor 

visitor_router = APIRouter(prefix='/visitor', tags=['visitor'])
    
@visitor_router.post('/add')
def add_visitor_controller():
    
    return create_visitor()

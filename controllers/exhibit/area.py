from fastapi import APIRouter
from services.exhibit.area import get_area

area_router = APIRouter(prefix='/area', tags=['area'])

@area_router.get('/{name}')
def get_area_controller(name):
    return get_area(name)
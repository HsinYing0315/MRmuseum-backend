from fastapi import APIRouter
from services.exhibit.time import get_time

time_router = APIRouter(prefix='/time', tags=['time'])

@time_router.get('/{area_id}/{name}')
def get_time_controller(area_id, name):
    
    return get_time(area_id, name)
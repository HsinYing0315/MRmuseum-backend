from fastapi import APIRouter
from services.exhibit.exhibit import get_exhibit, list_all_exhibits_by_time

exhibit_router = APIRouter(prefix='/exhibit', tags=['exhibit'])

@exhibit_router.get('/{time_id}')
def get_all_exhibits_controller(time_id):
    return list_all_exhibits_by_time(time_id)

@exhibit_router.get('/{exhibit_id}')
def get_exhibit_controller(exhibit_id):
    return get_exhibit(exhibit_id)
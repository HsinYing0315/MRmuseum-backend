from fastapi import APIRouter
from services.exhibit.exhibitGroup import list_all_exhibitGroups, get_exhibitGroup

exhibitGroup_router = APIRouter(prefix='/exhibitGroup', tags=['exhibitGroup'])

@exhibitGroup_router.get('/')
def list_all_exhibitGroups_controller():
    
    return list_all_exhibitGroups()

@exhibitGroup_router.get('/<exhibitGroup_id>')
def get_exhibitGroup_controller(exhibitGroup_id):
    return get_exhibitGroup(exhibitGroup_id)
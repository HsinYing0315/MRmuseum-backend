from fastapi import APIRouter
from pydantic import BaseModel
from services.interaction import create_interaction, get_interaction_count, get_interaction_duration 

interaction_router = APIRouter(prefix='/interaction', tags=['interaction'])
   
# class Interaction(BaseModel):
#     type: str
#     content: str
#     visitorID: str
#     exhibitID: str
# @interaction_router.post('/add')
# def add_interaction_controller(interaction: Interaction):
#     interaction = {
#         'type': interaction.type,
#         'content': interaction.content,
#         'visitorID': interaction.visitorID,
#         'exhibitID': interaction.exhibitID
#     }
    
#     return create_interaction(interaction)

@interaction_router.get('/count/{visitorID}')
def get_interaction_count_controller(visitorID):
    return get_interaction_count(visitorID)

@interaction_router.get('/duration/{visitorID}')
def get_interaction_duration_controller(visitorID):
    return get_interaction_duration(visitorID)

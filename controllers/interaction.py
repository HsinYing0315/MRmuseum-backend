from fastapi import APIRouter
from pydantic import BaseModel
from services.interaction import create_interaction, create_interaction_with_exhibit, get_interaction_count, get_interaction_duration 

interaction_router = APIRouter(prefix='/interaction', tags=['interaction'])
   
class Interaction(BaseModel):
    content: str
    visitorID: str
@interaction_router.post('/AI/add')
def add_interaction_controller(interaction: Interaction):
    interaction = {
        'type': 'AI assistant',
        'content': interaction.content,
        'visitorID': interaction.visitorID
    }
    
    return create_interaction(interaction)

@interaction_router.post('/NPC/add')
def add_duration_controller(interaction: Interaction):
    interaction = {
        'type': 'NPC',
        'content': interaction.content,
        'visitorID': interaction.visitorID
    }
    
    return create_interaction(interaction)

class ExInteraction(BaseModel):
    content: str
    visitorID: str
    exhibitID: str
@interaction_router.post('/exhibit/add')
def add_duration_controller(interaction: ExInteraction):
    interaction = {
        'type': 'exhibit',
        'content': interaction.content,
        'visitorID': interaction.visitorID,
        'exhibitID': interaction.exhibitID
    }
    
    return create_interaction_with_exhibit(interaction)

@interaction_router.post('/duration/add')
def add_duration_controller(interaction: ExInteraction):
    interaction = {
        'type': 'duration',
        'content': interaction.content,
        'visitorID': interaction.visitorID,
        'exhibitID': interaction.exhibitID
    }
    
    return create_interaction_with_exhibit(interaction)

@interaction_router.get('/count/{visitorID}')
def get_interaction_count_controller(visitorID):
    return get_interaction_count(visitorID)

@interaction_router.get('/duration/{visitorID}')
def get_interaction_duration_controller(visitorID):
    return get_interaction_duration(visitorID)

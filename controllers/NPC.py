from fastapi import APIRouter
from services.NPC import meet_NPC, interact_NPC 

NPC_router = APIRouter(prefix='/npc', tags=['npc'])
   
@NPC_router.get('/{NPC_id}')
def meet_NPC_controller():
    
    return meet_NPC()

@NPC_router.get('/{NPC_id}')
def interact_NPC_controller():
    
    return interact_NPC()

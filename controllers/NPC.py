from fastapi import APIRouter
from services.NPC import meet_NPC, interact_NPC
from pydantic import BaseModel

NPC_router = APIRouter(prefix='/npc', tags=['npc'])
   
@NPC_router.get('/{NPC}')
def meet_NPC_controller(NPC):
    
    return meet_NPC(NPC)

class NPCRequest(BaseModel):
    query: str
    lang: str
    npc_role: str
@NPC_router.post('/interact')
def interact_NPC_controller(NPCrequest: NPCRequest):
    
    return interact_NPC(NPCrequest)

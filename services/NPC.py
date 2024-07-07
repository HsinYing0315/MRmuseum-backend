import requests
from fastapi.responses import JSONResponse
from models.NPC import NPC
from database import session

def meet_NPC(npc):
    npc = session.query(NPC).get(name=npc)
    if (npc == None):
        return JSONResponse(content={'error': 'npc not found'})
    
    return JSONResponse(content=npc)

def interact_NPC(NPC_request):
    request = {
        'query': NPC_request.query,
        'lang': NPC_request.lang,
        'npc_role': NPC_request.npc_role
    }
    
    response = requests.post('http://140.119.19.21:5001/api/generate', json=request)
    
    return JSONResponse(content=response.json().get('response'))
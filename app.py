import requests
import uvicorn
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from __init__ import create_app
from controllers.visitor import visitor_router
from controllers.exhibit.area import area_router
from controllers.exhibit.time import time_router
from controllers.exhibit.exhibit import exhibit_router
from controllers.interaction import interaction_router
from controllers.questionnaire import questionnaire_router

app = create_app()
app.include_router(visitor_router)
app.include_router(area_router)
app.include_router(time_router)
app.include_router(exhibit_router)
app.include_router(interaction_router)
app.include_router(questionnaire_router)

@app.get('/')
def index():
    return JSONResponse(content={'message': 'Hello World'})

class TranslateRequest(BaseModel):
    query: str
    lang: str
@app.post('/translate')
def translate(translateRequest: TranslateRequest):
    request = {
        'text': translateRequest.query,
        'target_language': translateRequest.lang
    }
    response = requests.post('http://140.119.19.21:5001/api/translate', json=request)

    return JSONResponse(content=response.json())

class GenerateRequest(BaseModel):
    query: str
    lang: str
@app.post('/AI')
def ask_AI(generateRequest: GenerateRequest):
    if ('-' in generateRequest.lang):
        generateRequest.lang = generateRequest.lang.replace('-', '_')
        
    query = {
        'query': generateRequest.query,
        'lang': generateRequest.lang,
        'is_rag': True
    }
        
    response = requests.post('http://140.119.19.21:5001/api/generate', json=query)
    
    return JSONResponse(content=response.json().get('response'))

class NPCRequest(BaseModel):
    query: str
    lang: str
    npc_role: str
@app.post('/NPC')
def interact_NPC_controller(NPCrequest: NPCRequest):
    request = {
        'query': NPCrequest.query,
        'lang': NPCrequest.lang,
        'npc_role': NPCrequest.npc_role
    }
    
    response = requests.post('http://140.119.19.21:5001/api/npc/ask', json=request)
    
    return JSONResponse(content=response.json().get('response'))
    
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)

import requests
import uvicorn
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from __init__ import create_app
from services.interaction import create_interaction
from controllers.visitor import visitor_router
from controllers.exhibit.area import area_router
from controllers.exhibit.time import time_router
from controllers.exhibit.exhibit import exhibit_router
from controllers.NPC import NPC_router
from controllers.interaction import interaction_router
from controllers.questionnaire import questionnaire_router

app = create_app()
app.include_router(visitor_router)
app.include_router(area_router)
app.include_router(time_router)
app.include_router(exhibit_router)
app.include_router(NPC_router)
app.include_router(interaction_router)
app.include_router(questionnaire_router)

@app.get('/')
def index():
    return JSONResponse(content='Hello, World!')

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
    visitorID: str
    exhibitID: str
@app.post('/AI')
def ask_AI(generateRequest: GenerateRequest):
    if ('-' in generateRequest.lang):
        generateRequest.lang = generateRequest.lang.replace('-', '_')
        
    query = {
        'query': generateRequest.query,
        'lang': generateRequest.lang
    }
    interaction = {
        'type': 'question',
        'content': generateRequest.query,
        'visitorID': generateRequest.visitorID,
        'exhibitID': generateRequest.exhibitID
    }
        
    response = requests.post('http://140.119.19.21:5001/api/generate', json=query)
    create_interaction(interaction)
    
    return JSONResponse(content=response.json().get('response'))
    
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)

import requests
import uvicorn
from fastapi.responses import JSONResponse
from flask import request

from __init__ import create_app
from services.interaction import create_interaction
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

@app.route('/')
def index(self):
    return JSONResponse(content='Hello, World!')

@app.route('/translate')
def translate():
    data = request.json
    response = requests.post('http://140.119.19.21:5001/api/translate', json=data)

    return JSONResponse(content=response.json())

@app.route('/AI')
def ask_AI():
    data = request.json
    if ('-' in data['lang']):
        data['lang'] = data['lang'].replace('-', '_')
        
    query = {
        'query': data['query'],
        'lang': data['lang']
    }
    interaction = {
        'type': 'question',
        'content': data['query'],
        'visitorID': data['visitorID'],
        'exhibitID': data['exhibitID']
    }
        
    response = requests.post('http://140.119.19.21:5001/api/generate', json=query.json)
    create_interaction(interaction.json)
    
    return JSONResponse(content=response.json().get('response'))
    
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

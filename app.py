import requests
from flask import request, jsonify

from __init__ import create_app
from services.interaction import create_interaction
from controllers.visitor import visitor_blueprint
from controllers.exhibit.area import area_blueprint
from controllers.exhibit.time import time_blueprint
from controllers.exhibit.exhibit import exhibit_blueprint
from controllers.questionnaire import questionnaire_blueprint

app = create_app()
app.register_blueprint(visitor_blueprint, url_prefix='/visitor')
app.register_blueprint(area_blueprint, url_prefix='/area')
app.register_blueprint(time_blueprint, url_prefix='/time')
app.register_blueprint(exhibit_blueprint, url_prefix='/exhibit')
app.register_blueprint(questionnaire_blueprint, url_prefix='/questionnaire')

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

@app.route('/translate', methods=['GET'])
def translate():
    data = request.json
    response = requests.post('http://140.119.19.21:5001/api/translate', json=data)

    return response.json()

@app.route('/AI', methods=['POST'])
def ask_AI():
    data = request.json
    if ('-' in data['lang']):
        data['lang'] = data['lang'].replace('-', '_')
        
    query = jsonify({
        'query': data['query'],
        'lang': data['lang']
    })
    interaction = jsonify({
        'type': 'question',
        'content': data['query'],
        'visitorID': data['visitorID'],
        'exhibitID': data['exhibitID']
    })
        
    response = requests.post('http://140.119.19.21:5001/api/generate', json=query)
    create_interaction(interaction)

    return response.json()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

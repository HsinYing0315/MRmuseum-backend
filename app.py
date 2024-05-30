import requests
from flask import request

from __init__ import create_app
from controllers.visitor import visitor_blueprint
from controllers.exhibit.area import area_blueprint
from controllers.exhibit.time import time_blueprint
from controllers.exhibit.exhibit import exhibit_blueprint
from controllers.interaction import interaction_blueprint
from controllers.questionnaire import questionnaire_blueprint

app = create_app()
app.register_blueprint(visitor_blueprint, url_prefix='/visitor')
app.register_blueprint(area_blueprint, url_prefix='/area')
app.register_blueprint(time_blueprint, url_prefix='/time')
app.register_blueprint(exhibit_blueprint, url_prefix='/exhibit')
app.register_blueprint(interaction_blueprint, url_prefix='/interaction')
app.register_blueprint(questionnaire_blueprint, url_prefix='/questionnaire')

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

@app.route('/translate', methods=['GET'])
def translate():
    data = request.json
    response = requests.post('http://140.119.19.21:5001/api/translate', json=data)

    return response.json()

@app.route('/AI', methods=['GET'])
def ask_AI():
    data = request.json
    if ('-' in data['lang']):
        data['lang'] = data['lang'].replace('-', '_')
        
    response = requests.post('http://140.119.19.21:5001/api/generate', json=data)

    return response.json()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

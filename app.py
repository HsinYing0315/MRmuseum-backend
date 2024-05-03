from . import create_app
from .controllers.exhibit.area import area_blueprint
from .controllers.exhibit.time import time_blueprint
from .controllers.exhibit.exhibit import exhibit_blueprint
from .controllers.interaction import interaction_blueprint
from .controllers.questionnaire import questionnaire_blueprint

app = create_app('development')
app.register_blueprint(area_blueprint, url_prefix='/area')
app.register_blueprint(time_blueprint, url_prefix='/time')
app.register_blueprint(exhibit_blueprint, url_prefix='/exhibit')
app.register_blueprint(interaction_blueprint, url_prefix='/interaction')
app.register_blueprint(questionnaire_blueprint, url_prefix='/questionnaire')

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

@app.route('/AI', methods=['GET'])
def ask_AI():
    
    return ''
    
if __name__ == '__main__':
    app.run()

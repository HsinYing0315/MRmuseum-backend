from . import create_app
from .controllers.exhibit.area import area_blueprint
from .controllers.exhibit.time import time_blueprint
from .controllers.exhibit.exhibit import exhibit_blueprint
from .controllers.interaction import interaction_blueprint
from .controllers.questionnaire import questionnaire_blueprint

app = create_app('development')
app.register_blueprint(area_blueprint)
app.register_blueprint(time_blueprint)
app.register_blueprint(exhibit_blueprint)
app.register_blueprint(interaction_blueprint)
app.register_blueprint(questionnaire_blueprint)
    
if __name__ == '__main__':
    app.run()

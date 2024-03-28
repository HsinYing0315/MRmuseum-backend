from . import create_app
from .controllers.visitor import visitor_blueprint
from .controllers.exhibit.area import area_blueprint
from .controllers.exhibit.time import time_blueprint
from .controllers.exhibit.exhibitGroup import exhibitGroup_blueprint
from .controllers.exhibit.exhibit import exhibit_blueprint
from .controllers.interaction import interaction_blueprint
from .controllers.test.test import test_blueprint
from .controllers.test.answer import answer_blueprint
from .controllers.questionnaire import questionnaire_blueprint

app = create_app('development')
app.register_blueprint(visitor_blueprint, url_prefix='/visitors')
app.register_blueprint(area_blueprint, url_prefix='/areas')
app.register_blueprint(time_blueprint, url_prefix='/times')
app.register_blueprint(exhibitGroup_blueprint, url_prefix='/exhibitGroups')
app.register_blueprint(exhibit_blueprint, url_prefix='/exhibits')
app.register_blueprint(interaction_blueprint, url_prefix='/interactions')
app.register_blueprint(test_blueprint, url_prefix='/tests')
app.register_blueprint(answer_blueprint, url_prefix='/answers')
app.register_blueprint(questionnaire_blueprint, url_prefix='/questionnaires')
    
if __name__ == '__main__':
    app.run()

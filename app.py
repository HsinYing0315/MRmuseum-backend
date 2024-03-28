from . import create_app
from .controllers.visitor import visitor_blueprint
from .controllers.exhibit.area import area_blueprint
from .controllers.exhibit.time import time_blueprint
from .controllers.exhibit.exhibitGroup import exhibitGroup_blueprint
from .controllers.exhibit.exhibit import exhibit_blueprint

app = create_app('development')
app.register_blueprint(visitor_blueprint, url_prefix='/visitors')
app.register_blueprint(area_blueprint, url_prefix='/areas')
app.register_blueprint(time_blueprint, url_prefix='/times')
app.register_blueprint(exhibitGroup_blueprint, url_prefix='/exhibitGroups')
app.register_blueprint(exhibit_blueprint, url_prefix='/exhibits')
    
if __name__ == '__main__':
    app.run()

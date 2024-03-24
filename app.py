from . import create_app
from .controllers.visitor import visitor_blueprint
from .controllers.area import area_blueprint

app = create_app('development')
app.register_blueprint(visitor_blueprint, url_prefix='/visitors')
app.register_blueprint(area_blueprint, url_prefix='/areas')
    
if __name__ == '__main__':
    app.run()

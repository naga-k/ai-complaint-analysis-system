from flask import Flask
from config import config
from .extensions import init_extensions

def create_app(config_name='default'):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    
    init_extensions(app)
    
    from .controllers.complaint_controller import complaint_blueprint
    from .controllers.hello_controller import hello_blueprint  # Add this line
    
    app.register_blueprint(complaint_blueprint, url_prefix='/complaint')
    app.register_blueprint(hello_blueprint) 
    
    return app
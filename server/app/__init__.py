from flask import Flask
from config import config
from .extensions import init_extensions
from .controllers.complaint_controller import complaint_blueprint
from .controllers.audio_controller import audio_blueprint

def create_app(config_name='default'):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    
    init_extensions()
    
    app.register_blueprint(complaint_blueprint, url_prefix='/complaint')
    app.register_blueprint(audio_blueprint, url_prefix='/complaint')
    
    return app
from flask import Flask
# from config import Config
from .extensions import init_extensions
from .controllers.complaint_controller import complaint_blueprint

def create_app():
    app = Flask(__name__)

    init_extensions()
    
    app.register_blueprint(complaint_blueprint, url_prefix='/complaint')
    
    return app
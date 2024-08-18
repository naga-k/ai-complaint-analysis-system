from flask import Flask
from supabase import create_client, Client
from config import config
import openai

supabase: Client = None

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load the configuration
    app.config.from_object(config[config_name])
    
    # Initialize Supabase client
    global supabase
    supabase = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])
    
    openai.api_key = app.config['OPENAI_API_KEY']
    
    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
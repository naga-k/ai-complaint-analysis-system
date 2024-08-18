from supabase import create_client, Client
import openai

supabase: Client = None
openai_client = None

def init_extensions(app):
    global supabase, openai_client
    supabase = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])
    openai.api_key = app.config['OPENAI_API_KEY']
    openai_client = openai
from supabase import create_client, Client
import openai
from config import Config

supabase: Client = None

config = Config()

def init_extensions():
    global supabase
    supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
    openai.api_key = config.OPENAI_API_KEY

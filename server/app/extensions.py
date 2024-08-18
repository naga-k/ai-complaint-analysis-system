from supabase import create_client, Client
import openai
from config import Config

supabase: Client = None
openai_client = None

config = Config()

def init_extensions():
    """
    Initializes the extensions for the application.

    This function sets up the Supabase client and OpenAI client using the configuration settings.
    It uses the global variables `supabase` and `openai_client` to store the initialized clients.

    Parameters:
        None

    Returns:
        None
    """
    global supabase, openai_client
    supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
    openai.api_key = config.OPENAI_API_KEY
    openai_client = openai
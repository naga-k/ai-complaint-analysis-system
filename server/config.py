import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_ANON_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT')
    
    @classmethod
    def get(cls, key, default=None):
        return getattr(cls, key, default)

# Create an instance of the Config class
config = Config()

# For debugging purposes
if __name__ == "__main__":
    print("Current configuration:")
    for key in dir(Config):
        if key.isupper():
            print(f"{key}: {getattr(Config, key)}")
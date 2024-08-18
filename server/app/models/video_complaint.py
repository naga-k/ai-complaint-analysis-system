from supabase import create_client, Client
from config import Config

supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)

class VideoComplaint:
    @staticmethod
    def create(video_url: str, transcript: str, category: str, sentiment: str):
        data = supabase.table('video_complaints').insert({
            'video_url': video_url,
            'transcript': transcript,
            'category': category,
            'sentiment': sentiment
        }).execute()
        return data.data[0] if data.data else None

    @staticmethod
    def get(id: int):
        data = supabase.table('video_complaints').select('*').eq('id', id).execute()
        return data.data[0] if data.data else None
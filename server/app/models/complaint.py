from app.extensions import supabase

class Complaint:
    @staticmethod
    def create(user_id, complaint_data):
        complaint_data['user_id'] = user_id
        result = supabase.table('complaints').insert(complaint_data).execute()
        return result.data

    @staticmethod
    def get_by_user(user_id):
        result = supabase.table('complaints').select('*').eq('user_id', user_id).execute()
        return result.data
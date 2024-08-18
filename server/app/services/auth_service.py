from flask import request
from app.extensions import supabase

def get_authenticated_user_id():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    
    try:
        token = auth_header.split(' ')[1]
        user = supabase.auth.get_user(token)
        return user.id
    except Exception:
        return None
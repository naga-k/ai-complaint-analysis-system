from flask import jsonify, request
from . import main
from .. import supabase
from ..services.text_processing import process_complaint

@main.route('/')
def hello_world():
    return jsonify({"message": "Hello from python!"})

@main.route('/health')
def health_check():
    try:
        # Check Supabase connection
        response = supabase.table('health_check').select('*').limit(1).execute()
        
        return jsonify({
            "status": "healthy",
            "supabase": "connected",
            "message": "Supabase is responsive"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "supabase": "disconnected",
            "message": f"Supabase error: {str(e)}"
        }), 500

@main.route('/users', methods=['GET'])
def get_users():
    try:
        response = supabase.table('users').select('*').execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@main.route('/analyze_complaint', methods=['POST'])
def analyze_complaint():
    data = request.json
    if not data or 'complaint_text' not in data:
        return jsonify({"error": "No complaint text provided"}), 400

    complaint_text = data['complaint_text']
    
    try:
        analysis_result = process_complaint(complaint_text)
        
        # Store the result in Supabase
        supabase.table('complaint_analysis').insert({
            'original_text': complaint_text,
            'analysis_result': analysis_result
        }).execute()
        
        return jsonify(analysis_result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
from flask import jsonify
import json

class ComplaintViews:
    @staticmethod
    def complaint_response(data, message="Success", status=200):
        return jsonify({
            "message": message,
            "data": data
        }), status

    @staticmethod
    def error_response(message, status=400):
        return jsonify({
            "error": message
        }), status
        
    @staticmethod
    def voice_complaint_response(data, message="Success", status=200):
        return jsonify({
            "message": message,
            "data": {
                "id": data.get('id'),
                "user_id": data.get('user_id'),
                "audio_url": data.get('audio_url'),
                "transcript": data.get('transcript'),
                "category": data.get('category'),
                "sub_category": data.get('sub_category'),
                "summary": data.get('summary'),
                "key_issues": json.loads(data.get('key_issues', '[]'))
            }
        }), status
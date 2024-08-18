from flask import jsonify

class AudioViews:
    @staticmethod
    def success_response(data, message="Audio processed successfully", status=200):
        return jsonify({
            "success": True,
            "message": message,
            "data": data
        }), status

    @staticmethod
    def error_response(message, status=400):
        return jsonify({
            "success": False,
            "error": message
        }), status
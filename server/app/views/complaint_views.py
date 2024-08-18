from flask import jsonify

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
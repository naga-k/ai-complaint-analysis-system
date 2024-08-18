from flask import Blueprint, request
import os
from app.models.complaint import Complaint
from app.views.complaint_views import ComplaintViews
from app.services.auth_service import get_authenticated_user_id
from app.services.openai_service import analyze_text_with_gpt, transcribe_audio

complaint_blueprint = Blueprint('complaint', __name__)

@complaint_blueprint.route('/submit', methods=['POST'])
def submit_complaint():
    user_id = get_authenticated_user_id()
    if not user_id:
        return ComplaintViews.error_response("Authentication required", 401)
    
    try:
        complaint_data = request.json
        result = Complaint.create(user_id, complaint_data)
        return ComplaintViews.complaint_response(result, "Complaint submitted successfully")
    except Exception as e:
        return ComplaintViews.error_response(str(e), 500)

@complaint_blueprint.route('/analyze', methods=['POST'])
def analyze_complaint():
    data = request.json
    if not data or 'input' not in data: #was complaint_text
        return ComplaintViews.error_response("No complaint text provided")

    try:
        analysis_result = analyze_text_with_gpt(data['input'])
        return ComplaintViews.complaint_response(analysis_result)
    except Exception as e:
        return ComplaintViews.error_response(str(e), 500)    

@complaint_blueprint.route('/analyze_audio', methods=['POST'])
def analyze_audio_complaint():
    if 'file' not in request.files:
        return ComplaintViews.error_response("No audio file provided")

    file = request.files['file']
    if file.filename == '':
        return ComplaintViews.error_response("No selected file")

    try:
        # Save the file to a temporary location
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)

        # Transcribe the audio file
        transcribed_text = transcribe_audio(file_path)

        # Analyze the transcribed text
        analysis_result = analyze_text_with_gpt(transcribed_text)
        return ComplaintViews.complaint_response(analysis_result)
    except Exception as e:
        return ComplaintViews.error_response(str(e), 500)
    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
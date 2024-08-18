from flask import Blueprint, request
from app.models.complaint import Complaint
from app.views.complaint_views import ComplaintViews
from app.services.auth_service import get_authenticated_user_id
from app.services.openai_service import analyze_text_with_gpt, transcribe_audio
from app.utils.vision_processing import process_images_to_base64, analyze_images

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

@complaint_blueprint.route('/analyze_images', methods=['POST'])
def analyze_complaint_images():
    if 'images' not in request.files:
        return ComplaintViews.error_response("No images provided", 400)
    
    images = request.files.getlist('images')
    try:
        base64_images = process_images_to_base64(images)
        analysis_results = analyze_images(base64_images)
        
        return ComplaintViews.complaint_response(analysis_results, "Image analysis done")
    except Exception as e:
        return ComplaintViews.complaint_response(str(e), 500)

@complaint_blueprint.route('/analyze_audio', methods=['POST'])
def analyze_audio_complaint():
    if 'file' not in request.files:
        return ComplaintViews.error_response("No audio file provided", 400)
    
    audio_file = request.files['file']
    try:
        transcription = transcribe_audio(audio_file)
        analysis_result = analyze_text_with_gpt(transcription)
        return ComplaintViews.complaint_response(analysis_result, "Audio analysis done")
    except Exception as e:
        return ComplaintViews.error_response(str(e), 500)
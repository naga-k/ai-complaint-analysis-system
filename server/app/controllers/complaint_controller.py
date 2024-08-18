from flask import Blueprint, jsonify, request
from app.models.complaint import Complaint
from app.views.complaint_views import ComplaintViews
from app.services.auth_service import get_authenticated_user_id
from app.utils.vision_processing import process_images_to_base64, process_video
from app.services.openai_service import analyze_text_with_gpt, generate_video_description, transcribe_audio, analyze_images

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
    
@complaint_blueprint.route('/analyze_text', methods=['POST'])
def analyze_text_complaint():
    if not request.json or 'text' not in request.json:
        return ComplaintViews.error_response("No text provided", 400)
    
    text = request.json['text']
    try:
        analysis_result = analyze_text_with_gpt(text)
        return ComplaintViews.complaint_response(analysis_result, "Text analysis done")
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


@complaint_blueprint.route('/complaint/analyze_video', methods=['POST'])
def analyze_video():
    video_file = request.files['video']
    base64Frames = process_video(video_file)
    description = generate_video_description(base64Frames)

    return jsonify({
        'category': 'example_category',  # Replace with actual category if available
        'sub_category': 'example_sub_category',  # Replace with actual sub-category if available
        'summary': description,
        'key_issues': 'example_key_issues'  # Replace with actual key issues if available
    }), 200
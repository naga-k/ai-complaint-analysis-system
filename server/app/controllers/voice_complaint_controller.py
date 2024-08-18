from flask import Blueprint, request
from ..models.voice_complaint_model import VoiceComplaint
from app.views.complaint_views import ComplaintViews
from app.services.auth_service import get_authenticated_user_id
from ..services.voice_transcription_service import VoiceTranscriptionService

voice_complaint_blueprint = Blueprint('complaint', __name__)

# /voice/submit-voice
@voice_complaint_blueprint.route('/submit-voice', methods=['POST'])
def submit_voice_complaint():
    user_id = get_authenticated_user_id()
    if not user_id:
        return ComplaintViews.error_response("Authentication required", 401)
    
    try:
        data = request.json
        gcs_uri = data.get('gcs_uri')
        if not gcs_uri:
            return ComplaintViews.error_response("No GCS URI provided", 400)

        transcript = VoiceTranscriptionService.transcribe_audio(gcs_uri)
        analysis = VoiceComplaint.analyze_transcript(transcript)
        
        result = VoiceComplaint.create(user_id, gcs_uri, transcript, analysis)
        if result:
            return ComplaintViews.voice_complaint_response(result, "Voice complaint submitted and analyzed successfully")
        else:
            return ComplaintViews.error_response("Failed to save voice complaint", 500)
    except Exception as e:
        return ComplaintViews.error_response(str(e), 500)
import os
from flask import Blueprint, request
from app.views.complaint_views import ComplaintViews
from app.services.openai_service import analyze_text_with_gpt
from app.services.audio_service import transcribe_audio
from app.views.audio_views import AudioViews
from ..services.supabase_service import save_audio_analysis
from ..extensions import init_extensions

audio_blueprint = Blueprint('audio', __name__)

@audio_blueprint.route('/analyze_audio', methods=['POST'])
def analyze_audio_complaint():
    # init_extensions()
    
    if 'audio' not in request.files:
        return ComplaintViews.error_response("No audio file provided")

    file = request.files['audio']
    user_id = request.form.get('userId')

    if file.filename == '':
        return ComplaintViews.error_response("No selected file")
    
    if not user_id:
        return AudioViews.error_response("No user ID provided")

    try:
        # Save the file to a temporary location
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)

        # Transcribe the audio file
        transcribed_text = transcribe_audio(file_path)

        # Analyze the transcribed text
        analysis_result = analyze_text_with_gpt(transcribed_text)
        
        # Include the transcribed text in the response
        analysis_result['transcribed_text'] = transcribed_text
        print(analysis_result)
        
        # saved_data = save_audio_analysis(user_id, analysis_result)
        
        # print(saved_data)
        
        # if not saved_data:
        #     return AudioViews.error_response("Failed to save analysis to the database", 500)
        
        return AudioViews.success_response(analysis_result)
    except Exception as e:
        return AudioViews.error_response(str(e), 500)
    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
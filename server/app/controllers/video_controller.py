from flask import Blueprint, request, jsonify
from ..services.video_analysis_service import VideoAnalysisService
from ..models.video_complaint import VideoComplaint

video_bp = Blueprint('video', __name__)
video_service = VideoAnalysisService()

@video_bp.route('/process_video', methods=['POST'])
def process_video():
    video_url = request.json.get('video_url')
    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400

    try:
        analysis_result = video_service.analyze_video(video_url)
        
        new_complaint = VideoComplaint.create(
            video_url=video_url,
            transcript=analysis_result['transcript'],
            category=analysis_result['category'],
            sentiment=analysis_result['sentiment']
        )
        
        return jsonify({
            'message': 'Video processed successfully',
            'complaint_id': new_complaint['id'],
            'analysis_result': analysis_result
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
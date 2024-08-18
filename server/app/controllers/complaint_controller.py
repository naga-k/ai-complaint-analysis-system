from flask import Blueprint, request
import os
from app.models.complaint import Complaint
from app.views.complaint_views import ComplaintViews
from app.services.auth_service import get_authenticated_user_id
from app.services.openai_service import analyze_text_with_gpt

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
    
#@complaint_blueprint.route('analyze_image', methods=['POST'])
#def analyze_complaint_image():
    #if 'image' not in request.files:
    #    return ComplaintViews.error_response("No image provided", 400)
    
    #image_file = request.files['image']
    #try:
    #    analysis_result = analyze_image(image_file)
    #    print(analysis_result)
    #    return ComplaintViews.complaint_response(analysis_result, "Image analysis done")
    #except Exception as e:
    #    return ComplaintViews.complaint_response(str(e), 500)  


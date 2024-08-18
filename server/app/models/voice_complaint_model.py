from google.cloud import aiplatform
from app.extensions import supabase
import json
from config import Config

class VoiceComplaint:
    @staticmethod
    def create(user_id, audio_url, transcript, analysis):
        data = {
            'user_id': user_id,
            'audio_url': audio_url,
            'transcript': transcript,
            'category': analysis.get('category'),
            'sub_category': analysis.get('sub_category'),
            'summary': analysis.get('summary'),
            'key_issues': json.dumps(analysis.get('key_issues', []))
        }
        response = supabase.table('voice_complaints').insert(data).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def analyze_transcript(transcript):
        aiplatform.init(project=Config.GOOGLE_CLOUD_PROJECT, location=Config.GOOGLE_CLOUD_LOCATION)
        
        # Specify the model name for text generation
        model_name = "text-bison@001"
        
        # Create a prediction client
        client = aiplatform.gapic.PredictionServiceClient(client_options={"api_endpoint": f"{Config.GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com"})
        
        # Prepare the prompt
        prompt = f'''You are an AI that specializes in analyzing customer complaints. Analyze the following complaint:

{transcript}

Categorize the complaint, provide a sub-category, summarize it, and list key issues. Return the output as a JSON object in this format:
{{
    "category": "Category",
    "sub_category": "Sub-Category",
    "summary": "Summary",
    "key_issues": ["Issue 1", "Issue 2"]
}}'''

        instance = aiplatform.gapic.PredictRequest(
            endpoint=f"projects/{Config.GOOGLE_CLOUD_PROJECT}/locations/{Config.GOOGLE_CLOUD_LOCATION}/publishers/google/models/{model_name}",
            instances=[{"prompt": prompt}],
            parameters={"temperature": 0.2, "maxOutputTokens": 1024}
        )

        response = client.predict(instance)
        
        # Parse the response
        prediction = response.predictions[0]
        return json.loads(prediction['content'])
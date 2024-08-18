from google.cloud import aiplatform
from google.protobuf import json_format
from config import Config

class VideoAnalysisService:
    def __init__(self):
        aiplatform.init(project=Config.GOOGLE_CLOUD_PROJECT, location='us-central1')

    def analyze_video(self, video_url):
        # Initialize Vertex AI Video Intelligence model
        model = aiplatform.Model('projects/{}/locations/{}/models/{}'
                                 .format(Config.GOOGLE_CLOUD_PROJECT, 'us-central1', 'video-intelligence'))

        # Create instance payload for prediction
        instance = {
            'content': video_url,  # GCS URI of the video
            'features': ['SPEECH_TRANSCRIPTION', 'TEXT_DETECTION'],
            'videoContext': {
                'speechTranscriptionConfig': {
                    'languageCode': 'en-US',
                    'enableAutomaticPunctuation': True
                }
            }
        }

        # Make the prediction
        response = model.predict([instance])

        # Process the response
        result = json_format.MessageToDict(response.predictions[0])

        # Extract transcript
        transcript = ""
        for annotation in result.get('annotationResults', []):
            for transcription in annotation.get('speechTranscriptions', []):
                for alternative in transcription.get('alternatives', []):
                    transcript += alternative.get('transcript', '') + " "

        # Categorization and sentiment analysis
        category = self._categorize_complaint(transcript)
        sentiment = self._analyze_sentiment(transcript)

        return {
            "transcript": transcript.strip(),
            "category": category,
            "sentiment": sentiment,
        }

    def _categorize_complaint(self, transcript):
        # Implement more sophisticated categorization logic here
        if "billing" in transcript.lower():
            return "Billing Issue"
        elif "service" in transcript.lower():
            return "Service Quality"
        else:
            return "General Inquiry"

    def _analyze_sentiment(self, transcript):
        # Implement more sophisticated sentiment analysis here
        negative_words = ["bad", "poor", "terrible", "awful", "disappointed"]
        positive_words = ["good", "great", "excellent", "happy", "satisfied"]
        
        negative_count = sum(1 for word in negative_words if word in transcript.lower())
        positive_count = sum(1 for word in positive_words if word in transcript.lower())
        
        if negative_count > positive_count:
            return "Negative"
        elif positive_count > negative_count:
            return "Positive"
        else:
            return "Neutral"
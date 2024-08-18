from google.cloud import videointelligence
from google.cloud import aiplatform
from google.protobuf.json_format import MessageToDict
import io

class VideoAgent:
    def __init__(self):
        self.video_client = videointelligence.VideoIntelligenceServiceClient()
        aiplatform.init(project='your-project-id', location='your-location')

    def process(self, video_content: bytes) -> dict:
        # Perform video analysis using Video Intelligence API
        features = [videointelligence.Feature.LABEL_DETECTION,
                    videointelligence.Feature.SPEECH_TRANSCRIPTION]

        config = videointelligence.SpeechTranscriptionConfig(
            language_code="en-US",
            enable_automatic_punctuation=True,
        )

        video_context = videointelligence.VideoContext(
            speech_transcription_config=config
        )

        operation = self.video_client.annotate_video(
            request={
                "features": features,
                "input_content": video_content,
                "video_context": video_context,
            }
        )

        print("Processing video...")
        result = operation.result(timeout=180)

        # Extract relevant information
        annotations = MessageToDict(result._pb)
        
        # Extract labels
        labels = []
        for annotation in annotations.get('annotationResults', []):
            for label in annotation.get('segmentLabelAnnotations', []):
                labels.append(label['entity']['description'])

        # Extract transcription
        transcription = ""
        for annotation in annotations.get('annotationResults', []):
            for transcription_result in annotation.get('speechTranscriptions', []):
                for alternative in transcription_result.get('alternatives', []):
                    transcription += alternative.get('transcript', '') + " "

        # Use Vertex AI for sentiment analysis and categorization
        sentiment, categories = self.analyze_with_vertex_ai(transcription)

        return {
            "labels": labels,
            "transcription": transcription.strip(),
            "sentiment": sentiment,
            "categories": categories
        }

    def analyze_with_vertex_ai(self, text: str) -> tuple:
        # Use Vertex AI for sentiment analysis
        sentiment_endpoint = aiplatform.Endpoint("your-sentiment-endpoint-id")
        sentiment_response = sentiment_endpoint.predict(instances=[{"text": text}])
        sentiment = sentiment_response.predictions[0]['sentiment']

        # Use Vertex AI for categorization
        category_endpoint = aiplatform.Endpoint("your-category-endpoint-id")
        category_response = category_endpoint.predict(instances=[{"text": text}])
        categories = category_response.predictions[0]['categories']

        return sentiment, categories
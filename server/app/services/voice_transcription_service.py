from google.cloud import speech_v1p1beta1 as speech

class VoiceTranscriptionService:
    @staticmethod
    def transcribe_audio(gcs_uri):
        client = speech.SpeechClient()

        audio = speech.RecognitionAudio(uri=gcs_uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        operation = client.long_running_recognize(config=config, audio=audio)
        response = operation.result(timeout=90)

        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript + " "

        return transcript.strip()
from app.extensions import openai, init_extensions

def transcribe_audio(file_path, language="en"):
    # init_extensions()  # Ensure extensions are initialized
    # Open the audio file
    with open(file_path, "rb") as audio_file:
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language=language,
            response_format="json"
        )

    # Extract and return the text from the response
    transcript = response.text
    return transcript.strip()
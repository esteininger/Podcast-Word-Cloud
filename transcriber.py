import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def transcribe(file_name):

    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        print ('loading in mem')
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
        os.remove(file_name)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio file
    print ('running')
    response = client.recognize(config, audio)

    transcript = []
    for result in response.results:
        print ('output')
        transcript.append(result.alternatives[0].transcript)

    return transcript

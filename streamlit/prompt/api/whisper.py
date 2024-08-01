import os
import openai
from decouple import config

import requests
# print(transcript)

def transcribe_audio(file_path, model_name, token):
    """
    Transcribe audio file using OpenAI API.
    
    Args:
        file_path (str): File path to the audio file.
        model_name (str): Name of the OpenAI model to use for transcription (e.g., "whisper-1").
        token (str): OpenAI API token for authentication.
    
    Returns:
        dict: Transcription response from the API.
    """
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    files = {
        "file": (open(file_path, "rb")),
    }
    data = {
        "model": model_name,
    }

    response = requests.post(url, headers=headers, files=files, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    

transcribe_audio("streamlit/prompt/api/WhatsApp Audio 2023-04-12 at 8.20.33 PM.mp3","whisper-1",config("OPENAI_API_KEY"))
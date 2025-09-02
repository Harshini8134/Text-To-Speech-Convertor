from gtts import gTTS
import os
import uuid

def synthesize_speech(text, language):
    tts = gTTS(text=text, lang=language)
    filename = f"outputs/{uuid.uuid4()}.wav"
    tts.save(filename)
    return filename

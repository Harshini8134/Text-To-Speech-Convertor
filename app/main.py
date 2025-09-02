from flask import Flask, request, send_file
from app.tts_engine import synthesize_speech
from app.text_preprocessor import preprocess_text
from app.language_detector import detect_language

app = Flask(__name__)

@app.route("/synthesize", methods=["POST"])
def synthesize():
    data = request.get_json()
    text = preprocess_text(data["text"])
    language = data.get("language") or detect_language(text)

    output_path = synthesize_speech(text, language)
    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)

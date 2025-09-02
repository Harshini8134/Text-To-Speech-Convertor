from flask import Flask, request, send_file, render_template
from app.tts_engine import synthesize_speech
from app.text_preprocessor import preprocess_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.get_json()
    text = preprocess_text(data["text"])
    language = data["language"]
    output_path = synthesize_speech(text, language)
    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)

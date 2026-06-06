import os
import io
import fitz  # PyMuPDF
import asyncio
import edge_tts
import tempfile
import re
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Map language codes to high-tech neural voices
VOICES = {
    'en': 'en-US-AriaNeural',
    'hi': 'hi-IN-SwaraNeural',
    'es': 'es-ES-ElviraNeural',
    'fr': 'fr-FR-DeniseNeural'
}

def clean_text(text):
    """Advanced text cleaning for better AI pronunciation."""
    # Remove hyphens that break words at the end of lines
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    # Replace newlines with spaces
    text = text.replace('\n', ' ')
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove any weird characters
    text = re.sub(r'[^\w\s.,;:!?\'"-]', '', text)
    return text.strip()

def extract_text(pdf_stream):
    """Extracts text from the uploaded PDF file stream."""
    try:
        doc = fitz.open(stream=pdf_stream.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        return clean_text(text)
    except Exception as e:
        return None

async def generate_audio(text, voice, speed_rate):
    """Generates audio using Edge TTS."""
    communicate = edge_tts.Communicate(text, voice, rate=speed_rate)
    
    # We need a temporary file because edge_tts works best writing to disk directly
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file.close()
    
    await communicate.save(temp_file.name)
    return temp_file.name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if file is uploaded
        if 'pdf_file' not in request.files:
            return render_template('index.html', error="No file uploaded")
        
        file = request.files['pdf_file']
        
        if file.filename == '':
            return render_template('index.html', error="No file selected")

        if file:
            # 1. Extract Text
            text = extract_text(file)
            
            if not text or not text.strip():
                return render_template('index.html', error="Could not extract text. The PDF might be scanned/image-based.")

            # 2. Get Settings from Form
            lang = request.form.get('language', 'en')
            speed = request.form.get('speed', 'normal')
            
            # 3. Configure AI Neural Voice
            voice = VOICES.get(lang, 'en-US-AriaNeural')
            speed_rate = "-20%" if speed == 'slow' else "+0%"

            # 4. Generate Audio with AI
            try:
                # Run the async TTS generation
                mp3_path = asyncio.run(generate_audio(text, voice, speed_rate))
                
                # Send the file and let Flask handle closing/sending it
                # We can't delete it immediately as send_file is lazy, 
                # but tempfile will eventually be cleaned up by the OS, 
                # or we can read it into memory and delete it.
                with open(mp3_path, 'rb') as f:
                    data = f.read()
                os.remove(mp3_path)
                
                mp3_fp = io.BytesIO(data)
                
                return send_file(
                    mp3_fp,
                    mimetype="audio/mpeg",
                    as_attachment=True,
                    download_name=f"{file.filename.replace('.pdf', '')}_AI_Audio.mp3"
                )
            except Exception as e:
                return render_template('index.html', error=f"AI Conversion failed: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, url_for, redirect, session
import os
import uuid
import time
from werkzeug.utils import secure_filename
import logging

# Import custom modules
from modules.audio_processor import AudioProcessor
from modules.feature_extractor import FeatureExtractor
from modules.vocal_separator import VocalSeparator
from modules.reception_analyzer import ReceptionAnalyzer
from modules.report_generator import ReportGenerator

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s %(levelname)s: %(message)s')
app.logger.setLevel(logging.INFO)

# Initialize components dictionary
components = {}

def get_component(component_name):
    """Lazy load components only when needed"""
    if component_name not in components:
        try:
            if component_name == 'vocal_separator':
                components[component_name] = VocalSeparator()
            elif component_name == 'feature_extractor':
                components[component_name] = FeatureExtractor()
            elif component_name == 'audio_processor':
                components[component_name] = AudioProcessor()
            elif component_name == 'reception_analyzer':
                components[component_name] = ReceptionAnalyzer()
            elif component_name == 'report_generator':
                components[component_name] = ReportGenerator()
            app.logger.info(f"Initialized {component_name}")
        except Exception as e:
            app.logger.error(f"Failed to initialize {component_name}: {e}")
            raise
    return components[component_name]

ALLOWED_EXTENSIONS = {'.mp3', '.wav'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('error.html', error="No file part in the request"), 400
    
    file = request.files['file']
    if file.filename == '':
        return render_template('error.html', error="No selected file"), 400
    
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return render_template('error.html', error="Invalid file type (only MP3 and WAV allowed)"), 400
    
    composer = request.form.get('composer', 'Unknown Composer')
    song_name = request.form.get('song_name', 'Untitled Song')
    
    filename = secure_filename(file.filename)
    unique_filename = f"{uuid.uuid4()}_{filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(filepath)
    
    session['filepath'] = filepath
    session['composer'] = composer
    session['song_name'] = song_name
    
    return redirect(url_for('analyze'))

@app.route('/analyze')
def analyze():
    filepath = session.get('filepath')
    composer = session.get('composer', 'Unknown Composer')
    song_name = session.get('song_name', 'Untitled Song')
    
    if not filepath or not os.path.exists(filepath):
        return render_template('error.html', error="File not found or processing error"), 404
    
    try:
        # Lazy load components as needed
        vocal_separator = get_component('vocal_separator')
        feature_extractor = get_component('feature_extractor')
        audio_processor = get_component('audio_processor')
        reception_analyzer = get_component('reception_analyzer')
        report_generator = get_component('report_generator')
        
        vocal_track, instrumental_track = vocal_separator.separate(filepath)
        audio_features = feature_extractor.extract_features(filepath, vocal_track, instrumental_track)
        processed_audio = audio_processor.process(filepath)
        reception_scores = reception_analyzer.analyze(processed_audio, audio_features)
        report = report_generator.generate_report(
            song_name=song_name,
            composer=composer,
            features=audio_features,
            reception_scores=reception_scores
        )
        
        for temp_file in [processed_audio, vocal_track, instrumental_track]:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                    app.logger.info(f"Removed temporary file: {temp_file}")
                except Exception as e:
                    app.logger.warning(f"Failed to remove {temp_file}: {e}")
        
        session['report'] = report
        return redirect(url_for('results'))
    
    except Exception as e:
        app.logger.error(f"Error processing file {filepath}: {str(e)}")
        return render_template('error.html', error=f"Processing failed: {str(e)}"), 500

@app.route('/results')
def results():
    report = session.get('report')
    song_name = session.get('song_name', 'Untitled Song')
    if not report:
        return render_template('error.html', error="No report available"), 404
    return render_template('results.html', report=report, song_name=song_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
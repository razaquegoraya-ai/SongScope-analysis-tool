from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from config import Config
import logging
from modules.audio_processor import AudioProcessor
from modules.feature_extractor import FeatureExtractor
from modules.report_generator import ReportGenerator

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize components
audio_processor = AudioProcessor()
feature_extractor = FeatureExtractor()
report_generator = ReportGenerator()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))

    if not allowed_file(file.filename):
        flash('Invalid file type. Please upload MP3 or WAV files only.')
        return redirect(url_for('index'))

    try:
        # Get form data
        composer = request.form.get('composer', 'Unknown')
        song_name = request.form.get('song_name', 'Untitled')

        # Save the uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process the audio file
        processed_filepath = audio_processor.process(filepath)
        
        # Extract features
        features = feature_extractor.extract_features(processed_filepath)
        
        # Generate report
        report = report_generator.generate_report(song_name, composer, features)
        
        # Clean up temporary files
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(processed_filepath) and processed_filepath != filepath:
            os.remove(processed_filepath)

        return render_template('results.html', 
                             song_name=song_name,
                             composer=composer,
                             report=report)

    except Exception as e:
        flash(f'Error processing file: {str(e)}')
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    # Start the Flask server
    app.run(debug=app.config['DEBUG']) 
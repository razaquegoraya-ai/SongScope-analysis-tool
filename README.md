# SongScope Analysis Tool

A powerful music analysis tool that provides detailed insights into song characteristics, including vocal separation, feature extraction, and reception analysis.

## Features

- Vocal and instrumental track separation
- Audio feature extraction (tempo, energy, mood, etc.)
- Music theory analysis (key, mode, complexity)
- Reception analysis and scoring
- Detailed report generation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/razaquegoraya-ai/SongScope-analysis-tool.git
cd SongScope-analysis-tool
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload an audio file (MP3 or WAV) and provide song details

4. View the analysis results

## Project Structure

```
song-analysis-app/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── modules/            # Analysis modules
│   ├── audio_processor.py
│   ├── feature_extractor.py
│   ├── reception_analyzer.py
│   ├── report_generator.py
│   └── vocal_separator.py
├── templates/          # HTML templates
│   ├── index.html
│   ├── results.html
│   └── error.html
├── static/            # Static files (CSS, JS)
└── uploads/           # Uploaded audio files
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
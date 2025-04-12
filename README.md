# SongScope Analysis Tool

SongScope is a powerful music analysis tool that provides detailed insights into your audio files. It analyzes various musical characteristics including tempo, key, energy, mood, and spectral features to generate comprehensive reports.

## Features

- Audio file analysis (MP3, WAV)
- Tempo detection
- Key detection
- Energy level analysis
- Mood classification
- Spectral feature analysis
- Detailed interpretation and recommendations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SongScope-analysis-tool.git
cd SongScope-analysis-tool
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
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

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload your audio file:
   - Enter the composer name
   - Enter the song name
   - Select an audio file (MP3 or WAV)
   - Click "Analyze"

4. View the analysis report:
   - The report will be displayed on the results page
   - You can download the report or analyze another song

## Project Structure

```
SongScope-analysis-tool/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── modules/
│   ├── audio_processor.py    # Audio processing module
│   ├── feature_extractor.py  # Feature extraction module
│   ├── report_generator.py   # Report generation module
│   └── reception_analyzer.py # Reception analysis module
├── templates/
│   ├── index.html       # Main upload page
│   ├── results.html     # Results display page
│   └── error.html       # Error page
└── uploads/             # Directory for uploaded files
```

## Dependencies

- Flask
- librosa
- essentia
- numpy
- soundfile
- music21

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors who have helped improve this tool
- Special thanks to the open-source community for the amazing libraries used in this project# SongScope-analysis-tool

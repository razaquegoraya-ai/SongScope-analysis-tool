import librosa
import soundfile as sf
import numpy as np

class AudioProcessor:
    def __init__(self):
        pass
    
    def process(self, filepath):
        processed_path = f"{filepath}_processed.wav"
        # Load audio file
        audio, sr = librosa.load(filepath)
        
        # Apply some basic processing (normalize audio)
        audio = librosa.util.normalize(audio)
        
        # Save processed audio
        sf.write(processed_path, audio, sr)
        return processed_path 
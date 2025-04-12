import librosa
import soundfile as sf
import numpy as np
import os

class AudioProcessor:
    def __init__(self):
        self.sample_rate = 22050  # Standard sample rate for analysis
        
    def process(self, audio_path: str) -> str:
        try:
            # Load the audio file
            y, sr = librosa.load(audio_path, sr=self.sample_rate, mono=True)
            
            # Normalize audio
            y = librosa.util.normalize(y)
            
            # Generate output filename
            filename, ext = os.path.splitext(audio_path)
            output_path = f"{filename}_processed{ext}"
            
            # Save processed audio
            sf.write(output_path, y, self.sample_rate)
            
            return output_path
            
        except Exception as e:
            print(f"Error processing audio: {str(e)}")
            raise
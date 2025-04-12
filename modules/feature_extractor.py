import librosa
import numpy as np
from typing import Dict, Any

class FeatureExtractor:
    def __init__(self):
        self.sample_rate = 22050  # Standard sample rate for analysis
        self.hop_length = 512     # For efficient processing
        self.n_fft = 2048        # FFT window size

    def extract_features(self, audio_path: str) -> Dict[str, Any]:
        try:
            # Load audio file
            y, sr = librosa.load(audio_path, sr=self.sample_rate, mono=True)

            # Extract basic features
            tempo, _ = librosa.beat.beat_track(y=y, sr=sr, hop_length=self.hop_length)
            
            # Calculate energy (RMS)
            energy = np.mean(librosa.feature.rms(y=y, hop_length=self.hop_length))
            
            # Calculate spectral features using librosa's built-in functions
            spec_cent = np.mean(librosa.feature.spectral_centroid(
                y=y, sr=sr, n_fft=self.n_fft, hop_length=self.hop_length))
            
            spec_rolloff = np.mean(librosa.feature.spectral_rolloff(
                y=y, sr=sr, n_fft=self.n_fft, hop_length=self.hop_length))
            
            # Key detection using chroma features
            chroma = librosa.feature.chroma_stft(
                y=y, sr=sr, n_fft=self.n_fft, hop_length=self.hop_length)
            key_idx = np.argmax(np.mean(chroma, axis=1))
            keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            key = keys[key_idx]
            
            # Determine mood based on features
            mood = self._determine_mood({
                'energy': float(energy),
                'brightness': float(spec_cent)
            })
            
            return {
                "tempo": float(tempo),
                "energy": float(energy),
                "spectral_centroid": float(spec_cent),
                "spectral_rolloff": float(spec_rolloff),
                "key": key,
                "mood": mood
            }
            
        except Exception as e:
            print(f"Error extracting features: {str(e)}")
            raise

    def _determine_mood(self, features: Dict[str, float]) -> str:
        # Enhanced mood classification based on energy and brightness
        if features['energy'] > 0.6 and features['brightness'] > 3000:
            return 'Energetic/Happy'
        elif features['energy'] > 0.4 and features['brightness'] > 2000:
            return 'Upbeat'
        elif features['energy'] < 0.3 and features['brightness'] < 1500:
            return 'Calm/Melancholic'
        else:
            return 'Neutral'
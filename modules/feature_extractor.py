import librosa
import essentia.standard as es
import numpy as np
from music21 import converter, key, analysis
import os
from sklearn.preprocessing import StandardScaler

class FeatureExtractor:
    def extract_features(self, filepath, vocal_track, instrumental_track):
        try:
            audio, sr = librosa.load(filepath)
            vocal_audio, _ = librosa.load(vocal_track)
            
            # Basic features
            tempo, _ = librosa.beat.beat_track(y=audio, sr=sr)
            energy = librosa.feature.rms(y=audio).mean()
            vocal_clarity = es.PerceptualSharpness()(vocal_audio)  # Proxy for clarity
            complexity = es.SpectralComplexity()(audio)  # Proxy for instrumental complexity
            
            # Mood detection using spectral features
            spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=sr).mean()
            spectral_rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr).mean()
            
            # Normalize features for mood detection
            features = np.array([spectral_centroid, spectral_rolloff, energy])
            scaler = StandardScaler()
            features_scaled = scaler.fit_transform(features.reshape(1, -1))
            
            # Simple mood classification based on spectral features
            mood = "Bright and Uplifting" if features_scaled[0][0] > 0 else "Calm and Reflective"
            
            # Music theory analysis using librosa
            chroma = librosa.feature.chroma_cqt(y=audio, sr=sr)
            key_idx = np.argmax(np.mean(chroma, axis=1))
            key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            detected_key = key_names[key_idx]
            
            # Determine mode (major/minor) based on energy distribution
            is_major = np.mean(chroma[key_idx]) > np.mean(chroma[(key_idx + 3) % 12])
            mode = "major" if is_major else "minor"
            
            theory = {
                'key': f"{detected_key} {mode}",
                'progression': 'Simple'  # Simplified progression detection
            }
            
            # Mixing analysis
            mixing = {'high_freq_noise': librosa.feature.spectral_rolloff(y=audio, sr=sr).mean() > 10000}
            
            return {
                'tempo': tempo,
                'energy': float(energy),
                'vocal_clarity': min(vocal_clarity, 1.0),  # Normalize to 0-1
                'instrumental_complexity': min(complexity / 30.0, 1.0),  # Normalize to 0-1
                'mood': mood,
                'theory': theory,
                'mixing': mixing
            }
        except Exception as e:
            raise Exception(f"Feature extraction failed: {str(e)}") 
import librosa
import numpy as np
import soundfile as sf

class VocalSeparator:
    def __init__(self):
        self.sample_rate = 44100

    def separate(self, audio_path):
        try:
            # Load the audio file
            y, sr = librosa.load(audio_path, sr=self.sample_rate)

            # Compute the spectrogram
            S_full, phase = librosa.magphase(librosa.stft(y))

            # Compute a mel spectrogram from the magnitude spectrogram
            S_mel = librosa.feature.melspectrogram(S=S_full, sr=sr)

            # Find the most prominent frequencies (likely to be vocals)
            S_filter = librosa.decompose.nn_filter(S_mel,
                                                 aggregate=np.median,
                                                 metric='cosine')

            # Compute a mask based on the filtered spectrogram
            mask_mel = librosa.util.softmask(S_mel, S_filter)

            # Convert back to linear frequency scale
            mask = librosa.feature.inverse.mel_to_stft(mask_mel)

            # Apply the mask to separate vocals and instrumental
            S_vocal = S_full * mask
            S_inst = S_full * (1 - mask)

            # Reconstruct the time-domain signals
            y_vocal = librosa.istft(S_vocal * phase)
            y_inst = librosa.istft(S_inst * phase)

            # Save the separated tracks
            vocal_path = audio_path.replace('.mp3', '_vocals.wav').replace('.wav', '_vocals.wav')
            inst_path = audio_path.replace('.mp3', '_inst.wav').replace('.wav', '_inst.wav')

            sf.write(vocal_path, y_vocal, sr)
            sf.write(inst_path, y_inst, sr)

            return vocal_path, inst_path
        except Exception as e:
            print(f"Error separating vocals: {str(e)}")
            raise
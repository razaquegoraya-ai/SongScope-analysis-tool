import demucs.separate
import os

class VocalSeparator:
    def __init__(self):
        self.model = 'htdemucs'
    
    def separate(self, filepath):
        vocals_path = f"{filepath}_vocals.wav"
        instrumental_path = f"{filepath}_instrumental.wav"
        demucs.separate.main(['--two-stems', 'vocals', '-n', self.model, '-o', os.path.dirname(filepath), filepath])
        return f"{os.path.splitext(filepath)[0]}_vocals.wav", f"{os.path.splitext(filepath)[0]}_instrumental.wav" 
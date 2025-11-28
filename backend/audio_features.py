import librosa
import numpy as np

def extract_audio_features(video_audio_path):
    # Load audio waveform
    y, sr = librosa.load(video_audio_path)

    # Extract MFCC features
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    # Root Mean Square Energy (loudness curve)
    energy = librosa.feature.rms(y=y)[0]

    # Convert to simple time‑series (mean of MFCC bands)
    mfcc_mean = mfcc.mean(axis=0)

    return mfcc_mean, energy

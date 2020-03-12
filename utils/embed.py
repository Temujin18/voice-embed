from resemblyzer import preprocess_wav, VoiceEncoder
import numpy as np
import os

encoder = VoiceEncoder()

def audio2embed(audio_file_path):
    return np.array(encoder.embed_utterance(preprocess_wav(audio_file_path)))
from vosk import Model, KaldiRecognizer
import os

MODEL_PATH = os.path.expanduser("~/DRISHTI/vosk-hindi-model")

print("Loading Vosk model...")
model = Model(MODEL_PATH)
KaldiRecognizer(model, 16000)
print("Vosk loaded OK!")

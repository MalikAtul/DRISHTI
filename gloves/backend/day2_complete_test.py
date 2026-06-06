import os, subprocess
from vosk import Model, KaldiRecognizer

MP = os.path.expanduser("~/DRISHTI/vosk-hindi-model")

def speak(t):
    print(f"[TTS] {t}")
    subprocess.run(['espeak-ng', '-v', 'hi', '-s', '130', t])

def test_vosk():
    if not os.path.exists(MP):
        print("[VOSK] ERROR: model not found")
        return False
    try:
        Model(MP)
        print("[VOSK] Loaded OK")
        return True
    except Exception as e:
        print(f"[VOSK] ERROR: {e}")
        return False

print("="*40)
speak("नमस्ते, मेरा नाम ड्रिश्टि है")
speak("आपके सामने एक कुर्सी है")
ok = test_vosk()
print("DAY 2 STATUS:", "COMPLETE" if ok else "INCOMPLETE")
print("="*40)

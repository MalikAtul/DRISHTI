import pyttsx3, subprocess

def speak(text):
    print(f"Speaking: {text}")
    try:
        e = pyttsx3.init()
        e.setProperty('rate', 130)
        e.say(text)
        e.runAndWait()
    except:
        subprocess.run(['espeak-ng','-v','hi','-s','130',text])

speak("नमस्ते")
speak("पांच सौ रुपये का नोट")
speak("धन्यवाद")

# src/tts.py
import pyttsx3

def speak(text):
    engine = pyttsx3.init()  # initialize every time
    print(f"🤖 Jarvis: {text}")  # optional debug
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # cleanup

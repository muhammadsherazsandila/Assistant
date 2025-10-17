import speech_recognition as sr
from src.tts import speak
def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening for command...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"🗣 You said: {command}")
        return command
    except sr.UnknownValueError:
        print("😕 Could not understand audio")
        return None
    except sr.RequestError:
        print("⚠ Speech service error")
        return None

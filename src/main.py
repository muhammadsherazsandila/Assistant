import speech_recognition as sr
from src.tts import speak
from src.commands import execute_command
from src.wake_word import listen_for_wake_word

recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        speak("Yes, I am listening.")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        speak("I didn't catch that.")
        return ""

if __name__ == "__main__":
    speak("Jarvis assistant activated.")
    while True:
        if listen_for_wake_word() >= 0:
            command = listen_for_command()
            execute_command(command)

import webbrowser
from datetime import datetime
from src.tts import speak

def execute_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "time" in command:
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}")
    else:
        speak("Sorry, I don't know that command.")

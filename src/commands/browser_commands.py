import webbrowser
from src.tts import speak

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

def search_google(query):
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

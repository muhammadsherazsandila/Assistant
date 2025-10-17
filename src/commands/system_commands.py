# src/commands/system_commands.py
from datetime import datetime
from src.tts import speak

def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def tell_date():
    current_date = datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

def shutdown():
    speak("Shutting down...")
    # Optional: OS-level shutdown

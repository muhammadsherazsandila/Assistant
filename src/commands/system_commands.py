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

def find_files(filename):
    filename = filename.lower()
    if 'dot' in filename:
        filename = filename.replace('dot', '.')
    if 'underscore' in filename:
        filename = filename.replace('underscore', '_')
    if 'dash' in filename:
        filename = filename.replace('dash', '-')
    if ' ' in filename:
        filename = filename.replace(' ', '')
    speak(f"Searching for files named {filename}")
    import os
    matches = []
    for root, dirs, files in os.walk('/'):
        if filename in files:
            matches.append(os.path.join(root, filename))
    if matches:
        speak(f"Found {len(matches)} files named {filename}.")
        for match in matches:
            speak(match)
    else:
        speak(f"No files named {filename} were found.")
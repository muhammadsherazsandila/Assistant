# src/main.py
from src.wake_word import listen_for_wake_word
from src.stt import listen_for_command
from src.tts import speak
from src.commands import system_commands, browser_commands

def handle_command(cmd):
    cmd = cmd.lower()

    if "time" in cmd:
        system_commands.tell_time()
    elif "date" in cmd:
        system_commands.tell_date()
    elif "open google" in cmd:
        browser_commands.open_google()
    elif cmd.startswith("search"):
        query = cmd.replace("search", "").strip()
        browser_commands.search_google(query)
    elif "shutdown" in cmd:
        system_commands.shutdown()
        exit()
    else:
        print("Sorry, I don't know how to do that yet.")

if __name__ == "__main__":
    while True:  # always-on
        print("👂 Waiting for wake word...")
        listen_for_wake_word()  # blocks until wake word detected
        speak("Jarvis Activated")

        while True:  # active command loop
            command = listen_for_command()
            if command is None:
                continue  # keep listening

            cmd_lower = command.lower()
            if cmd_lower in ["sleep", "exit"]:
                speak("Going to sleep. Call me again when needed.")
                break  # back to wake-word loop
            elif "shutdown" in cmd_lower:
                system_commands.shutdown()
                exit()
            else:
                handle_command(command)

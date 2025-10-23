# src/main.py
from src.wake_word import listen_for_wake_word
from src.stt import listen_for_command
from src.tts import speak
from src.commands import system_commands, browser_commands

from src.commands import matching_commands

def handle_command(cmd):
    cmd = cmd.lower()

    if cmd in matching_commands.time_related_commands:
        system_commands.tell_time()
    elif cmd in matching_commands.date_related_commands:
        system_commands.tell_date()
    elif cmd in matching_commands.open_google_commands:
        browser_commands.open_google()
    elif cmd.startswith("search"):
        query = cmd.replace("search", "").strip()
        browser_commands.search_google(query)
    elif cmd in matching_commands.shutdown_commands:
        system_commands.shutdown()
        exit()
    elif cmd.startswith(matching_commands.find_commands_prefix):
        filename = cmd.replace(matching_commands.find_commands_prefix, "").strip()
        system_commands.find_files(filename)
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
            if "go to sleep" in cmd_lower:
                speak("Going to sleep. Call me again when needed.")
                break  # back to wake-word loop
            elif "shutdown" in cmd_lower:
                system_commands.shutdown()
                exit()
            elif "jarvis" in cmd_lower:
                speak("Yes Anonymous I am here.")
            else:
                handle_command(command)

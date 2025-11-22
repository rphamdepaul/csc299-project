import sys
import os

# Ensure the `src` directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.finalversion.pkms import PKMS
from src.finalversion.improved_task_manager import TaskManager

def main():
    print("Welcome to the Terminal Chat Interface!")
    print("Type 'help' to see available commands.")

    print("Initializing PKMS...")
    pkms = PKMS("notes.json")
    print("PKMS initialized.")

    print("Initializing TaskManager...")
    task_manager = TaskManager("tasks.json")
    print("TaskManager initialized.")

    commands = {
        "help": lambda: print("\n" + "\n".join([
            "Available commands:",
            "  add_note <id> <content> - Add a new note",
            "  list_notes - List all notes",
            "  search_notes <query> - Search notes",
            "  add_task <title> - Add a new task",
            "  list_tasks - List all tasks",
            "  exit - Exit the chat interface",
        ])),
        "add_note": lambda args: (pkms.add(args[0], " ".join(args[1:])), print(f"Note '{args[0]}' added.")),
        "list_notes": lambda _: print("\n".join(["Notes:"] + [f"- {note}" for note in pkms.list()])),
        "search_notes": lambda args: print("\n".join(["Search Results:"] + [f"- {note_id}: {content}" for note_id, content in pkms.search(" ".join(args)).items()])),
        "add_task": lambda args: (task_manager.add_task(" ".join(args)), print(f"Task '{' '.join(args)}' added.")),
        "list_tasks": lambda _: print("\n".join(["Tasks:"] + [f"- {task['id']}: {task['title']}" for task in task_manager.list_tasks()])),
    }

    while True:
        try:
            command_line = input("\n> ").strip()
            if not command_line:
                continue

            command_parts = command_line.split()
            command, args = command_parts[0], command_parts[1:]

            if command == "exit":
                print("Goodbye!")
                break

            if command in commands:
                commands[command](args)
            else:
                print("Unknown command. Type 'help' for a list of commands.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
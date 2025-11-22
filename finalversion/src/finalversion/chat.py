import sys
import os

# Ensure the `src` directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import readline
from src.finalversion.pkms import PKMS
from src.finalversion.improved_task_manager import TaskManager

def main():
    print("Welcome to the Terminal Chat Interface!")
    print("Type 'help' to see available commands.")

    pkms = PKMS("notes.json")
    task_manager = TaskManager("tasks.json")

    while True:
        try:
            command = input("\n> ").strip()

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "help":
                print("Available commands:")
                print("  add_note <id> <content> - Add a new note")
                print("  list_notes - List all notes")
                print("  search_notes <query> - Search notes")
                print("  add_task <title> - Add a new task")
                print("  list_tasks - List all tasks")

            elif command.startswith("add_note"):
                _, note_id, content = command.split(" ", 2)
                pkms.add(note_id, content)
                print(f"Note '{note_id}' added.")

            elif command == "list_notes":
                notes = pkms.list()
                print("Notes:")
                for note in notes:
                    print(f"- {note}")

            elif command.startswith("search_notes"):
                _, query = command.split(" ", 1)
                results = pkms.search(query)
                print("Search Results:")
                for note_id, content in results.items():
                    print(f"- {note_id}: {content}")

            elif command.startswith("add_task"):
                _, title = command.split(" ", 1)
                task = task_manager.add_task(title)
                print(f"Task '{task['id']}' added.")

            elif command == "list_tasks":
                tasks = task_manager.list_tasks()
                print("Tasks:")
                for task in tasks:
                    print(f"- {task['id']}: {task['title']}")

            else:
                print("Unknown command. Type 'help' for a list of commands.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
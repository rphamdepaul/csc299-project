#!/usr/bin/env python3

import sys
import os
import pathlib

# Dynamically add the project root to the Python path
project_root = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

# Ensure the `src` directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.finalversion.pkms import PKMS
from src.finalversion.improved_task_manager import TaskManager

# Shared counter for generating unique IDs
id_counter = 1

def generate_id():
    global id_counter
    current_id = id_counter
    id_counter += 1
    return str(current_id)

# Updated shared counter for user-friendly IDs
user_friendly_id_counter = 1

def generate_user_friendly_id():
    global user_friendly_id_counter
    current_id = user_friendly_id_counter
    user_friendly_id_counter += 1
    return str(current_id)

def main():
    if "TEST_MODE" not in os.environ:
        print("Welcome to the Terminal Chat Interface!")
        print("Type 'help' to see available commands.")

        print("Initializing PKMS...")
    pkms = PKMS("notes.json")
    if "TEST_MODE" not in os.environ:
        print("PKMS initialized.")

        print("Initializing TaskManager...")
    task_manager = TaskManager("tasks.json")
    if "TEST_MODE" not in os.environ:
        print("TaskManager initialized.")

    commands = {
        "help": lambda: print("\n" + "\n".join([
            "Available commands:",
            "  add_note <content> - Add a new note",  # Simplified
            "  list_notes - List all notes",
            "  search_notes <query> - Search notes",
            "  add_task <title> - Add a new task",  # Simplified
            "  list_tasks - List all tasks",
            "  exit - Exit the chat interface",
        ])),
        "add_note": lambda args: (
            pkms.add(*" ".join(args).split("|", 1)),  # Split input into title and content using the '|' delimiter
            print("CONFIRMATION: Note added successfully.")
        ),
        "list_notes": lambda _: print("\n".join(["Notes:"] + [f"-1: {note}" for note in pkms.list_notes()])),
        "search_notes": lambda args: (
            query := " ".join(args).strip('"'),  # Strip extra quotation marks from the query
            print("\n".join(["Search Results:"] + [
                f"- {note['id']}: {note['title']} {note['content']}"
                for note in sorted(pkms.search(query).values(), key=lambda x: x['id'])
            ]))
        ),
        "add_task": lambda args: (
            task_manager.add_task(generate_user_friendly_id(), " ".join(args)),  # Use all arguments as task title
            print("CONFIRMATION: Task added successfully.")
        ),
        "list_tasks": lambda _: print("\n".join(["Tasks:"] + [f"- {task['user_id']}: {task['title']}" for task in task_manager.list_tasks()])),
        "search_tasks": lambda args: (
            query := " ".join(args).strip(),  # Process the query
            tasks := task_manager.search_tasks(query),  # Use TasksAdapter.search_tasks
            print("\n".join(["Search Results:"] + [
                f"- {task_id}: {task['title']} {task['notes']}"
                for task_id, task in tasks.items()
            ]))
        ),
        "delete_all_tasks": lambda _: delete_all_tasks(),
        "delete_all_notes": lambda _: delete_all_notes(),
    }

    def delete_all_tasks():
        confirmation = input("Are you sure you want to delete all tasks? This action cannot be undone. (yes/no): ").strip().lower()
        if confirmation == "yes":
            task_manager.delete_all_tasks()
            print("All tasks have been deleted.")
        else:
            print("Action canceled. No tasks were deleted.")

    def delete_all_notes():
        confirmation = input("Are you sure you want to delete all notes? This action cannot be undone. (yes/no): ").strip().lower()
        if confirmation == "yes":
            pkms.delete_all_notes()
            print("All notes have been deleted.")
        else:
            print("Action canceled. No notes were deleted.")

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
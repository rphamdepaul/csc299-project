import argparse
from src.finalversion.pkms import PKMS
from src.finalversion.tasks_adapter import TasksAdapter
from src.finalversion.chat import main as chat_main

def main():
    parser = argparse.ArgumentParser(description="CLI for managing notes and tasks.")
    subparsers = parser.add_subparsers(dest="command")

    # Notes commands
    notes_parser = subparsers.add_parser("notes", help="Manage notes")
    notes_subparsers = notes_parser.add_subparsers(dest="action")

    add_note_parser = notes_subparsers.add_parser("add", help="Add a new note")
    add_note_parser.add_argument("id", help="Note ID")
    add_note_parser.add_argument("content", help="Note content")

    list_notes_parser = notes_subparsers.add_parser("list", help="List all notes")

    delete_note_parser = notes_subparsers.add_parser("delete", help="Delete a note")
    delete_note_parser.add_argument("id", help="Note ID")

    # Tasks commands
    tasks_parser = subparsers.add_parser("tasks", help="Manage tasks")
    tasks_subparsers = tasks_parser.add_subparsers(dest="action")

    add_task_parser = tasks_subparsers.add_parser("add", help="Add a new task")
    add_task_parser.add_argument("title", help="Task title")

    list_tasks_parser = tasks_subparsers.add_parser("list", help="List all tasks")

    delete_task_parser = tasks_subparsers.add_parser("delete", help="Delete a task")
    delete_task_parser.add_argument("id", help="Task ID")

    # Chat command
    subparsers.add_parser("chat", help="Launch the chat interface")

    # Shorthand commands
    shorthand_parser = subparsers.add_parser("add", help="Shorthand for adding tasks or notes")
    shorthand_parser.add_argument("type", choices=["note", "task"], help="Type of item to add")
    shorthand_parser.add_argument("id_or_title", help="Note ID or Task title")
    shorthand_parser.add_argument("content", nargs="?", help="Note content (only for notes)")

    args = parser.parse_args()

    pkms = PKMS("notes.json")
    tasks_adapter = TasksAdapter("tasks.json")

    if args.command == "notes":
        if args.action == "add":
            pkms.add(args.id, args.content)
            print(f"Note '{args.id}' added.")
        elif args.action == "list":
            notes = pkms.list()
            print("Notes:")
            for note in notes:
                print(f"- {note}")
        elif args.action == "delete":
            pkms.delete(args.id)
            print(f"Note '{args.id}' deleted.")

    elif args.command == "tasks":
        if args.action == "add":
            tasks_adapter.add_task(args.title)
            print(f"Task '{args.title}' added.")
        elif args.action == "list":
            tasks = tasks_adapter.list_tasks()
            print("Tasks:")
            for task in tasks:
                print(f"- {task['title']}")
        elif args.action == "delete":
            tasks_adapter.delete_task(args.id)
            print(f"Task '{args.id}' deleted.")

    elif args.command == "chat":
        chat_main()

    elif args.command == "add":
        if args.type == "note":
            pkms.add(args.id_or_title, args.content)
            print(f"Note '{args.id_or_title}' added.")
        elif args.type == "task":
            tasks_adapter.add_task(args.id_or_title)
            print(f"Task '{args.id_or_title}' added.")

if __name__ == "__main__":
    main()
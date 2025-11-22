import argparse
from src.finalversion.pkms import PKMS
from src.finalversion.tasks_adapter import TasksAdapter

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

    # Tasks commands
    tasks_parser = subparsers.add_parser("tasks", help="Manage tasks")
    tasks_subparsers = tasks_parser.add_subparsers(dest="action")

    add_task_parser = tasks_subparsers.add_parser("add", help="Add a new task")
    add_task_parser.add_argument("title", help="Task title")

    list_tasks_parser = tasks_subparsers.add_parser("list", help="List all tasks")

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

    elif args.command == "tasks":
        if args.action == "add":
            tasks_adapter.add_task(args.title)
            print(f"Task '{args.title}' added.")
        elif args.action == "list":
            tasks = tasks_adapter.list_tasks()
            print("Tasks:")
            for task in tasks:
                print(f"- {task['title']}")

if __name__ == "__main__":
    main()
import argparse
import sys
import re
from datetime import datetime
from finalversion.pkms import PKMS
from finalversion.improved_task_manager import TaskManager
from finalversion.ai_agent import summarize_text

def chat_interface():
    pkms = PKMS("notes.json")
    task_manager = TaskManager()
    current_list_type = None
    current_list = None
    print("Welcome to the PKMS/TaskManager chat interface!")
    print("Type 'help' for available commands.")
    while True:
        user_input = input("chat> ").strip()
        if user_input == "exit":
            print("Exiting chat interface.")
            break
        elif user_input.startswith("add note "):
            # Format: add note <id> <content> OR add note "Title": Content
            match = re.match(r'add note "([^"]+)":\s*(.*)', user_input)
            if match:
                title = match.group(1)
                content = match.group(2)
                note = pkms.add(title, content)
                print(f"Note '{title}' added.")
            else:
                parts = user_input.split(maxsplit=3)
                if len(parts) >= 4:
                    _, _, note_id, content = parts
                    note = pkms.add(note_id, content)
                    print(f"Note '{note_id}' added.")
                else:
                    print("Usage: add note <id> <content> OR add note \"Title\": Content")
        elif user_input == "list notes":
            notes = pkms.list()
            print("Notes:")
            for note in notes:
                priority = note.get('priority', 'medium')
                print(f"- {note['id']}: {note['title']} (priority: {priority})")
            current_list_type = 'notes'
            current_list = notes
        elif user_input.startswith("search notes "):
            _, _, query = user_input.partition("search notes ")
            results = pkms.search(query.strip())
            print("Notes:")
            for note in results:
                priority = note.get('priority', 'medium')
                print(f"- {note['id']}: {note['title']} (priority: {priority})")
            current_list_type = 'notes'
            current_list = results
        elif user_input.startswith("delete note "):
            _, _, note_id = user_input.partition("delete note ")
            try:
                pkms.delete(note_id.strip())
                print(f"Note '{note_id.strip()}' deleted.")
            except Exception as e:
                print(f"Error: {e}")
        elif user_input == "delete all notes":
            try:
                pkms.delete_all()
                print("All notes deleted.")
            except Exception as e:
                print(f"Error: {e}")
        elif user_input.startswith("add task "):
            _, _, rest = user_input.partition("add task ")
            match = re.match(r'(.+?)\s+(\d{4}-\d{2}-\d{2} \d{1,2}:\d{2}(?: [APMapm]{2})?)\s+(low|medium|high)\s*$', rest)
            if match:
                title = match.group(1).strip()
                due_raw = match.group(2).strip()
                priority = match.group(3)
                try:
                    if re.search(r'[APMapm]{2}', due_raw):
                        due_dt = datetime.strptime(due_raw, "%Y-%m-%d %I:%M %p")
                    else:
                        due_dt = datetime.strptime(due_raw, "%Y-%m-%d %H:%M")
                    due_24 = due_dt.strftime("%Y-%m-%d %H:%M")
                except Exception:
                    due_24 = due_raw
                task_manager.add_task(user_id="default", title=title, priority=priority, due=due_raw, due_24=due_24)
                print(f"Task '{title}' added with due date '{due_raw}' and priority '{priority}'.")
            else:
                task_manager.add_task(user_id="default", title=rest.strip())
                print(f"Task '{rest.strip()}' added.")
        elif user_input == "list tasks":
            tasks = task_manager.list_tasks()
            print("Tasks:")
            for idx, task in enumerate(tasks, 1):
                priority = task.get('priority', 'medium')
                due = task.get('due', None)
                due_str = f", due: {due}" if due else ""
                print(f"{idx}. {task['title']} (priority: {priority}{due_str})")
            current_list_type = 'tasks'
            current_list = tasks
        elif user_input.startswith("delete task "):
            _, _, idx_str = user_input.partition("delete task ")
            try:
                idx = int(idx_str.strip())
                success = task_manager.delete_task_by_index(idx)
                if success:
                    print(f"Task {idx} deleted.")
                else:
                    print(f"Task {idx} not found.")
            except Exception as e:
                print(f"Error: {e}")
        elif user_input == "delete all tasks":
            try:
                count = task_manager.delete_all_tasks()
                print(f"All tasks deleted ({count} tasks).")
            except Exception as e:
                print(f"Error: {e}")
        elif user_input.startswith("ai agent summarize "):
            _, _, idx_str = user_input.partition("ai agent summarize ")
            idx_str = idx_str.strip()
            if not idx_str.isdigit():
                print("Please provide a valid index number.")
                continue
            idx = int(idx_str)
            if current_list_type == 'notes':
                notes = current_list
                if 1 <= idx <= len(notes):
                    note = notes[idx-1]
                    text = note.get("content", note.get("title", ""))
                    print(f"Summarizing Note {idx}: {text}")
                    summary = summarize_text(text)
                    print(f"AI Summary: {summary}")
                else:
                    print("Index out of range for notes.")
            elif current_list_type == 'tasks':
                tasks = current_list
                if 1 <= idx <= len(tasks):
                    task = tasks[idx-1]
                    text = task.get("title", "")
                    print(f"Summarizing Task {idx}: {text}")
                    summary = summarize_text(text)
                    print(f"AI Summary: {summary}")
                else:
                    print("Index out of range for tasks.")
            else:
                print("Please run 'list notes' or 'list tasks' before summarizing.")
        elif user_input == "help":
            print("Available commands:")
            print("add note <id> <content>")
            print("add note \"Title\": Content")
            print("list notes")
            print("search notes <query>")
            print("delete note <id>")
            print("delete all notes")
            print("add task <description> <due_date> <priority>")
            print("add task <description>")
            print("list tasks")
            print("delete task <index>")
            print("delete all tasks")
            print("ai agent summarize <index>")
            print("help")
            print("exit")
        else:
            print("Unknown command. Type 'help' for available commands.")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "chat":
        chat_interface()
    else:
        parser = argparse.ArgumentParser(description="PKMS and TaskManager CLI")
        subparsers = parser.add_subparsers(dest="command")

        # Notes commands
        notes_parser = subparsers.add_parser("notes")
        notes_subparsers = notes_parser.add_subparsers(dest="action")
        notes_add = notes_subparsers.add_parser("add")
        notes_add.add_argument("id")
        notes_add.add_argument("content")
        notes_list = notes_subparsers.add_parser("list")
        notes_delete = notes_subparsers.add_parser("delete")
        notes_delete.add_argument("id")

        # Tasks commands
        tasks_parser = subparsers.add_parser("tasks")
        tasks_subparsers = tasks_parser.add_subparsers(dest="action")
        tasks_add = tasks_subparsers.add_parser("add")
        tasks_add.add_argument("title")
        tasks_list = tasks_subparsers.add_parser("list")
        tasks_delete = tasks_subparsers.add_parser("delete")
        tasks_delete.add_argument("id")

        args = parser.parse_args()
        pkms = PKMS("notes.json")
        task_manager = TaskManager()

        if args.command == "notes":
            if args.action == "add":
                pkms.add(args.id, args.content)
                print(f"Note '{args.id}' added.")
            elif args.action == "list":
                notes = pkms.list()
                print("Notes:")
                for note in notes:
                    priority = note.get('priority', 'medium')
                    print(f"- {note['id']}: {note['title']} (priority: {priority})")
            elif args.action == "delete":
                pkms.delete(args.id)
                print(f"Note '{args.id}' deleted.")
        elif args.command == "tasks":
            if args.action == "add":
                task_manager.add_task(user_id="default", title=args.title)
                print(f"Task '{args.title}' added.")
            elif args.action == "list":
                tasks = task_manager.list_tasks()
                print("Tasks:")
                for task in tasks:
                    print(f"- {task['title']}")
            elif args.action == "delete":
                success = task_manager.delete_task_by_index(int(args.id))
                if success:
                    print(f"Task {args.id} deleted.")
                else:
                    print(f"Task {args.id} not found.")

if __name__ == "__main__":
    main()
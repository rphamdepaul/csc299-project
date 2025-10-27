import argparse
from task_manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument("command", choices=["add", "list", "search"], help="Command to execute")
    parser.add_argument("--title", help="Title of the task (required for 'add')")
    parser.add_argument("--description", help="Description of the task (required for 'add')")
    parser.add_argument("--query", help="Search query (required for 'search')")

    args = parser.parse_args()
    task_manager = TaskManager("tasks.json")

    if args.command == "add":
        if not args.title or not args.description:
            print("Error: --title and --description are required for 'add' command.")
            return
        task = task_manager.add_task(args.title, args.description)
        print(f"Task added: {task}")

    elif args.command == "list":
        tasks = task_manager.list_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")
        else:
            print("No tasks found.")

    elif args.command == "search":
        if not args.query:
            print("Error: --query is required for 'search' command.")
            return
        results = task_manager.search_tasks(args.query)
        if results:
            for task in results:
                print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")
        else:
            print("No matching tasks found.")

if __name__ == "__main__":
    main()
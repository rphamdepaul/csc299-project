"""CLI for the task manager. Keeps CLI logic separate from storage implementation.

Usage examples:
  python -m task_manager.cli add "Title" --description "desc" --tags a b
  python -m task_manager.cli list
  python -m task_manager.cli search "query"
  python -m task_manager.cli edit <id> --title "new" --completed
  python -m task_manager.cli delete <id>
"""
from __future__ import annotations

import argparse
import sys
from typing import List
from .store import TaskStore, TaskNotFound


def parse_args(argv: List[str] = None):
    parser = argparse.ArgumentParser(prog="task-manager")
    parser.add_argument("--file", "-f", default="tasks.json", help="Path to tasks json file")
    sub = parser.add_subparsers(dest="cmd")

    # add
    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title")
    p_add.add_argument("--description", "-d", default="")
    p_add.add_argument("--due", help="Due date/time in ISO format", default=None)
    p_add.add_argument("--tags", nargs="*", help="Tags for the task", default=[])

    # list
    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument("--pending", action="store_true", help="Show only pending tasks")

    # search
    p_search = sub.add_parser("search", help="Search tasks by text/tags")
    p_search.add_argument("query")

    # get
    p_get = sub.add_parser("get", help="Get a task by id")
    p_get.add_argument("id")

    # edit
    p_edit = sub.add_parser("edit", help="Edit a task")
    p_edit.add_argument("id")
    p_edit.add_argument("--title")
    p_edit.add_argument("--description")
    p_edit.add_argument("--due")
    p_edit.add_argument("--tags", nargs="*")
    p_edit.add_argument("--completed", choices=["true", "false"], help="Set completion state")

    # delete
    p_delete = sub.add_parser("delete", help="Delete a task")
    p_delete.add_argument("id")

    return parser.parse_args(argv)


def print_task(t: dict):
    tags = ", ".join(t.get("tags") or [])
    print(f"ID: {t.get('id')}")
    print(f"Title: {t.get('title')}")
    if t.get("description"):
        print(f"Description: {t.get('description')}")
    print(f"Created: {t.get('created_at')}")
    if t.get("due"):
        print(f"Due: {t.get('due')}")
    print(f"Completed: {t.get('completed')}")
    if tags:
        print(f"Tags: {tags}")
    print("---")


def main(argv: List[str] = None):
    args = parse_args(argv)
    if not args.cmd:
        print("No command provided. Use --help for usage.")
        return 2

    store = TaskStore(args.file)

    try:
        if args.cmd == "add":
            t = store.add_task(args.title, description=args.description, due=args.due, tags=args.tags)
            print("Task added:")
            print_task(t)
            return 0

        if args.cmd == "list":
            tasks = store.list_tasks(include_completed=not args.pending)
            if not tasks:
                print("No tasks")
                return 0
            for t in tasks:
                print_task(t)
            return 0

        if args.cmd == "search":
            results = store.search_tasks(args.query)
            if not results:
                print("No matching tasks")
                return 0
            for t in results:
                print_task(t)
            return 0

        if args.cmd == "get":
            t = store.get_task(args.id)
            print_task(t)
            return 0

        if args.cmd == "edit":
            fields = {}
            for k in ("title", "description", "due", "tags"):
                val = getattr(args, k, None)
                if val is not None:
                    fields[k] = val
            if args.completed is not None:
                fields["completed"] = True if args.completed == "true" else False
            t = store.edit_task(args.id, **fields)
            print("Task updated:")
            print_task(t)
            return 0

        if args.cmd == "delete":
            store.delete_task(args.id)
            print("Task deleted")
            return 0

    except TaskNotFound as e:
        print(f"Error: task not found: {e}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

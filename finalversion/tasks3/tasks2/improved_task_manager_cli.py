"""Improved CLI for the new TaskManager (uses tasks_new.json)
"""
import argparse
import json
from improved_task_manager import TaskManager


def main():
    parser = argparse.ArgumentParser(prog="taskmgr-new")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add")
    add.add_argument("--title", "-t", required=True)
    add.add_argument("--notes", "-n")
    add.add_argument("--tags", "-g", help="comma separated tags")
    add.add_argument("--due", help="ISO due date")

    listp = sub.add_parser("list")
    listp.add_argument("--format", choices=["table", "json"], default="table")
    listp.add_argument("--all", action="store_true", help="include deleted tasks")

    view = sub.add_parser("view")
    view.add_argument("id")

    edit = sub.add_parser("edit")
    edit.add_argument("id")
    edit.add_argument("--title")
    edit.add_argument("--notes")
    edit.add_argument("--tags")
    edit.add_argument("--due")
    edit.add_argument("--status", choices=["todo", "in-progress", "done"])

    delete = sub.add_parser("delete")
    delete.add_argument("id")
    delete.add_argument("--yes", "-y", action="store_true")
    delete.add_argument("--hard", action="store_true")

    undo = sub.add_parser("undo")
    undo.add_argument("id")
    undo.add_argument("--steps", type=int, default=1)

    args = parser.parse_args()
    tm = TaskManager()

    if args.cmd == "add":
        tags = [t.strip() for t in args.tags.split(",")] if args.tags else None
        task = tm.add_task(args.title, notes=args.notes or "", tags=tags, due=args.due)
        print(task["id"])

    elif args.cmd == "list":
        tasks = tm.list_tasks(include_deleted=args.all)
        if args.format == "json":
            print(json.dumps(tasks, indent=2, ensure_ascii=False))
        else:
            for t in tasks:
                status = t.get("status", "todo")
                print(f"{t['id'][:8]}  {status:>11}  {t.get('title')}")

    elif args.cmd == "view":
        t = tm.get_task(args.id, include_deleted=True)
        if not t:
            print("Not found")
        else:
            print(json.dumps(t, indent=2, ensure_ascii=False))

    elif args.cmd == "edit":
        kwargs = {}
        if args.title is not None:
            kwargs["title"] = args.title
        if args.notes is not None:
            kwargs["notes"] = args.notes
        if args.tags is not None:
            kwargs["tags"] = [x.strip() for x in args.tags.split(",") if x.strip()]
        if args.due is not None:
            kwargs["due"] = args.due
        if args.status is not None:
            kwargs["status"] = args.status
        if not kwargs:
            print("No changes provided")
        else:
            ok = tm.update_task(args.id, **kwargs)
            print("Updated" if ok else "Task not found")

    elif args.cmd == "delete":
        if not args.yes:
            confirm = input(f"Delete {args.id}? type 'yes' to confirm: ")
            if confirm.strip().lower() != "yes":
                print("Aborted")
                return
        ok = tm.delete_task(args.id, hard=args.hard)
        print("Deleted" if ok else "Task not found")

    elif args.cmd == "undo":
        ok = tm.undo(args.id, steps=args.steps)
        print("Undone" if ok else "Failed to undo")


if __name__ == "__main__":
    main()

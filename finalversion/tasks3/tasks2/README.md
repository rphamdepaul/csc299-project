
# Improved PKMS Task Manager (new)

Files created:

- `improved_task_manager.py` - new TaskManager implementation using `tasks_new.json`.
- `improved_task_manager_cli.py` - CLI for the new task manager.
- `tasks_new.json` - JSON datastore used by the new manager (created in this directory).

Quick notes

- The CLI examples below assume you run the commands from this directory. The datastore `tasks_new.json` will be created here if it doesn't exist.
- Use `python3` to run the scripts on macOS / Linux (replace with `python` if your system points to Python 3).
- `--tags` accepts a comma-separated list (e.g. `--tags groceries,errands`).

Usage examples

Add a task (tags are optional and comma-separated):

```sh
python3 improved_task_manager_cli.py add --title "Buy milk" --notes "2L" --tags groceries,shopping
```

List tasks (table format, default):

```sh
python3 improved_task_manager_cli.py list
```

List tasks as JSON (includes only non-deleted tasks by default):

```sh
python3 improved_task_manager_cli.py list --format json
```

Include deleted (soft-deleted) tasks in the listing:

```sh
python3 improved_task_manager_cli.py list --all
```

View a task (use the full id returned when adding):

```sh
python3 improved_task_manager_cli.py view <task-id>
```

Edit a task (provide one or more fields to change):

```sh
python3 improved_task_manager_cli.py edit <task-id> --title "New title" --notes "updated notes"
```

Delete a task (soft delete; use `--hard` to permanently remove):

```sh
python3 improved_task_manager_cli.py delete <task-id>
# or permanent:
python3 improved_task_manager_cli.py delete <task-id> --hard --yes
```

Undo the last change(s) to a task (default 1 step):

```sh
python3 improved_task_manager_cli.py undo <task-id>
```

Help

Show full help for available commands and flags:

```sh
python3 improved_task_manager_cli.py -h
python3 improved_task_manager_cli.py add -h
```

If you want, I can also add a short section showing how to run the smoke test and how to run the CLI from any directory by setting the `TASKS_FILE` environment variable (or adding a flag) — tell me which you prefer.

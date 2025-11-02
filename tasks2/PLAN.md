# Project Plan: PKMS Task Manager

## Overview
PKMS is a CLI task manager that stores tasks in `tasks.json`.

## Goals
- Keep `tasks.json` as the primary datastore.
- Add edit/delete + one extra feature (recurrence) while preserving existing APIs.
- Safe migration/backups and atomic writes.
- Record machine-readable agent instructions.

## Features (summary)
- Existing: add, list, search (preserve).
- New: edit/update tasks, delete (soft by default + hard option).
- New: per-task history and undo.
- New: recurring tasks (instance-based on completion).
- New: atomic saves and first-run backup (`tasks.json.bak`).
- CLI: argparse subcommands (add/list/view/edit/delete/undo/complete).

## Data Structure (extended task)
- id: string (UUID)
- title: string
- description / notes: string
- created_at: ISO8601
- updated_at: ISO8601 (new)
- status: "todo" | "in-progress" | "done" (new)
- tags: [string] (optional)
- due: ISO8601 | null (optional)
- deleted: boolean (soft-delete marker, new)
- history: [{ts, action, snapshot}] (new)
- recurrence: object|null (new)

## CLI (argparse-style)
- add: add a task
- list: list tasks (filters: --tag, --status, --format)
- view <id>: show full task JSON
- edit <id>: update provided fields or open $EDITOR (planned)
- delete <id>: soft-delete by default; `--hard` for permanent remove; `--yes` to skip confirm
- undo <id>: revert recent change(s)
- complete <id>: mark done; if recurring, create next instance

## Implementation plan (steps)
1. Migration & backup: create `tasks.json.bak` and add default fields to legacy tasks.
2. TaskManager: implement update_task, delete_task(hard=False), get_task(include_deleted=False), history hooks.
3. Atomic saves & simple macOS locking (fcntl guarded).
4. CLI: add argparse subcommands and keep backward compatibility.
5. Recurrence: instance-based next-instance creation on completion.
6. Tests: pytest for add/update/delete/undo/migration using tmp_path.

## Agent metadata (machine-readable)
```json
{
  "project_root": ".",
  "entry_points": ["task_manager.py","task_manager_cli.py"],
  "primary_datastore": "tasks.json",
  "actions": [
    {"file": "task_manager.py", "tasks": ["update_task","delete_task","history_hooks","atomic_save","migration"]},
    {"file": "task_manager_cli.py", "tasks": ["argparse_subcommands: edit,delete,undo,complete,view"]},
    {"file": "tests/test_task_manager.py", "tasks": ["unit_tests:add/update/delete/undo/migration"]},
    {"file": "tasks.json.bak", "tasks": ["create_on_migration"]}
  ],
  "constraints": {
    "must_preserve": ["primary_datastore_format","public_API:add_task,get_task,list_tasks"],
    "write_strategy": "atomic_temp_and_rename"
  }
}
```
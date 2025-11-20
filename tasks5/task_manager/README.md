Task Manager

This small task manager provides a JSON-backed TaskStore and a CLI.

Usage (module):

from task_manager.store import TaskStore
store = TaskStore('data/tasks.json')
store.add_task('Buy milk')

Usage (CLI):

python -m task_manager.cli add "Title" --description "desc"
python -m task_manager.cli list

Storage is separated from CLI: `store.py` contains the storage layer; `cli.py` handles parsing and calls into the store.

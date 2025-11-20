"""Task Manager - JSON-backed task storage with CLI.

Usage:
    from task_manager.store import TaskStore
    store = TaskStore('tasks.json')
    store.add_task('Title')

CLI:
    python -m task_manager.cli add "Task" --tags work
    python -m task_manager.cli list
"""
__version__ = "0.1.0"

import json
from src.finalversion.improved_task_manager import TaskManager

class TasksAdapter:
    def __init__(self, tasks_file):
        self.task_manager = TaskManager(tasks_file)

    def add_task(self, title, due_date=None):
        """Add a task with optional due date."""
        self.task_manager.add_task(title, notes="", tags=None, due=due_date)

    def list_tasks(self):
        """List all tasks."""
        return self.task_manager.list_tasks()

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        self.task_manager.delete_task(task_id)

    def update_task(self, task_id, title=None, priority=None, due_date=None):
        """Update task details."""
        self.task_manager.update_task(task_id, title=title, priority=priority, due=due_date)

    def search_tasks(self, query):
        """Search tasks by a query."""
        return self.task_manager.search_tasks(query)

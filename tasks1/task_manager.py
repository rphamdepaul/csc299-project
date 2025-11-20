import json
import uuid

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description):
        task = {
            "id": str(uuid.uuid4()),
            "title": title,
            "description": description
        }
        self.tasks.append(task)
        self._save_tasks()
        return task

    def list_tasks(self):
        return self.tasks

    def search_tasks(self, query):
        return [task for task in self.tasks if query.lower() in task['title'].lower() or query.lower() in task['description'].lower()]
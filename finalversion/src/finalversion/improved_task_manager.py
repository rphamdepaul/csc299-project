"""Improved TaskManager
Separate JSON datastore (tasks_new.json) to avoid touching original files.
Supports add, list, get, update, delete (soft/hard), history, and atomic saves.
Minimal dependencies, easy to read/modify.
"""

import json
import uuid
import os
import tempfile
from datetime import datetime, timezone  # Add timezone import
from typing import List, Dict, Optional
import threading
import time

DEFAULT_FILE = os.path.join(os.path.dirname(__file__), "tasks_new.json")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat() + "Z"


class TaskManager:
    def __init__(self, file_path: str = DEFAULT_FILE):
        self.file_path = file_path
        self.tasks: List[Dict] = []
        self.notifications = []  # Store notifications for testing
        self._load()

    def _load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
                for task in self.tasks:
                    if "user_id" not in task:
                        task["user_id"] = "unknown"
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            self.tasks = []

    def _atomic_write(self, data):
        dirpath = os.path.dirname(self.file_path) or "."
        fd, tmp = tempfile.mkstemp(dir=dirpath)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            os.replace(tmp, self.file_path)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)

    def _save(self):
        self._atomic_write(self.tasks)

    def add_task(self, user_id: str, title: str, notes: str = "", tags: Optional[List[str]] = None, due: Optional[str] = None, due_24: Optional[str] = None, priority: str = "medium") -> Dict:
        if priority not in ["low", "medium", "high"]:
            priority = "medium"
        user_id = str(user_id)
        task = {
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            "title": title,
            "notes": notes or "",
            "tags": tags or [],
            "due": due,
            "due_24": due_24,
            "priority": priority,
            "status": "todo",
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
        }
        self.tasks.append(task)
        self._save()
        return task

    def list_tasks(self, include_deleted: bool = False, priority_filter: Optional[str] = None) -> List[Dict]:
        tasks = self.tasks if include_deleted else [t for t in self.tasks if not t.get("deleted", False)]
        if priority_filter:
            if priority_filter not in ["low", "medium", "high"]:
                raise ValueError("Priority filter must be one of: low, medium, high.")
            tasks = [t for t in tasks if t.get("priority") == priority_filter]
        return tasks

    def delete_task_by_index(self, index: int) -> bool:
        tasks = self.list_tasks()
        if 1 <= index <= len(tasks):
            count = 0
            for i, t in enumerate(self.tasks):
                if not t.get("deleted", False):
                    count += 1
                    if count == index:
                        t["deleted"] = True
                        t["updated_at"] = _now_iso()
                        self._save()
                        return True
            return False
        return False

    def _record_history(self, task: Dict, action: str):
        snapshot = {k: v for k, v in task.items() if k != "history"}
        entry = {"ts": _now_iso(), "action": action, "snapshot": snapshot}
        task.setdefault("history", []).append(entry)

    def delete_all_tasks(self) -> int:
        count = 0
        for t in self.tasks:
            if not t.get("deleted", False):
                t["deleted"] = True
                t["updated_at"] = _now_iso()
                count += 1
        self._save()
        return count


if __name__ == "__main__":
    print("This module provides TaskManager class. Use the CLI.")

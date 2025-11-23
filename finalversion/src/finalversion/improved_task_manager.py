"""Improved TaskManager

- Separate JSON datastore (tasks_new.json) to avoid touching original files.
- Supports add, list, get, update, delete (soft/hard), history, and atomic saves.
- Minimal dependencies, easy to read/modify.
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
        self.notification_thread = threading.Thread(target=self._notification_worker, daemon=True)
        self.notification_thread.start()

    def _load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            # Corrupt file: start with empty list but do not overwrite
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

    def add_task(self, user_id: str, title: str, notes: str = "", tags: Optional[List[str]] = None, due: Optional[str] = None, priority: str = "medium") -> Dict:
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be one of: low, medium, high.")

        # Find the lowest unused ID greater than 0
        existing_ids = {task["user_id"] for task in self.tasks if "user_id" in task}
        new_id = 1
        while new_id in existing_ids:
            new_id += 1

        task = {
            "id": str(uuid.uuid4()),  # Internal unique ID
            "user_id": new_id,  # User-friendly ID
            "title": title,
            "notes": notes or "",
            "tags": tags or [],
            "due": due,
            "priority": priority,
            "status": "todo",
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
            "deleted": False,
            "history": [],
            "recurrence": None,
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

    def get_task(self, task_id: str, include_deleted: bool = False) -> Optional[Dict]:
        for t in self.tasks:
            if t.get("id") == task_id:
                if not include_deleted and t.get("deleted", False):
                    return None
                return t
        return None

    def _record_history(self, task: Dict, action: str):
        snapshot = {k: v for k, v in task.items() if k != "history"}
        entry = {"ts": _now_iso(), "action": action, "snapshot": snapshot}
        task.setdefault("history", []).append(entry)

    def update_task(self, task_id: str, **fields) -> bool:
        t = self.get_task(task_id, include_deleted=True)
        if not t:
            return False
        # record pre-change snapshot
        self._record_history(t, "update")
        changed = False
        for k, v in fields.items():
            if k in ["title", "notes", "tags", "due", "status", "recurrence", "priority"]:
                t[k] = v
                changed = True
        if changed:
            t["updated_at"] = _now_iso()
            self._save()
        return True

    def delete_task(self, task_id: str, hard: bool = False) -> bool:
        t = self.get_task(task_id, include_deleted=True)
        if not t:
            return False
        if hard:
            # record history externally to preserve a chance to recover if needed
            self._record_history(t, "delete_hard")
            self.tasks = [x for x in self.tasks if x.get("id") != task_id]
            self._save()
            return True
        else:
            if t.get("deleted"):
                return False
            self._record_history(t, "delete_soft")
            t["deleted"] = True
            t["updated_at"] = _now_iso()
            self._save()
            return True

    def delete_all_tasks(self):
        """Delete all tasks permanently."""
        self.tasks = []
        self._save()

    def undo(self, task_id: str, steps: int = 1) -> bool:
        t = self.get_task(task_id, include_deleted=True)
        if not t:
            return False
        history = t.get("history") or []
        if not history:
            return False
        if steps <= 0:
            return False
        if steps > len(history):
            return False
        # revert to snapshot before the last `steps` actions
        target = history[-steps]["snapshot"]
        # record current as history entry
        self._record_history(t, "undo")
        # restore fields except history
        for k in list(t.keys()):
            if k == "history":
                continue
            t.pop(k, None)
        t.update(target)
        t.setdefault("history", history[:-steps])
        t["updated_at"] = _now_iso()
        self._save()
        return True

    def search_tasks(self, query: str) -> List[Dict]:
        """Search tasks by a query in title or notes."""
        query = query.strip('"').lower()  # Sanitize the query
        tasks = self.list_tasks()
        results = [
            task for task in tasks
            if query in task.get("title", "").lower() or query in task.get("notes", "").lower()
        ]
        return results

    def _notification_worker(self):
        while True:
            now = datetime.now(timezone.utc)
            for task in self.tasks:
                if task.get("due") and not task.get("notified"):
                    due_time = datetime.fromisoformat(task["due"][:-1]).replace(tzinfo=timezone.utc)
                    if now >= due_time:
                        notification = f"Notification: Task '{task['title']}' is due!"
                        self.notifications.append(notification)
                        print(notification)
                        task["notified"] = True
                        self._save()
            time.sleep(60)  # Check every minute


if __name__ == "__main__":
    print("This module provides TaskManager class. Use the CLI.")

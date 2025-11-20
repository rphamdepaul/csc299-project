"""JSON-backed task storage for the task manager.

API:
- TaskStore(path)
- add_task(title, description='', due=None, tags=None)
- list_tasks()
- search_tasks(query)
- get_task(task_id)
- edit_task(task_id, **fields)
- delete_task(task_id)

Tasks are stored as a list of dicts in the JSON file. Each task has:
- id (uuid4 hex)
- title
- description
- created_at (ISO datetime)
- due (ISO date/time or None)
- tags (list)
- completed (bool)
"""
from __future__ import annotations

import json
import os
from typing import List, Dict, Optional, Any
from uuid import uuid4
from datetime import datetime


class TaskNotFound(Exception):
    pass


class TaskStore:
    def __init__(self, path: str = "tasks.json"):
        self.path = path
        # ensure directory exists
        parent = os.path.dirname(os.path.abspath(self.path))
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)

    def _load(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return data
            except json.JSONDecodeError:
                return []

    def _save(self, tasks: List[Dict[str, Any]]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)

    def add_task(
        self,
        title: str,
        description: str = "",
        due: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        tasks = self._load()
        task = {
            "id": uuid4().hex,
            "title": title,
            "description": description,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "due": due,
            "tags": list(tags) if tags else [],
            "completed": False,
        }
        tasks.append(task)
        self._save(tasks)
        return task

    def list_tasks(self, include_completed: bool = True) -> List[Dict[str, Any]]:
        tasks = self._load()
        if include_completed:
            return tasks
        return [t for t in tasks if not t.get("completed")]

    def search_tasks(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower()
        results = []
        for t in self._load():
            if q in (t.get("title", "") or "").lower() or q in (
                t.get("description", "") or ""
            ).lower():
                results.append(t)
                continue
            tags = t.get("tags") or []
            if any(q in tag.lower() for tag in tags):
                results.append(t)
                continue
        return results

    def get_task(self, task_id: str) -> Dict[str, Any]:
        for t in self._load():
            if t.get("id") == task_id:
                return t
        raise TaskNotFound(task_id)

    def edit_task(self, task_id: str, **fields) -> Dict[str, Any]:
        tasks = self._load()
        for i, t in enumerate(tasks):
            if t.get("id") == task_id:
                # allowed fields: title, description, due, tags, completed
                for k in ("title", "description", "due", "tags", "completed"):
                    if k in fields:
                        t[k] = fields[k]
                tasks[i] = t
                self._save(tasks)
                return t
        raise TaskNotFound(task_id)

    def delete_task(self, task_id: str) -> None:
        tasks = self._load()
        new = [t for t in tasks if t.get("id") != task_id]
        if len(new) == len(tasks):
            raise TaskNotFound(task_id)
        self._save(new)

    # convenience util for tests or maintenance
    def clear(self) -> None:
        self._save([])


if __name__ == "__main__":
    print("TaskStore module — import and use TaskStore in your application")

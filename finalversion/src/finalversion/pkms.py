import json
from pathlib import Path
from threading import Lock
from typing import List, Dict

class PKMS:
    def __init__(self, storage_path):
        self.storage_path = Path(storage_path)
        self.lock = Lock()
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.storage_path.is_file():
            self._atomic_save({})  # Explicitly create the file with an empty dictionary

    def _atomic_save(self, data):
        temp_path = self.storage_path.with_suffix('.tmp')
        with temp_path.open('w') as temp_file:
            json.dump(data, temp_file, indent=4)
        temp_path.replace(self.storage_path)

    def _load_data(self):
        with self.storage_path.open('r') as file:
            data = json.load(file)
            return data

    def add(self, title, content, priority="medium"):
        with self.lock:
            data = self._load_data()
            if any(note["title"] == title for note in data.values() if isinstance(note, dict)):
                raise ValueError(f"A note with the title '{title}' already exists.")
            existing_ids = {note["id"] for note in data.values() if isinstance(note, dict) and "id" in note}
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            sanitized_title = title.strip().strip('"') if title.strip() else "Untitled"
            sanitized_content = content.replace('"', '').strip()
            if priority not in ["low", "medium", "high"]:
                priority = "medium"
            note = {
                "id": new_id,
                "title": sanitized_title,
                "content": sanitized_content,
                "priority": priority,
                "created_at": self._now_iso(),
                "updated_at": self._now_iso(),
            }
            data[str(new_id)] = note
            self._atomic_save(data)
            return note

    def add_auto(self, text):
        with self.lock:
            data = self._load_data()
            existing_ids = {note["id"] for note in data.values() if isinstance(note, dict) and "id" in note}
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            # Require quoted title before colon
            import re
            match = re.match(r'"([^"]+)":(.*)', text)
            if match:
                sanitized_title = match.group(1).strip()
                sanitized_content = match.group(2).replace('"', '').strip()
            else:
                sanitized_title = "Untitled"
                sanitized_content = text.replace('"', '').strip()
            note = {
                "id": new_id,
                "title": sanitized_title,
                "content": sanitized_content,
                "created_at": self._now_iso(),
                "updated_at": self._now_iso(),
            }
            data[str(new_id)] = note
            self._atomic_save(data)
            return note

    def list(self):
        with self.lock:
            return list(self._load_data().values())

    def get(self, note_id):
        with self.lock:
            data = self._load_data()
            return data.get(note_id, None)

    def search(self, query):
        query = query.strip('"')  # Remove extra quotation marks from the query
        with self.lock:
            data = self._load_data()
            return [
                note for note in data.values()
                if query.lower() in note.get("title", "").lower() or query.lower() in note.get("content", "").lower()
            ]

    def delete(self, note_id):
        with self.lock:
            data = self._load_data()
            if note_id in data:
                del data[note_id]
                self._atomic_save(data)
            else:
                raise ValueError(f"Note with ID {note_id} does not exist.")

    def delete_all(self):
        with self.lock:
            self._atomic_save({})

    def _now_iso(self):
        """Return the current time in ISO format."""
        from datetime import datetime
        return datetime.now().isoformat()
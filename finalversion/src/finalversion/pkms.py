import json
from pathlib import Path
from threading import Lock
from typing import List, Dict

class PKMS:
    def __init__(self, storage_path):
        self.storage_path = Path(storage_path)
        self.lock = Lock()
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.storage_path.exists():
            self._atomic_save({})

    def _atomic_save(self, data):
        temp_path = self.storage_path.with_suffix('.tmp')
        with temp_path.open('w') as temp_file:
            json.dump(data, temp_file, indent=4)
        temp_path.replace(self.storage_path)

    def _load_data(self):
        with self.storage_path.open('r') as file:
            return json.load(file)

    def add(self, title, content):
        with self.lock:
            data = self._load_data()
            # Find the lowest unused ID greater than 0
            existing_ids = {note["id"] for note in data.values() if "id" in note}
            new_id = 1
            while new_id in existing_ids:
                new_id += 1

            # Ensure title and content are sanitized and validated
            sanitized_title = title.strip().strip('"') if title.strip() else "Untitled"
            sanitized_content = content.replace('"', '').strip()  # Remove all quotation marks and extra spaces

            note = {
                "id": new_id,  # User-friendly ID
                "title": sanitized_title,
                "content": sanitized_content,
                "created_at": self._now_iso(),
                "updated_at": self._now_iso(),
            }
            data[str(new_id)] = note
            self._atomic_save(data)

    def list(self):
        with self.lock:
            return list(self._load_data().keys())

    def get(self, note_id):
        with self.lock:
            data = self._load_data()
            return data.get(note_id, None)

    def search(self, query):
        query = query.strip('"')  # Remove extra quotation marks from the query
        with self.lock:
            data = self._load_data()
            return {
                k: v for k, v in data.items()
                if query.lower() in v.get("title", "").lower() or query.lower() in v.get("content", "").lower()
            }

    def delete(self, note_id):
        with self.lock:
            data = self._load_data()
            if note_id in data:
                del data[note_id]
                self._atomic_save(data)
            else:
                raise ValueError(f"Note with ID {note_id} does not exist.")

    def update(self, note_id, new_content):
        """Update the content of an existing note."""
        with self.lock:
            data = self._load_data()
            if note_id not in data:
                raise ValueError(f"Note with ID {note_id} does not exist.")
            data[note_id] = new_content
            self._atomic_save(data)

    def export_notes(self, export_path):
        """Export all notes to a specified file path."""
        with self.lock:
            data = self._load_data()
            with open(export_path, 'w') as export_file:
                json.dump(data, export_file, indent=4)

    def delete_all_notes(self):
        """Delete all notes permanently."""
        with self.lock:
            self._atomic_save({})

    def _now_iso(self):
        """Return the current time in ISO format."""
        from datetime import datetime
        return datetime.now().isoformat()

    def list_notes(self) -> List[str]:
        # Return a formatted list of notes with their titles and content only
        with self.lock:
            data = self._load_data()
            return [
                f"- \"{note['title']}\" \"{note['content']}\""
                for note in data.values()
                if 'title' in note and 'content' in note
            ]
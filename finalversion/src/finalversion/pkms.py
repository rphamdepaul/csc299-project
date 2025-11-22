import json
from pathlib import Path
from threading import Lock

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

    def add(self, note_id, content):
        with self.lock:
            data = self._load_data()
            if note_id in data:
                raise ValueError(f"Note with ID {note_id} already exists.")
            data[note_id] = content
            self._atomic_save(data)

    def list(self):
        with self.lock:
            return list(self._load_data().keys())

    def get(self, note_id):
        with self.lock:
            data = self._load_data()
            return data.get(note_id, None)

    def search(self, query):
        with self.lock:
            data = self._load_data()
            return {k: v for k, v in data.items() if query.lower() in v.lower()}

    def delete(self, note_id):
        with self.lock:
            data = self._load_data()
            if note_id in data:
                del data[note_id]
                self._atomic_save(data)
            else:
                raise ValueError(f"Note with ID {note_id} does not exist.")
# Documentation

## Personal Knowledge Management System (PKMS)

### Overview
The PKMS is a module for managing personal notes. It provides functionalities to add, list, retrieve, search, and delete notes. Notes are stored in a JSON file, ensuring data persistence.

### Usage

#### Initialization
```python
from src.finalversion.pkms import PKMS
pkms = PKMS('path/to/storage.json')
```

#### Adding a Note
```python
pkms.add('note_id', 'This is a note.')
```

#### Listing Notes
```python
note_ids = pkms.list()
```

#### Retrieving a Note
```python
content = pkms.get('note_id')
```

#### Searching Notes
```python
results = pkms.search('query')
```

#### Deleting a Note
```python
pkms.delete('note_id')
```

### Implementation Details
- Atomic saves ensure data integrity.
- Thread-safe operations using locks.

### Testing
Refer to `tests.md` for details on test cases.

---

## Task Management System

### New Features
- **Task Prioritization**: Tasks can have a priority level (low, medium, high). Tasks can also be filtered by priority.

### Usage

#### Adding a Task with Priority
```python
from tasks3.src.tasks3.improved_task_manager import TaskManager
tm = TaskManager('path/to/tasks.json')
task = tm.add_task('Task Title', priority='high')
```

#### Listing Tasks with Priority Filter
```python
tasks = tm.list_tasks(priority_filter='low')
```
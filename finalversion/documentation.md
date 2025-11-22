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
- **Task Notifications**: Tasks with due dates trigger notifications when they are due.

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

#### Adding a Task with Due Date
```python
from tasks3.src.tasks3.improved_task_manager import TaskManager
tm = TaskManager('path/to/tasks.json')
due_time = "2025-11-22T15:00:00Z"
task = tm.add_task('Task Title', due=due_time)
```

#### Notifications
Notifications are printed to the console when a task is due.

---

## Task Manager (from tasks3)

### Overview
The Task Manager is a module for managing personal tasks. It provides functionalities to add, list, retrieve, update, delete, and undo changes to tasks. Tasks are stored in a JSON file (`tasks_new.json`), ensuring data persistence.

### Usage

#### Adding a Task
```python
from tasks3.src.tasks3.improved_task_manager import TaskManager
tm = TaskManager('path/to/tasks.json')
task = tm.add_task('Task Title', notes='Details about the task', tags=['tag1'], due='2025-11-22T15:00:00Z', priority='high')
```

#### Listing Tasks
```python
tasks = tm.list_tasks(priority_filter='low', include_deleted=False)
```

#### Retrieving a Task
```python
task = tm.get_task('task_id')
```

#### Updating a Task
```python
tm.update_task('task_id', title='Updated Title', priority='medium')
```

#### Deleting a Task
```python
tm.delete_task('task_id', hard=True)
```

#### Undoing Changes
```python
tm.undo('task_id', steps=1)
```

---

## Terminal Chat Interface

### Overview
The terminal-based chat interface allows users to interact with the PKMS and TaskManager. Users can add, list, and search notes, as well as add and list tasks.

### Usage

#### Running the Chat Interface
```bash
python src/finalversion/chat.py
```

#### Example Commands
```plaintext
> add_note 1 First note
> list_notes
> search_notes First
> add_task First task
> list_tasks
> exit
```

---

## TasksAdapter

### Overview
The `TasksAdapter` provides a simplified interface for managing tasks using the `TaskManager` from `tasks3`.

### Usage

#### Initialization
```python
from src.finalversion.tasks_adapter import TasksAdapter
adapter = TasksAdapter('path/to/tasks.json')
```

#### Adding a Task
```python
adapter.add_task('Task Title')
```

#### Listing Tasks
```python
tasks = adapter.list_tasks()
```

#### Deleting a Task
```python
adapter.delete_task('task_id')
```

#### Updating a Task
```python
adapter.update_task('task_id', title='Updated Title')
```
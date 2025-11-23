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
pkms.add('Note Title', 'This is the content of the note.')
```

#### Listing Notes
```python
notes = pkms.list()
# Returns a list of note objects with their details
```

#### Retrieving a Note
```python
note = pkms.get('note_id')
# Returns the note object or None if not found
```

#### Searching Notes
```python
results = pkms.search('query')
# Returns a list of note objects matching the query
```

#### Deleting a Note
```python
pkms.delete('note_id')
```

### Implementation Details
- **Thread Safety**: All operations are thread-safe using locks.
- **Validation**: Input is sanitized to ensure data integrity.
- **Error Handling**: Raises appropriate exceptions for invalid operations.

---

## Task Management System

### New Features
- **Task Prioritization**: Tasks can have a priority level (low, medium, high). Tasks can also be filtered by priority.
- **Task Notifications**: Tasks with due dates trigger notifications when they are due.

### Usage

#### Adding a Task with Priority
```python
from src.finalversion.improved_task_manager import TaskManager
tm = TaskManager('path/to/tasks.json')
task = tm.add_task('Task Title', priority='high')
```

#### Listing Tasks with Priority Filter
```python
tasks = tm.list_tasks(priority_filter='low')
```

#### Adding a Task with Due Date
```python
from src.finalversion.improved_task_manager import TaskManager
tm = TaskManager('path/to/tasks.json')
due_time = "2025-11-22T15:00:00Z"
task = tm.add_task('Task Title', due=due_time)
```

#### Notifications
Notifications are printed to the console when a task is due.

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
The `TasksAdapter` provides a simplified interface for managing tasks using the `TaskManager`.

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

---

## CLI Entrypoint

### Overview
The CLI entrypoint allows users to manage notes and tasks directly from the terminal. It provides a simple interface for interacting with the `PKMS` and `TasksAdapter` modules.

### Usage

#### Adding a Note
```bash
python src/finalversion/cli.py notes add <id> <content>
```

#### Listing Notes
```bash
python src/finalversion/cli.py notes list
```

#### Adding a Task
```bash
python src/finalversion/cli.py tasks add <title>
```

#### Listing Tasks
```bash
python src/finalversion/cli.py tasks list
```
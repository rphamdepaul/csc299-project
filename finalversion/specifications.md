# Specifications

## Personal Knowledge Management System (PKMS)

### Core Functionalities
- **Add Notes**: Add a note with a unique identifier and content.
- **List Notes**: Retrieve a list of all note identifiers.
- **Get Note**: Retrieve the content of a note by its identifier.
- **Search Notes**: Search for notes containing a specific query.
- **Delete Note**: Remove a note by its identifier.

### New Features
- **Task Prioritization**: Tasks can have a priority level (low, medium, high). Tasks can also be filtered by priority.
- **Task Notifications**: Tasks with due dates trigger notifications when they are due.

### Implementation Details
- Notes are stored in a JSON file.
- Atomic saves ensure data integrity.
- Thread-safe operations using locks.

### File Structure
- Implementation: `src/finalversion/pkms.py`
- Tests: `finalversion/tests/test_pkms.py`

## Task Manager (from tasks3)

### Core Functionalities
- **Add Tasks**: Add a task with details like title, notes, tags, due date, and priority.
- **List Tasks**: Retrieve tasks with optional filters for priority and inclusion of deleted tasks.
- **Get Task**: Retrieve task details by ID.
- **Update Task**: Modify task details.
- **Delete Task**: Soft or hard delete tasks.
- **Undo Changes**: Revert changes to a task.

### Implementation Details
- Tasks are stored in a JSON file (`tasks_new.json`).
- Atomic saves ensure data integrity.
- Task history is maintained for updates and deletions.

## TaskManager Adapter

### Overview
The `TasksAdapter` class wraps the `TaskManager` from `tasks3` to provide a simplified API for managing tasks. It supports adding, listing, deleting, and updating tasks.

### Core Functionalities
- **Add Task**: Add a task with a title and optional due date.
- **List Tasks**: Retrieve all tasks.
- **Delete Task**: Remove a task by its ID.
- **Update Task**: Modify task details.

### Implementation Details
- The adapter uses the `TaskManager` class from `tasks3`.
- Tasks are stored in a JSON file (`tasks_new.json`).
- Atomic saves ensure data integrity.

### File Structure
- Implementation: `src/finalversion/tasks_adapter.py`
- Tests: `finalversion/tests/test_tasks_adapter.py`

## Terminal Chat Interface

### Overview
The terminal-based chat interface allows users to interact with the PKMS and TaskManager. Users can add, list, and search notes, as well as add and list tasks.

### Commands
- `add_note <id> <content>`: Add a new note.
- `list_notes`: List all notes.
- `search_notes <query>`: Search notes by query.
- `add_task <title>`: Add a new task.
- `list_tasks`: List all tasks.
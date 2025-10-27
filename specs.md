# Project Plan: Task Manager

## Overview
The `task-manager` is a command-line application written in Python that allows users to manage tasks. Tasks are stored in a JSON file named `tasks.json`, located in the root directory of the project. Each task will have an ID, title, and a short description. The application will support adding, listing, and searching tasks.

---

## Features

### 1. Add Task
- **Description**: Allows the user to add a new task.
- **Input**:
  - Title (string)
  - Description (string)
- **Output**: The task is saved to `tasks.json` with a unique ID.

### 2. List Tasks
- **Description**: Displays all tasks stored in `tasks.json`.
- **Output**: A list of tasks with their IDs, titles, and descriptions.

### 3. Search Tasks
- **Description**: Allows the user to search for tasks by title or description.
- **Input**: Search query (string).
- **Output**: A list of tasks matching the search query.

---

## Data Structure

### Task
- **ID**: A unique identifier for the task (integer or UUID).
- **Title**: The title of the task (string).
- **Description**: A short description of the task (string).

### JSON File (`tasks.json`)
- Format: Array of task objects.
- Example:
  ```json
  [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, eggs, and bread"
    },
    {
      "id": 2,
      "title": "Call mom",
      "description": "Check in and say hello"
    }
  ]
  ```

---

## Command-Line Interface (CLI)

### Commands
1. **Add Task**:
   - Command: `python task_manager.py add`
   - Prompts the user for title and description.

2. **List Tasks**:
   - Command: `python task_manager.py list`
   - Displays all tasks.

3. **Search Tasks**:
   - Command: `python task_manager.py search <query>`
   - Displays tasks matching the query.

---

## Implementation Plan

### Step 1: Project Setup
- Create the project directory structure.
- Initialize the `tasks.json` file with an empty array (`[]`).

### Step 2: Define the Data Model
- Create a Python class or functions to handle task creation, listing, and searching.

### Step 3: Implement CLI Commands
- Use `argparse` to handle command-line arguments.
- Implement the `add`, `list`, and `search` commands.

### Step 4: File Operations
- Implement functions to read from and write to `tasks.json`.

### Step 5: Testing
- Test each feature manually to ensure correctness.
- Write unit tests for core functionality.

### Step 6: Documentation
- Add usage instructions and examples to a `README.md` file.

---

## Tools and Libraries
- Python 3.8+
- `argparse` for CLI argument parsing.
- `json` for reading and writing the `tasks.json` file.

---

## Future Enhancements
- Add task deletion and editing functionality.
- Support for task prioritization and deadlines.
- Implement a more robust search (e.g., case-insensitive or fuzzy matching).
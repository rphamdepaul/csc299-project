# Task Manager CLI

## Overview
The Task Manager CLI allows users to manage tasks stored in a JSON file. Users can add, list, and search tasks using simple commands.

## Installation
1. Ensure Python 3.8+ is installed on your system.
2. Clone the repository or download the project files.
3. Navigate to the project directory.

## Usage

### Add a Task
```bash
python task_manager_cli.py add --title "Task Title" --description "Task Description"
```

### List All Tasks
```bash
python task_manager_cli.py list
```

### Search for Tasks
```bash
python task_manager_cli.py search --query "Search Query"
```

## Example

1. Add a task:
   ```bash
   python task_manager_cli.py add --title "Buy groceries" --description "Milk, eggs, and bread"
   ```

2. List tasks:
   ```bash
   python task_manager_cli.py list
   ```

3. Search tasks:
   ```bash
   python task_manager_cli.py search --query "groceries"
   ```

## Future Enhancements
- Add task deletion and editing functionality.
- Support for task prioritization and deadlines.
- Implement a more robust search (e.g., case-insensitive or fuzzy matching).
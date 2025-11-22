# CSC299 Project

## Overview
This project is a modular CLI-based software designed to manage tasks and notes. It includes a Personal Knowledge Management System (PKMS), a TaskManager, and a terminal-based chat interface. The software is under active development, and features will be updated as tasks are completed.

## Current Features
- **TaskManager**: Add, list, update, and delete tasks with support for priorities and notifications.
- **Modular Design**: Components are designed to be reusable and extensible.
- **Terminal Chat Interface**: Fully implemented. Allows interaction with PKMS and TaskManager via terminal commands.

## Prerequisites
1. **Python**: Ensure Python 3.10 or later is installed.
2. **Dependencies**: Install required packages using pip:
   ```bash
   pip3 install -r requirements.txt
   ```

## How to Use

### 1. Set Up the Environment
- Clone the repository to your local machine:
  ```bash
  git clone <repository-url>
  cd csc299-project/finalversion
  ```
- Install dependencies:
  ```bash
  pip3 install -r requirements.txt
  ```

### 2. Run the TaskManager
- Use the `TaskManager` programmatically:
  ```python
  from src.finalversion.improved_task_manager import TaskManager

  tm = TaskManager()
  tm.add_task("Example Task", "This is a test task.")
  print(tm.list_tasks())
  ```

### 3. Chat Interface
- The chat interface will allow users to interact with the PKMS and TaskManager via terminal commands. Once implemented, it can be launched using:
  ```bash
  python src/finalversion/chat.py
  ```
- Example commands:
  ```plaintext
  > add_note 1 First note
  > list_notes
  > search_notes First
  > add_task First task
  > list_tasks
  > exit
  ```

### 4. CLI Commands
- The CLI entry point is under development. Once implemented, it will allow managing notes and tasks via terminal commands.

### 5. Testing
- Run the test suite to validate functionality:
  ```bash
  pytest
  ```

## Roadmap
- Implement PKMS core module.
- Integrate TaskManager adapter for simplified API.
- Complete CLI entry point and chat interface.
- Add AI agent stubs for summarizing notes and creating tasks.
- Enhance TaskManager with prioritization and notification features.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
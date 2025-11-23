# CSC299 Project

## Overview
This project is a modular CLI-based software designed to manage tasks and notes. It includes a Personal Knowledge Management System (PKMS), a TaskManager, and a terminal-based chat interface. The software is under active development, and features will be updated as tasks are completed.

## Current Features
- **PKMS**: Add, list, and delete notes stored in JSON format.
- **TaskManager**: Add, list, and delete tasks with support for future prioritization and notifications.
- **CLI Interface**: Manage notes and tasks, and launch the chat interface via terminal commands.
- **Terminal Chat Interface**: Allows interaction with PKMS and TaskManager via a conversational interface.
- **Modular Design**: Components are designed to be reusable and extensible.

## Prerequisites
1. **Python**: Ensure Python 3.10 or later is installed.
2. **Dependencies**: Install required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. **Setup the Chat Command**: Run the setup script to enable the `chat` command:
   ```bash
   ./setup.sh
   ```
   This will make the `chat` command globally available in your terminal.

## How to Use

### 1. Set Up the Environment
- Clone the repository to your local machine:
  ```bash
  git clone <repository-url>
  cd csc299-project/finalversion
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run the setup script:
  ```bash
  ./setup.sh
  ```

### 2. Run the CLI
- Use the CLI to manage notes and tasks or launch the chat interface:
  ```bash
  chat
  ```
- Example commands:
  ```bash
  # Add a note (provide both title and content, ID is auto-generated)
  add_note "Note Title" "This is the content of the note."

  # List all notes
  list_notes

  # Delete a note
  delete_note 1

  # Add a task (provide both title and description, ID is auto-generated)
  add_task "Task Title" "This is the description of the task."

  # List all tasks
  list_tasks

  # Delete a task
  delete_task 1

  # Launch the chat interface
  chat
  ```

### 3. Setup the Chat Command
- If you want to run the setup script:
  ```bash
  chmod +x ./setup.sh
  ./setup.sh
  ```
- Alternatively, if you prefer not to run the script, you can manually set up the `chat` command:
  ```bash
  chmod +x src/finalversion/chat.py
  sudo ln -sf $(pwd)/src/finalversion/chat.py /usr/local/bin/chat
  ```

### 4. Testing
- Run the test suite to validate functionality:
  ```bash
  pytest
  ```

### 5. Steps to Open the Chat Interface

If you have cloned this repository and want to use the `chat` interface, follow these steps:

1. **Install Python and Dependencies**:
   - Ensure Python 3.10 or later is installed.
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Set Up the Chat Command**:
   - Run the setup script to enable the `chat` command:
     ```bash
     chmod +x ./setup.sh
     ./setup.sh
     ```
   - Alternatively, manually set up the `chat` command:
     ```bash
     chmod +x src/finalversion/chat.py
     sudo ln -sf $(pwd)/src/finalversion/chat.py /usr/local/bin/chat
     ```

3. **Verify the Setup**:
   - Ensure the `chat` command is available by typing:
     ```bash
     chat
     ```
   - If the interface does not open, ensure the `src` directory is in your Python path. You can add it dynamically by modifying the `chat.py` script (already included in this repository).

4. **Run the Chat Interface**:
   - Once the setup is complete, you can launch the chat interface by typing:
     ```bash
     chat
     ```

### 6. Available Commands

Here is a list of all available commands in the chat interface, grouped by functionality:

#### Note Commands:
- **add_note <content>**: Add a new note with the specified content. The ID is auto-generated.
- **list_notes**: List all notes with their IDs and content in the format `-1: <content>`.
- **search_notes <query>**: Search notes by the specified query. Displays the ID, title, and content of matching notes.
- **delete_note <id>**: Delete a note by its ID.

#### Task Commands:
- **add_task <title>**: Add a new task with the specified title. The ID is auto-generated.
- **list_tasks**: List all tasks with their IDs and titles.
- **search_tasks <query>**: Search tasks by the specified query. Displays the ID, title, and description of matching tasks.
- **delete_task <id>**: Delete a task by its ID.
- **delete_all_tasks**: Delete all tasks. A confirmation prompt will appear before deletion.

#### General Commands:
- **help**: Display a list of all available commands.
- **exit**: Exit the chat interface.

## Roadmap
- Add AI agent stubs for summarizing notes and creating tasks.
- Enhance TaskManager with prioritization and notification features.
- Run full test suite to validate recent changes and catch regressions.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
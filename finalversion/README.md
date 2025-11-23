# CSC299 Project

## Overview
This project is a modular CLI-based software designed to manage tasks and notes. It includes a Personal Knowledge Management System (PKMS), a TaskManager, and a terminal-based chat interface.

## Prerequisites
1. **Python**: Ensure Python 3.10 or later is installed.
2. **Dependencies**: Install required packages using pip:
   ```bash
   pip install -r requirements.txt
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

### 3. Testing
- To run tests, use the following command:
  ```bash
  PYTHONPATH=$(pwd)/src pytest
  ```
- Example for running specific tests:
  ```bash
  PYTHONPATH=$(pwd)/src pytest tests/test_pkms.py
  ```
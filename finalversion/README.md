
# CSC299 Project: AI-Driven PKMS & Task Manager

## Overview
This project demonstrates how to use AI coding assistants to plan, specify, develop, and test a modular Python application for:

- **Personal Knowledge Management System (PKMS):** Add, list, search, and delete notes. Notes are stored in portable JSON files.
- **Personal Task Management System:** Add, list, and delete tasks with priorities and due dates. Tasks are stored in JSON files.
- **Terminal-Based Chat Interface:** Interact with your notes and tasks using natural language commands in the terminal.
- **AI Agents:** Summarize notes or tasks using OpenAI's API.

All code is written in Python and runs portably on Windows, macOS, and Linux. No platform-specific dependencies. State is stored in JSON documents for maximum portability and transparency.

## Prerequisites
- **Python 3.10+**
- **Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
- **OpenAI API Key:**
   ```bash
   export OPENAI_API_KEY=your-own-api-key-here
   ```
   *Do NOT share your API key publicly. Each user should use their own key.*


## How to Run the Software

### Prerequisites
1. **Python 3.10 or later** installed on your system (Windows, macOS, or Linux).
2. **Install dependencies** (in your terminal):
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your OpenAI API key** (for AI summarization, in your terminal):
   ```bash
   export OPENAI_API_KEY=your-own-api-key-here
   ```

### Running the Software in Your Terminal
1. **Clone the repository and install dependencies** (in your terminal):
   ```bash
   git clone <repository-url>
   cd csc299-project/finalversion
   pip install -r requirements.txt
   ```
2. **Start the chat interface** (in your terminal):
   ```bash
   python src/finalversion/cli.py chat
   ```
   This will open an interactive prompt in your terminal where you can manage notes and tasks using natural language commands. Type `help` to see all available commands.

3. **Run CLI commands directly** (in your terminal):
   - Add a note:
     ```bash
     python src/finalversion/cli.py notes add <id> "Note Content"
     ```
   - List notes:
     ```bash
     python src/finalversion/cli.py notes list
     ```
   - Delete a note:
     ```bash
     python src/finalversion/cli.py notes delete <id>
     ```
   - Add a task:
     ```bash
     python src/finalversion/cli.py tasks add "Task Title"
     ```
   - List tasks:
     ```bash
     python src/finalversion/cli.py tasks list
     ```
   - Delete a task (by index):
     ```bash
     python src/finalversion/cli.py tasks delete <task_id>
     ```

**Tip:** All commands can be run directly in your terminal from the `csc299-project/finalversion` directory. For the chat interface, type commands interactively after running `python src/finalversion/cli.py chat`.


## Chat Interface Commands & Syntax

Copy and paste these commands directly into the chat interface prompt. Each command is followed by a brief explanation:

```plaintext
add note "Shopping List": Milk, eggs, bread         # Adds a new note with a quoted title and content
add note 1 Buy groceries                            # Adds a new note with a specific ID and content
list notes                                          # Lists all notes with their IDs and titles
search notes groceries                              # Searches notes by keyword in title or content
delete note 1                                       # Deletes the note with the given ID
add task Finish report 2025-12-01 2:00 PM high      # Adds a new task with description, due date, and priority
list tasks                                          # Lists all tasks with their index, title, priority, and due date
delete task 2                                       # Deletes the task at the given position in the list
ai agent summarize 1                                # Summarizes the note or task at the given index using AI
help                                                # Shows all available commands
exit                                                # Quits the chat interface
```

**Example session:**
```plaintext
add note "Shopping List": Milk, eggs, bread
add note "Meeting Notes": Discuss project timeline
list notes
search notes Shopping
delete note 1
list notes
add task Finish the project documentation 2025-12-01 2:00 PM high
add task Review code for bugs 2025-12-02 9:30 AM medium
add task Submit assignment 2025-12-03 23:59 low
list tasks
delete task 1
ai agent summarize 2
help
exit
```

## What Each Command Does
- **add note "<title>": <content>**: Adds a note with a quoted title and content. The ID is auto-assigned.
- **add note <id> <content>**: Adds a note with a specific ID and content.
- **list notes**: Displays all notes stored in the system.
- **search notes <query>**: Finds notes containing the query in their title or content.
- **delete note <id>**: Removes the note with the specified ID.
- **add task <desc> <due> <priority>**: Adds a task with description, due date, and priority (low/medium/high).
- **list tasks**: Shows all tasks with their index, title, priority, and due date.
- **delete task <index>**: Deletes the task at the given index in the list.
- **ai agent summarize <index>**: Uses AI to summarize the note or task at the given index.
- **help**: Lists all available commands and their syntax.
- **exit**: Exits the chat interface.

## Features & Commands

### PKMS (Notes)
- Add a note by ID:
   ```bash
   python src/finalversion/cli.py notes add <id> "Note Content"
   ```
- List notes:
   ```bash
   python src/finalversion/cli.py notes list
   ```
- Delete a note:
   ```bash
   python src/finalversion/cli.py notes delete <id>
   ```
- Search notes (chat interface only):
   ```
   search notes <query>
   ```

### TaskManager (Tasks)
- Add a task:
   ```bash
   python src/finalversion/cli.py tasks add "Task Title"
   ```
- List tasks:
   ```bash
   python src/finalversion/cli.py tasks list
   ```
- Delete a task (by index):
   ```bash
   python src/finalversion/cli.py tasks delete <task_id>
   ```
- Add with due date and priority (chat interface):
   ```
   add task <description> <due_date> <priority>
   ```

### Chat Interface
Type these commands inside the chat prompt:

| Command                        | Function                                      |
|--------------------------------|-----------------------------------------------|
| add note "<title>": <content> | Add a new note (ID auto-assigned, title in quotes before ':') |
| add note <id> <content>        | Add a new note with a specific ID and content |
| list notes                     | List all notes                                |
| search notes <query>           | Search notes by keyword                       |
| delete note <id>               | Delete a note by its ID                       |
| add task <description> <due_date> <priority> | Add a new task (due date: YYYY-MM-DD HH:MM or YYYY-MM-DD HH:MM AM/PM, priority: low/medium/high) |
| list tasks                     | List all tasks with their index               |
| delete task <index>            | Delete a task by its position in the list     |
| ai agent summarize <index>     | Summarize the note or task at the given index using the AI agent |
| help                           | Show available commands                       |
| exit                           | Quit the chat interface                       |

**Example usage:**
```
add note "Shopping List": Milk, eggs, bread high
add note "Meeting Notes": Discuss project timeline low
list notes
search notes Shopping
delete note 1
list notes
add task Finish the project documentation 2025-12-01 2:00 PM high
add task Review code for bugs 2025-12-02 9:30 AM medium
add task Submit assignment 2025-12-03 23:59 low
list tasks
delete task 1
ai agent summarize 2
help
exit
```

## Architecture
- **Python only**: No platform-specific code; runs on Windows, macOS, Linux.
- **State storage**: All notes and tasks are stored in JSON files for portability and transparency.
- **AI agent**: Summarization uses OpenAI's API (user must provide their own API key).

## Testing
Run all tests:
```bash
PYTHONPATH=$(pwd)/src pytest
```
Run specific tests:
```bash
PYTHONPATH=$(pwd)/src pytest tests/test_pkms.py
```
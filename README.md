
# CSC299 Project: AI-Driven PKMS & Task Manager

## Overview
This project demonstrates how to use AI coding assistants to plan, specify, develop, and test a modular Python application for:

- **Personal Knowledge Management System (PKMS):** Add, list, and delete notes. Notes are stored in portable JSON files.
- **Personal Task Management System:** Add, list, and delete tasks with priorities and due dates. Tasks are stored in JSON files.
- **Terminal-Based Chat Interface:** Interact with your notes and tasks using natural language commands in the terminal.
- **AI Agents:** Summarize notes or tasks using OpenAI's API.

All code is written in Python and runs portably on Windows, macOS, and Linux. No platform-specific dependencies. State is stored in JSON documents for maximum portability and transparency.

## Prerequisites
- **Python 3.10+**
- **Dependencies:**
   From the `finalversion` directory:
   ```bash
   pip install -r requirements.txt
   ```
   Or from the `csc299-project` directory:
   ```bash
   pip install -r finalversion/requirements.txt
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
   - From the `csc299-project` directory:
      ```bash
      PYTHONPATH=finalversion/src python3 finalversion/src/finalversion/cli.py chat
      ```
    - From the `csc299-project/finalversion` directory:
       ```bash      add note 1 Buy groceries      add note "Book Ideas": Fantasy novel about time travel medium
       PYTHONPATH=$(pwd)/src python3 src/finalversion/cli.py chat
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

**Tip:**
- If you are running from the `csc299-project` directory, use:
   ```bash
   PYTHONPATH=finalversion/src python3 finalversion/src/finalversion/cli.py chat
   ```
- If you are running from the `csc299-project/finalversion` directory, use:
   ```bash
   python src/finalversion/cli.py chat
   ```
This ensures Python can find the `finalversion` package. If you run from another directory or without setting `PYTHONPATH`, you may get a `ModuleNotFoundError`.


## Chat Interface Commands

The chat interface provides the following commands. Type `help` inside the chat to see this list:

### Available Commands

| Command | Description |
|---------|-------------|
| `add note <id> <content> [priority]` | Add a note with a specific ID and content. Priority is optional (low/medium/high, defaults to medium) |
| `add note "Title": Content [priority]` | Add a note with a quoted title and content. ID is auto-assigned. Priority is optional |
| `list notes` | List all notes with their IDs, titles, and priorities |
| `delete note <id>` | Delete a specific note by its ID |
| `delete all notes` | Delete all notes from the system |
| `add task <description> <due_date> <priority>` | Add a task with description, due date (YYYY-MM-DD HH:MM AM/PM), and priority (low/medium/high) |
| `add task <description>` | Add a task with just a description (no due date, defaults to medium priority) |
| `list tasks` | List all tasks with their index, title, priority, and due date (if set) |
| `delete task <index>` | Delete a specific task by its position in the list |
| `delete all tasks` | Delete all tasks from the system |
| `ai agent summarize <index>` | Use AI to summarize a note or task at the given index (run `list notes` or `list tasks` first) |
| `help` | Display all available commands |
| `exit` | Exit the chat interface |

### Example Session

```plaintext
add note "Shopping List": Milk, eggs, bread high
add note "Meeting Notes": Discuss project timeline low
list notes
delete note 1
list notes
add task Finish the project documentation 2025-12-01 2:00 PM high
add task Review code for bugs 2025-12-02 9:30 AM medium
add task Submit assignment 2025-12-03 23:59 low
list tasks
delete task 1
ai agent summarize 1
delete all tasks
delete all notes
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
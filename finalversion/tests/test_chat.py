import subprocess
import tempfile
import os
import json

def test_chat_interface():
    with tempfile.TemporaryDirectory() as temp_dir:
        notes_file = os.path.join(temp_dir, "notes.json")
        tasks_file = os.path.join(temp_dir, "tasks.json")

        # Ensure the notes file is completely reset
        if os.path.exists(notes_file):
            os.remove(notes_file)
        with open(notes_file, "w") as f:
            json.dump({}, f)

        # Create a temporary script to simulate user input
        script = """
add_note 1 First note
list_notes
add_task First task
list_tasks
exit
"""
        script_file = os.path.join(temp_dir, "script.txt")
        with open(script_file, "w") as f:
            f.write(script)

        python_executable = "/Users/iexplode247/csc299-project/finalversion/.venv/bin/python"

        # Run the chat interface with the script as input
        result = subprocess.run(
            [python_executable, os.path.abspath("src/finalversion/chat.py")],
            input=script,
            text=True,
            capture_output=True,
            cwd="/Users/iexplode247/csc299-project/finalversion/src/finalversion",
            env={"PYTHONPATH": os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")), "TEST_MODE": "1"},
        )

        # Check the output
        stdout = result.stdout
        assert "DEBUG: Adding note with ID 1 and content First note" in stdout
        assert "Note '1' added." in stdout
        assert "Notes:" in stdout
        assert "- 1" in stdout
        assert "Task 'First task' added." in stdout
        assert "Tasks:" in stdout
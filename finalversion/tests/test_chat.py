import subprocess
import tempfile
import os

def test_chat_interface():
    with tempfile.TemporaryDirectory() as temp_dir:
        notes_file = os.path.join(temp_dir, "notes.json")
        tasks_file = os.path.join(temp_dir, "tasks.json")

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
            env={"PYTHONPATH": os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))},
        )

        # Check the output
        assert "Note '1' added." in result.stdout
        assert "Notes:" in result.stdout
        assert "- 1" in result.stdout
        assert "Task" in result.stdout
        assert "Tasks:" in result.stdout
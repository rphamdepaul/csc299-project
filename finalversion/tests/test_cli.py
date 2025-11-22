import subprocess
import tempfile
import os

def test_add_and_list_notes():
    with tempfile.TemporaryDirectory() as temp_dir:
        python_executable = "/Users/iexplode247/csc299-project/finalversion/.venv/bin/python"
        cli_path = "/Users/iexplode247/csc299-project/finalversion/src/finalversion/cli.py"
        env = os.environ.copy()
        env["PYTHONPATH"] = "/Users/iexplode247/csc299-project/finalversion"

        result_add = subprocess.run(
            [python_executable, cli_path, "notes", "add", "1", "Test Note"],
            text=True,
            capture_output=True,
            cwd=temp_dir,
            env=env
        )
        assert "Note '1' added." in result_add.stdout

        result_list = subprocess.run(
            [python_executable, cli_path, "notes", "list"],
            text=True,
            capture_output=True,
            cwd=temp_dir,
            env=env
        )
        assert "Notes:" in result_list.stdout
        assert "- 1" in result_list.stdout

def test_add_and_list_tasks():
    with tempfile.TemporaryDirectory() as temp_dir:
        python_executable = "/Users/iexplode247/csc299-project/finalversion/.venv/bin/python"
        cli_path = "/Users/iexplode247/csc299-project/finalversion/src/finalversion/cli.py"
        env = os.environ.copy()
        env["PYTHONPATH"] = "/Users/iexplode247/csc299-project/finalversion"

        result_add = subprocess.run(
            [python_executable, cli_path, "tasks", "add", "Test Task"],
            text=True,
            capture_output=True,
            cwd=temp_dir,
            env=env
        )
        assert "Task 'Test Task' added." in result_add.stdout

        result_list = subprocess.run(
            [python_executable, cli_path, "tasks", "list"],
            text=True,
            capture_output=True,
            cwd=temp_dir,
            env=env
        )
        assert "Tasks:" in result_list.stdout
        assert "- Test Task" in result_list.stdout
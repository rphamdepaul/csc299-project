import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../finalversion/src')))

import pytest
from finalversion.tasks_adapter import TasksAdapter
import tempfile

@pytest.fixture
def temp_tasks_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        yield temp_file.name
    os.remove(temp_file.name)

def test_add_task(temp_tasks_file):
    adapter = TasksAdapter(temp_tasks_file)
    adapter.add_task("Test Task")
    tasks = adapter.list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"

def test_list_tasks(temp_tasks_file):
    adapter = TasksAdapter(temp_tasks_file)
    adapter.add_task("Task 1")
    adapter.add_task("Task 2")
    tasks = adapter.list_tasks()
    assert len(tasks) == 2

def test_delete_task(temp_tasks_file):
    adapter = TasksAdapter(temp_tasks_file)
    adapter.add_task("Task to Delete")
    tasks = adapter.list_tasks()
    task_id = tasks[0]["id"]
    adapter.delete_task(task_id)
    tasks = adapter.list_tasks()
    assert len(tasks) == 0

def test_update_task(temp_tasks_file):
    adapter = TasksAdapter(temp_tasks_file)
    adapter.add_task("Old Task")
    tasks = adapter.list_tasks()
    task_id = tasks[0]["id"]
    adapter.update_task(task_id, title="Updated Task")
    tasks = adapter.list_tasks()
    assert tasks[0]["title"] == "Updated Task"

def test_search_tasks(temp_tasks_file):
    adapter = TasksAdapter(temp_tasks_file)

    # Add tasks for testing
    adapter.add_task("Submit Report", "Prepare and submit the final project report by Friday")
    adapter.add_task("Team Meeting", "Discuss project milestones and deadlines")
    adapter.add_task("Code Review", "Review the latest pull requests")

    # Test searching for tasks
    results = adapter.search_tasks("report")
    assert len(results) == 1
    assert results[0]["title"] == "Submit Report"

    results = adapter.search_tasks("project")
    assert len(results) == 2

    results = adapter.search_tasks("review")
    assert len(results) == 1
    assert results[0]["title"] == "Code Review"

    results = adapter.search_tasks("nonexistent")
    assert len(results) == 0

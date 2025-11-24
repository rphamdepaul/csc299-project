import pytest
import os
import sys
import tempfile

# Ensure the `src` directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from finalversion.improved_task_manager import TaskManager

@pytest.fixture
def temp_task_manager():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = os.path.join(temp_dir, "tasks.json")
        yield TaskManager(temp_file)

def test_add_task_with_priority(temp_task_manager):
    task = temp_task_manager.add_task(user_id="user1", title="Test Task", priority="high")
    assert task["priority"] == "high"

def test_add_task_invalid_priority(temp_task_manager):
    task = temp_task_manager.add_task(user_id="user1", title="Invalid Priority Task", priority="urgent")
    assert task["priority"] == "medium"

def test_list_tasks_with_priority_filter(temp_task_manager):
    temp_task_manager.add_task(user_id="user1", title="Low Priority Task", priority="low")
    temp_task_manager.add_task(user_id="user1", title="High Priority Task", priority="high")
    filtered_tasks = temp_task_manager.list_tasks(priority_filter="low")
    assert len(filtered_tasks) == 1
    assert filtered_tasks[0]["priority"] == "low"

def test_list_tasks_invalid_priority_filter(temp_task_manager):
    with pytest.raises(ValueError):
        temp_task_manager.list_tasks(priority_filter="urgent")
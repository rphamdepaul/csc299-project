import pytest
from tasks3.src.tasks3.improved_task_manager import TaskManager
import tempfile
import os

@pytest.fixture
def temp_task_manager():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = os.path.join(temp_dir, "tasks.json")
        yield TaskManager(temp_file)

def test_add_task_with_priority(temp_task_manager):
    task = temp_task_manager.add_task("Test Task", priority="high")
    assert task["priority"] == "high"

def test_add_task_invalid_priority(temp_task_manager):
    with pytest.raises(ValueError):
        temp_task_manager.add_task("Invalid Priority Task", priority="urgent")

def test_list_tasks_with_priority_filter(temp_task_manager):
    temp_task_manager.add_task("Low Priority Task", priority="low")
    temp_task_manager.add_task("High Priority Task", priority="high")
    filtered_tasks = temp_task_manager.list_tasks(priority_filter="low")
    assert len(filtered_tasks) == 1
    assert filtered_tasks[0]["priority"] == "low"

def test_list_tasks_invalid_priority_filter(temp_task_manager):
    with pytest.raises(ValueError):
        temp_task_manager.list_tasks(priority_filter="urgent")
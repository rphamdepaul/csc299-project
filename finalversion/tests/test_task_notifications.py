import pytest
from src.finalversion.improved_task_manager import TaskManager
import tempfile
import os
from datetime import datetime, timedelta, timezone
import time

@pytest.fixture
def temp_task_manager():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = os.path.join(temp_dir, "tasks.json")
        yield TaskManager(temp_file)

def test_task_notification(temp_task_manager, capsys):
    due_time = (datetime.now(timezone.utc) + timedelta(seconds=2)).isoformat() + "Z"
    temp_task_manager.add_task("Task with Notification", due=due_time)
    time.sleep(3)  # Wait for the notification thread to trigger
    captured = capsys.readouterr()
    print("DEBUG OUTPUT:", captured.out)  # Display debug output
    assert any("Task with Notification" in n for n in temp_task_manager.notifications)

def test_no_notification_for_future_task(temp_task_manager):
    due_time = (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat() + "Z"
    temp_task_manager.add_task("Future Task", due=due_time)
    time.sleep(2)  # Ensure no notification is triggered
    assert not any("Future Task" in n for n in temp_task_manager.notifications)
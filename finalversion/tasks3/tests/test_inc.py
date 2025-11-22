import tempfile
from tasks3 import inc
from tasks3.improved_task_manager import TaskManager

def test_inc():
    assert inc(5) == 6

def test_add_task():
    with tempfile.NamedTemporaryFile() as temp_file:
        tm = TaskManager(file_path=temp_file.name)
        task = tm.add_task("Test task", notes="This is a test", tags=["test", "task"], due="2024-12-31")
        assert task["title"] == "Test task"
        assert task["notes"] == "This is a test"
        assert task["tags"] == ["test", "task"]
        assert task["due"] == "2024-12-31"

def test_update_task():
    with tempfile.NamedTemporaryFile() as temp_file:
        tm = TaskManager(file_path=temp_file.name)
        task = tm.add_task("Initial title")
        task_id = task["id"]
        updated = tm.update_task(task_id, title="Updated title", notes="Added notes")
        assert updated is True
        t = tm.get_task(task_id)
        assert t["title"] == "Updated title"
        assert t["notes"] == "Added notes"

def test_get_task():
    with tempfile.NamedTemporaryFile() as temp_file:
        tm = TaskManager(file_path=temp_file.name)
        task = tm.add_task("Sample task")
        task_id = task["id"]
        fetched_task = tm.get_task(task_id)
        assert fetched_task is not None
        assert fetched_task["id"] == task_id

def test_list_tasks():
    with tempfile.NamedTemporaryFile() as temp_file:
        tm = TaskManager(file_path=temp_file.name)
        tm.add_task("Task 1")
        tm.add_task("Task 2")
        tasks = tm.list_tasks()
        assert len(tasks) >= 2
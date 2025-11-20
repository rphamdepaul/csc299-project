import os
import tempfile
from task_manager.store import TaskStore, TaskNotFound


def test_add_and_get():
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        s = TaskStore(path)
        t = s.add_task('test', description='d')
        got = s.get_task(t['id'])
        assert got['title'] == 'test'
    finally:
        os.remove(path)


def test_edit_and_delete():
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        s = TaskStore(path)
        t = s.add_task('a')
        s.edit_task(t['id'], title='b', completed=True)
        got = s.get_task(t['id'])
        assert got['title'] == 'b' and got['completed'] is True
        s.delete_task(t['id'])
        try:
            s.get_task(t['id'])
            assert False, 'should have raised'
        except TaskNotFound:
            pass
    finally:
        os.remove(path)

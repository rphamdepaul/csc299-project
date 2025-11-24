import pytest
import os
import sys
import tempfile

# Ensure the `src` directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from finalversion.pkms import PKMS

@pytest.fixture
def temp_storage():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield os.path.join(temp_dir, 'notes.json')

@pytest.fixture
def pkms(temp_storage):
    return PKMS(temp_storage)

def test_add_and_get(pkms):
    pkms.add('Title 1', 'First note')
    assert any(note['content'] == 'First note' for note in pkms.list())

def test_add_duplicate(pkms):
    pkms.add('Title 1', 'First note')
    with pytest.raises(ValueError):
        pkms.add('Title 1', 'Duplicate note')

def test_list(pkms):
    pkms.add('Title 1', 'First note')
    pkms.add('Title 2', 'Second note')
    assert set(note['title'] for note in pkms.list()) == {'Title 1', 'Title 2'}

def test_delete(pkms):
    pkms.add('1', 'First note')
    pkms.delete('1')
    assert all(note['id'] != '1' for note in pkms.list())

def test_delete_nonexistent(pkms):
    with pytest.raises(ValueError):
        pkms.delete('nonexistent')

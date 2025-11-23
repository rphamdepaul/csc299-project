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
    assert pkms.get('1')['content'] == 'First note'

def test_add_duplicate(pkms):
    pkms.add('Title 1', 'First note')
    with pytest.raises(ValueError):
        pkms.add('Title 1', 'Duplicate note')

def test_list(pkms):
    pkms.add('Title 1', 'First note')
    pkms.add('Title 2', 'Second note')
    assert set(note['title'] for note in pkms.list()) == {'Title 1', 'Title 2'}

def test_search(pkms):
    pkms.add('Title 1', 'First note')
    pkms.add('Title 2', 'Second note')
    results = pkms.search('first')
    assert any(note['title'] == 'Title 1' for note in results)
    assert not any(note['title'] == 'Title 2' for note in results)

def test_delete(pkms):
    pkms.add('1', 'First note')
    pkms.delete('1')
    assert pkms.get('1') is None

def test_delete_nonexistent(pkms):
    with pytest.raises(ValueError):
        pkms.delete('nonexistent')

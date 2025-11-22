import pytest
from src.finalversion.pkms import PKMS
import os
import tempfile

@pytest.fixture
def temp_storage():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield os.path.join(temp_dir, 'notes.json')

@pytest.fixture
def pkms(temp_storage):
    return PKMS(temp_storage)

def test_add_and_get(pkms):
    pkms.add('1', 'First note')
    assert pkms.get('1') == 'First note'

def test_add_duplicate(pkms):
    pkms.add('1', 'First note')
    with pytest.raises(ValueError):
        pkms.add('1', 'Duplicate note')

def test_list(pkms):
    pkms.add('1', 'First note')
    pkms.add('2', 'Second note')
    assert set(pkms.list()) == {'1', '2'}

def test_search(pkms):
    pkms.add('1', 'First note')
    pkms.add('2', 'Second note')
    results = pkms.search('first')
    assert '1' in results
    assert '2' not in results

def test_delete(pkms):
    pkms.add('1', 'First note')
    pkms.delete('1')
    assert pkms.get('1') is None

def test_delete_nonexistent(pkms):
    with pytest.raises(ValueError):
        pkms.delete('nonexistent')

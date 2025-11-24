import tempfile
import json
from finalversion.pkms import PKMS

def test_pkms_add():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = f"{temp_dir}/notes.json"
        pkms = PKMS(temp_file)

        # Add a note
        pkms.add("Test Title", "Test Content")

        # Load the data directly from the file
        with open(temp_file, "r") as f:
            data = json.load(f)

        # Assert the structure of the data
        assert len(data) == 1
        note = list(data.values())[0]
        assert note["title"] == "Test Title"
        assert note["content"] == "Test Content"
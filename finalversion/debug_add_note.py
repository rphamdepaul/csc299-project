import os
from src.finalversion.pkms import PKMS

def debug_add_note():
    print("Debugging add_note command")

    # Initialize PKMS
    pkms = PKMS("notes.json")

    # Add a note
    note_id = "1"
    content = "First note"
    try:
        pkms.add(note_id, content)
        print(f"Note '{note_id}' added successfully.")
    except Exception as e:
        print(f"Error adding note: {e}")

    # List notes
    notes = pkms.list()
    print("Current notes:", notes)

if __name__ == "__main__":
    debug_add_note()
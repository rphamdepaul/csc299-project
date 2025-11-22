# Specifications

## Personal Knowledge Management System (PKMS)

### Core Functionalities
- **Add Notes**: Add a note with a unique identifier and content.
- **List Notes**: Retrieve a list of all note identifiers.
- **Get Note**: Retrieve the content of a note by its identifier.
- **Search Notes**: Search for notes containing a specific query.
- **Delete Note**: Remove a note by its identifier.

### New Features
- **Task Prioritization**: Tasks can have a priority level (low, medium, high). Tasks can also be filtered by priority.

### Implementation Details
- Notes are stored in a JSON file.
- Atomic saves ensure data integrity.
- Thread-safe operations using locks.

### File Structure
- Implementation: `src/finalversion/pkms.py`
- Tests: `finalversion/tests/test_pkms.py`
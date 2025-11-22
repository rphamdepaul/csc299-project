# Tests

## PKMS Tests

### Test Cases
1. **Add and Get Note**: Verify that a note can be added and retrieved correctly.
2. **Add Duplicate Note**: Ensure adding a note with an existing ID raises an error.
3. **List Notes**: Check that all note IDs are listed correctly.
4. **Search Notes**: Confirm that notes matching a query are returned.
5. **Delete Note**: Validate that a note can be deleted.
6. **Delete Nonexistent Note**: Ensure deleting a nonexistent note raises an error.

### Test Framework
- **Framework**: Pytest
- **Test File**: `finalversion/tests/test_pkms.py`

## Task Manager Tests

### Test Cases
1. **Add Task with Priority**: Verify that a task can be added with a valid priority.
2. **Add Task with Invalid Priority**: Ensure adding a task with an invalid priority raises an error.
3. **List Tasks with Priority Filter**: Check that tasks can be filtered by priority.
4. **List Tasks with Invalid Priority Filter**: Ensure filtering tasks with an invalid priority raises an error.

### Test Framework
- **Framework**: Pytest
- **Test File**: `finalversion/tests/test_task_prioritization.py`
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

### Test Results

#### PKMS Tests
- **Results**: All 6 tests passed.
- **Execution Time**: 0.09 seconds

## Task Manager Tests

### Test Cases
1. **Add Task with Priority**: Verify that a task can be added with a valid priority.
2. **Add Task with Invalid Priority**: Ensure adding a task with an invalid priority raises an error.
3. **List Tasks with Priority Filter**: Check that tasks can be filtered by priority.
4. **List Tasks with Invalid Priority Filter**: Ensure filtering tasks with an invalid priority raises an error.

### Test Framework
- **Framework**: Pytest
- **Test File**: `finalversion/tests/test_task_prioritization.py`

### Test Results

#### Task Manager Tests
- **Results**: All 4 tests passed.
- **Execution Time**: 0.09 seconds

## Task Manager Tests (from tasks3)

### Test Cases
1. **Add Task**: Verify that a task can be added with all details.
2. **List Tasks**: Check that tasks can be listed with optional filters for priority and deleted status.
3. **Get Task**: Ensure task details can be retrieved by ID.
4. **Update Task**: Validate that task details can be updated.
5. **Delete Task**: Test both soft and hard deletion of tasks.
6. **Undo Changes**: Verify that changes to tasks can be undone.

### Test Framework
- **Framework**: Pytest
- **Test File**: `tasks3/src/tasks3/improved_task_manager.py`
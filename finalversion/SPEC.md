# Specifications

## Overview
This document outlines the specifications for the CSC299 project, including the PKMS, TaskManager, and terminal chat interface. The software is modular and designed for extensibility.

## Modules

### 1. Personal Knowledge Management System (PKMS)
- **Features**: Add, list, retrieve, search, and delete notes.
- **Storage**: Notes are stored in a JSON file.
- **Concurrency**: Thread-safe operations using locks.
- **Testing**: Refer to `tests.md` for test cases.

### 2. TaskManager
- **Features**: Add, list, update, delete, and undo tasks.
- **Enhancements**:
  - Task prioritization (low, medium, high).
  - Notifications for tasks with due dates.
- **Storage**: Tasks are stored in a JSON file.
- **Concurrency**: Thread-safe operations using locks.
- **Testing**: Refer to `tests.md` for test cases.

### 3. Terminal Chat Interface
- **Features**: Interact with PKMS and TaskManager via terminal commands.
- **Commands**:
  - Add, list, and search notes.
  - Add and list tasks.
- **Testing**: Refer to `tests.md` for test cases.
- **Status**: Completed
- **Details**: The terminal chat interface has been implemented. It allows users to interact with the PKMS and TaskManager via terminal commands. Users can add, list, and search notes, as well as add and list tasks.

### 4. CLI Entrypoint
- **Features**: Manage notes and tasks via terminal commands.
- **Commands**:
  - Add, list, and delete notes.
  - Add, list, and delete tasks.
- **Testing**: Refer to `tests.md` for test cases.

### 5. TasksAdapter
- **Features**: Simplifies interaction with the TaskManager.
  - Add, list, update, and delete tasks.
- **Testing**: Refer to `tests.md` for test cases.
- **Status**: Completed
- **Details**: The TasksAdapter module has been implemented and tested. It provides a simplified interface for managing tasks using the TaskManager.
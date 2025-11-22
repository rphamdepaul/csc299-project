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

### 4. CLI Entrypoint
- **Features**: Manage notes and tasks via terminal commands.
- **Commands**:
  - Add, list, and delete notes.
  - Add, list, and delete tasks.
- **Testing**: Refer to `tests.md` for test cases.
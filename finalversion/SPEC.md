PKMS / Task CLI Project Specification

Overview

This project provides a small CLI-based Personal Knowledge Management System (PKMS) and task management integration.

Goals

- PKMS: JSON-backed notes store with add/list/get/search/delete
- Task integration: reuse existing TaskManager in `tasks3` as adapter
- Terminal chat interface: search and interact with notes and tasks
- AI agents: local stubs that can summarize notes or create tasks
- Tests: pytest-based unit tests for core functionality

Files to edit throughout development

- `src/finalversion/pkms.py` - PKMS core implementation
- `src/finalversion/tasks_adapter.py` - lightweight wrapper around `tasks3` TaskManager
- `src/finalversion/cli.py` - command-line entrypoint
- `src/finalversion/chat.py` - terminal chat UI
- `src/finalversion/agents.py` - simple agent implementations
- `tests/` - pytest tests for pkms, tasks adapter, agents, and CLI

Acceptance criteria

- All tests must pass under pytest in the workspace
- No new files in `tasks3/` (we reuse existing module there)
- Each logical change must be accompanied by SPEC, tests, and documentation updates


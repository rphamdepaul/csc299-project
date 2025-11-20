# Spec-Kit Project

Task manager implementation with JSON-backed storage and CLI.

## Quick Start

```bash
# Run the CLI
python -m task_manager.cli add "My first task" --description "test" --tags work urgent
python -m task_manager.cli list

# Run tests
python -m pytest task_manager/
```

## Governance

This project follows the [Project Constitution v1.0.0](.github/CONSTITUTION.md).

Key principles:
- Clarity over cleverness
- Test-first development
- Simplicity and explicit design
- Consistent UX and accessibility

All PRs must confirm Constitution alignment. See the [PR template](.github/pull_request_template.md) and [Reviewer Quickstart](.github/REVIEWER_QUICKSTART.md).

## Project Structure

```
task_manager/
  store.py       - JSON storage (TaskStore API)
  cli.py         - Command-line interface
  test_store.py  - Unit tests
```

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run linters:

```bash
black task_manager/
flake8 task_manager/
```

Run tests:

```bash
pytest task_manager/
```

## Contributing

1. Read the [Constitution](.github/CONSTITUTION.md)
2. Check the [PR template](.github/pull_request_template.md)
3. Follow test-first development
4. Ensure CI passes before requesting review

For questions or ARB review, open an issue titled "ARB: <topic>".

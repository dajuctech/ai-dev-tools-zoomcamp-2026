# Shared Household Chores

This is my Module 1 homework project for AI Dev Tools Zoomcamp 2026.

The homework starts from a vague idea:

```text
A tool for managing shared household chores
```

I scoped that idea into a small Django application for coordinating chores in a shared household. The goal of the homework is to practice an AI-native developer workflow: turn a vague idea into a project scope, break it into implementation tasks, build the first version with an AI coding agent, and verify the result with tests.

## What It Does

- Create household members
- Create chores with optional description, assignee, and due date
- Edit chores
- Mark chores as complete
- View pending and completed chores separately

## Tech Stack

- Python
- Django
- SQLite for local development
- uv for dependency management

## Project Structure

```text
shared-household-chores/
├── README.md
├── _docs/
│   └── plan.md
├── backlog.md
├── manage.py
├── pyproject.toml
├── uv.lock
├── household_chores/
│   ├── settings.py
│   └── urls.py
└── chores/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── templates/
```

## Setup

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Tests

```bash
uv run python manage.py test
```

Current verification:

```text
6 tests passed
System check identified no issues
```

## Homework Answers

- Coding agent used: Codex
- Features selected: household members, chore creation/editing/assignment, completion tracking, pending/completed views
- Django app registration file: `settings.py`
- First backlog task: project skeleton
- Development server command: `uv run python manage.py runserver`
- Test command: `uv run python manage.py test`

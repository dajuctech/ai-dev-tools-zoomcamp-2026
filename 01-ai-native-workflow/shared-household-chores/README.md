# Shared Household Chores

A small Django homework project for managing chores in a shared household.

## What It Does

- Create household members
- Create chores with optional description, assignee, and due date
- Edit chores
- Mark chores as complete
- View pending and completed chores separately

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

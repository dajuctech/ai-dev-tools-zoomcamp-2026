# RetroLoop

A Django workshop project for weekly team feedback and retrospectives.

## Features

- Register with username, display name, and password
- Create projects and feedback cycles
- Submit start / stop / continue feedback
- Submit feedback anonymously
- Reveal feedback for a retrospective
- Group feedback into editable clusters
- Vote on discussion topics with three votes per person
- Capture decisions and action items
- Process pasted transcript text into candidate retrospective outputs

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

## Docker Compose

The project includes a Postgres service for the workshop constraint:

```bash
docker compose up db
```

The default local Django settings use SQLite so tests and local runs work without requiring Postgres.

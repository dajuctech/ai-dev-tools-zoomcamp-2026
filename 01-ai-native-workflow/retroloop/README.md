# RetroLoop

RetroLoop is a Django workshop practice project for Module 1 of AI Dev Tools Zoomcamp 2026.

The workshop demonstrates an AI-native developer workflow: start with a vague product idea, define the scope, turn it into a backlog, implement in small steps, and verify the result. RetroLoop is the scoped version of the vague idea "a tool for weekly feedback for projects".

This project is included as extra practice alongside the homework project. It is not the homework submission target.

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

## AI Feature Status

This app does not call an AI API yet.

The transcript processing feature is currently a simple rule-based stub:

- lines starting with `Decision:` become decisions
- lines starting with `Action:` or `Todo:` become action items
- matching outputs are saved for review

The workshop PRD mentions Whisper-style transcription, but real audio/video transcription is not implemented in this version.

## Tech Stack

- Python
- Django
- SQLite for local development and tests
- Postgres service available through Docker Compose
- uv for dependency management

## Project Structure

```text
retroloop/
├── README.md
├── docker-compose.yml
├── manage.py
├── pyproject.toml
├── uv.lock
├── retroloop/
│   ├── settings.py
│   └── urls.py
└── retrospectives/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── services.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── templates/
```

## Setup

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver 127.0.0.1:8001
```

Open `http://127.0.0.1:8001/register/`.

## Tests

```bash
uv run python manage.py test
```

Current verification:

```text
11 tests passed
System check identified no issues
```

## Docker Compose

The project includes a Postgres service for the workshop constraint:

```bash
docker compose up db
```

The default local Django settings use SQLite so tests and local runs work without requiring Postgres.

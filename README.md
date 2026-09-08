# AI Dev Tools Zoomcamp 2026

This workspace tracks course material, notes, PRDs, and generated projects for AI Dev Tools Zoomcamp 2026.

## Module Tracker

| Module | Status | Notes | PRDs | Projects |
| --- | --- | --- | --- | --- |
| `01-ai-native-workflow` | In progress | `01-ai-native-workflow/note.md` | `prd_workshop.md`, `prd_homework.md` | `retroloop/`, `shared-household-chores/` |

## Module 1: AI-Native Developer Workflow

Module folder:

```text
01-ai-native-workflow/
```

This module covers:

- spec-driven development
- context engineering
- loop engineering
- graph engineering
- product manager, software engineer, and QA agent roles
- using an AI coding agent to turn a vague idea into an implemented Django project

## Module 1 Files

```text
01-ai-native-workflow/
├── content.md
├── homework.md
├── homework.yaml
├── medium-blog.md
├── note.md
├── practice.md
├── prd_homework.md
├── prd_workshop.md
├── retroloop/
└── shared-household-chores/
```

### Source and Notes

- `content.md` contains the raw course/workshop source content.
- `note.md` contains cleaned study notes for Module 1.
- `homework.md` contains the homework instructions.
- `homework.yaml` contains homework metadata for the course platform.

### PRDs

- `prd_workshop.md` is the PRD for the workshop demo product: RetroLoop.
- `prd_homework.md` is the PRD for the homework product: Shared Household Chores.

## Project 1: RetroLoop

Project folder:

```text
01-ai-native-workflow/retroloop/
```

RetroLoop is the workshop project from `prd_workshop.md`. It is a Django web app for weekly project feedback and retrospectives.

Implemented features:

- username/display-name/password registration
- login and logout
- project creation
- feedback cycles
- start / stop / continue feedback
- anonymous feedback
- feedback reveal
- editable clusters
- three votes per user
- voting close flow
- decisions and action items
- transcript processing stub
- Django admin registration
- tests
- Docker Compose file with Postgres service

Important files:

```text
retroloop/
├── README.md
├── _docs/
│   ├── architecture.md
│   └── plan.md
├── backlog.md
├── docker-compose.yml
├── manage.py
├── pyproject.toml
├── retroloop/
└── retrospectives/
```

Run RetroLoop:

```bash
cd 01-ai-native-workflow/retroloop
uv sync
uv run python manage.py migrate
uv run python manage.py runserver 127.0.0.1:8001
```

Test RetroLoop:

```bash
cd 01-ai-native-workflow/retroloop
uv run python manage.py test
```

Verification:

```text
11 tests passed
System check identified no issues
```

## Project 2: Shared Household Chores

Project folder:

```text
01-ai-native-workflow/shared-household-chores/
```

Shared Household Chores is the homework project from `prd_homework.md`. It is a small Django app for managing chores in a shared household.

Implemented features:

- household members
- chore creation
- chore editing
- chore assignment
- pending chore dashboard
- completed chore page
- mark chore complete
- Django admin registration
- tests
- step-by-step practice document

Important files:

```text
shared-household-chores/
├── README.md
├── _docs/
│   └── plan.md
├── backlog.md
├── manage.py
├── practice.md
├── pyproject.toml
├── household_chores/
└── chores/
```

Run Shared Household Chores:

```bash
cd 01-ai-native-workflow/shared-household-chores
uv sync
uv run python manage.py migrate
uv run python manage.py runserver 127.0.0.1:8000
```

Test Shared Household Chores:

```bash
cd 01-ai-native-workflow/shared-household-chores
uv run python manage.py test
```

Verification:

```text
6 tests passed
System check identified no issues
```

## Notes

- Both generated projects use Django and `uv`.
- Both projects include local SQLite databases after migrations are run.
- RetroLoop includes `docker-compose.yml` for the Postgres constraint from the workshop PRD, but defaults to SQLite for simple local development and tests.
- The generated `.venv/`, SQLite database files, caches, and local runtime artifacts should not be committed.

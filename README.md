# AI Dev Tools Zoomcamp 2026

This repository contains my public project work for AI Dev Tools Zoomcamp 2026.

The focus is on building real software with AI coding agents while keeping a disciplined engineering workflow: define the scope, turn it into a backlog, implement in small steps, and verify the result with tests.

## Module Tracker

| Module | Topic | Status | Public Projects |
| --- | --- | --- | --- |
| `01-ai-native-workflow` | AI-native developer workflow | Complete | `shared-household-chores/`, `retroloop/` |
| `02-end-to-end` | Coming later | Not started | - |
| `03-deployment` | Coming later | Not started | - |
| `04-devops` | Coming later | Not started | - |
| `05-agent-capabilities` | Coming later | Not started | - |

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

## Public Repository Structure

```text
01-ai-native-workflow/
├── retroloop/
└── shared-household-chores/
```

Private study notes, raw course captures, PRDs, planning docs, backlog docs, and draft writing files are intentionally not tracked in Git. The public repository keeps the buildable project code and the README files needed to understand it.

## Homework Project: Shared Household Chores

Project folder:

```text
01-ai-native-workflow/shared-household-chores/
```

Shared Household Chores is the Module 1 homework project. It starts from the vague idea:

```text
A tool for managing shared household chores
```

The idea was scoped into a small Django application for managing chores in a shared household.

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

Important files:

```text
shared-household-chores/
├── README.md
├── manage.py
├── pyproject.toml
├── uv.lock
├── household_chores/
└── chores/
```

Run the homework project:

```bash
cd 01-ai-native-workflow/shared-household-chores
uv sync
uv run python manage.py migrate
uv run python manage.py runserver 127.0.0.1:8000
```

Test the homework project:

```bash
cd 01-ai-native-workflow/shared-household-chores
uv run python manage.py test
```

Verification:

```text
6 tests passed
System check identified no issues
```

## Workshop Practice Project: RetroLoop

Project folder:

```text
01-ai-native-workflow/retroloop/
```

RetroLoop is an additional workshop practice project. It is a Django web app for weekly project feedback and retrospectives.

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
├── docker-compose.yml
├── manage.py
├── pyproject.toml
├── uv.lock
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

## Notes

- Both generated projects use Django and `uv`.
- Both projects use local SQLite by default after migrations are run.
- RetroLoop includes `docker-compose.yml` for the Postgres constraint from the workshop PRD, but defaults to SQLite for simple local development and tests.
- AI is used as part of the development workflow. The generated apps themselves do not call an AI API.
- The generated `.venv/`, SQLite database files, caches, raw notes, PRDs, and private study documents are intentionally excluded from Git.

## Homework Submission Link

Submit the GitHub repository URL:

```text
https://github.com/dajuctech/ai-dev-tools-zoomcamp-2026
```

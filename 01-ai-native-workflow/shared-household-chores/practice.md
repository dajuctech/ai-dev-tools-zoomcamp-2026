# Practice: How the Shared Household Chores Project Was Built

This document explains the step-by-step process used to build the Django homework project from the PRD.

## 1. Start from the PRD

The project started from:

```text
../prd_homework.md
```

The PRD defined the product as a small Django web application for managing shared household chores.

The MVP requirements were:

- create household members
- create chores
- assign chores to household members
- edit chores
- mark chores as complete
- show pending chores
- show completed chores
- include tests

The PRD also required these repository artifacts:

- `.gitignore`
- `README.md`
- `_docs/plan.md`
- `backlog.md`
- a Django project
- a Django app
- tests

## 2. Create the Project Folder

A new implementation folder was created inside the module directory:

```text
shared-household-chores/
```

This keeps the homework implementation separate from the course notes, PRDs, and workshop files.

## 3. Add Basic Repository Files

The first files added were:

```text
.gitignore
README.md
pyproject.toml
```

`.gitignore` excludes local Python and Django artifacts such as:

- `.venv/`
- `__pycache__/`
- `*.sqlite3`
- `.pytest_cache/`
- `.DS_Store`

`README.md` explains what the app does and includes the main commands for setup, migration, running, and testing.

`pyproject.toml` defines the Python project and declares Django as the dependency:

```toml
dependencies = [
    "django>=5.2,<6.0",
]
```

## 4. Create the Product Plan

The plan was written to:

```text
_docs/plan.md
```

The plan turns the PRD into four MVP feature groups:

1. Household members
2. Chore management
3. Completion tracking
4. Review views

It also records what is out of scope:

- authentication
- recurring chores
- notifications
- calendar integrations
- mobile app
- advanced permissions

## 5. Create the Backlog

The implementation backlog was written to:

```text
backlog.md
```

The backlog breaks the PRD into small implementation tasks:

1. Project skeleton
2. Household members
3. Chore CRUD
4. Completion tracking
5. Tests

Each task includes acceptance criteria so the work can be checked after implementation.

## 6. Create the Django Project

The Django project package is:

```text
household_chores/
```

It contains the standard Django project files:

```text
household_chores/__init__.py
household_chores/settings.py
household_chores/urls.py
household_chores/asgi.py
household_chores/wsgi.py
```

The root Django command file is:

```text
manage.py
```

`manage.py` sets:

```python
DJANGO_SETTINGS_MODULE = "household_chores.settings"
```

That tells Django which settings module to use when running commands.

## 7. Create the Django App

The main Django app is:

```text
chores/
```

It contains:

```text
chores/admin.py
chores/apps.py
chores/forms.py
chores/models.py
chores/tests.py
chores/urls.py
chores/views.py
chores/migrations/
chores/templates/chores/
```

This app owns the product behavior: household members, chores, forms, views, routing, templates, admin registration, and tests.

## 8. Add the App to Django Settings

The app was added to `INSTALLED_APPS` in:

```text
household_chores/settings.py
```

The relevant entry is:

```python
"chores",
```

This step is required because Django only loads models, templates, migrations, admin configuration, and tests from apps that are installed.

The project uses SQLite for local development:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

## 9. Wire the Project URLs

The project-level URL file is:

```text
household_chores/urls.py
```

It includes:

```python
path("", include("chores.urls")),
```

This sends the homepage and chore-related routes to the `chores` app.

The app-level URL file is:

```text
chores/urls.py
```

It defines routes for:

- dashboard / pending chores
- completed chores
- new chore
- edit chore
- complete chore
- new household member

## 10. Define the Data Models

The models are defined in:

```text
chores/models.py
```

### HouseholdMember

`HouseholdMember` represents a person in the shared household.

Fields:

- `name`
- `created_at`

The `name` field is unique so duplicate household member names are not allowed.

### Chore

`Chore` represents a household task.

Fields:

- `title`
- `description`
- `assignee`
- `due_date`
- `status`
- `created_at`
- `completed_at`

The `status` field uses two choices:

- `pending`
- `complete`

The model also includes:

```python
mark_complete()
```

This method sets the chore status to complete and records the completion timestamp.

## 11. Create the Forms

Forms are defined in:

```text
chores/forms.py
```

There are two forms:

- `HouseholdMemberForm`
- `ChoreForm`

`HouseholdMemberForm` lets the user add a household member by name.

`ChoreForm` lets the user create or edit:

- title
- description
- assignee
- due date

Using Django `ModelForm` keeps form handling close to the models and avoids writing repetitive validation and field code by hand.

## 12. Implement the Views

Views are defined in:

```text
chores/views.py
```

The implemented views are:

### `chore_list`

Shows the dashboard with pending chores and household members.

It also provides the household member form so new members can be added from the dashboard.

### `completed_chores`

Shows chores with status `complete`.

### `chore_create`

Handles the new chore form.

On valid submission, it saves the chore and redirects back to the dashboard.

### `chore_edit`

Loads an existing chore, lets the user edit it, then saves the updated values.

### `chore_complete`

Marks a chore complete.

This view only accepts `POST` requests because it changes data.

### `member_create`

Adds a new household member.

If the member name is invalid or duplicated, it shows an error message and returns to the dashboard.

## 13. Build the Templates

Templates are stored in:

```text
chores/templates/chores/
```

### `base.html`

Defines the shared page layout, navigation, basic styling, and message display.

### `chore_list.html`

Renders:

- pending chores
- assignee names
- due dates
- edit links
- complete buttons
- household member list
- add-member form

### `chore_form.html`

Renders the create/edit chore form.

The same template is reused for both new chores and existing chores.

### `completed_chores.html`

Renders completed chores separately from pending chores.

This satisfies the PRD requirement that pending and completed chores can be distinguished.

## 14. Register Models in Django Admin

The admin configuration is in:

```text
chores/admin.py
```

Both models are registered:

- `HouseholdMember`
- `Chore`

The admin list pages include useful fields such as assignee, due date, status, and completed timestamp.

## 15. Create the Initial Migration

The initial migration is:

```text
chores/migrations/0001_initial.py
```

It creates the database tables for:

- `HouseholdMember`
- `Chore`

The migration is applied with:

```bash
uv run python manage.py migrate
```

That creates the local SQLite database:

```text
db.sqlite3
```

## 16. Add Tests

Tests are defined in:

```text
chores/tests.py
```

The tests cover:

- marking a chore complete
- rendering the pending chore dashboard
- creating a household member
- creating a chore with an assignee
- moving a completed chore from pending view to completed view
- editing a chore

The tests are run with:

```bash
uv run python manage.py test
```

The verification result was:

```text
Ran 6 tests
OK
```

## 17. Run the App Locally

Install dependencies:

```bash
uv sync
```

Apply migrations:

```bash
uv run python manage.py migrate
```

Start the Django development server:

```bash
uv run python manage.py runserver
```

Open the app:

```text
http://127.0.0.1:8000/
```

## 18. Final Project Structure

The generated project structure is:

```text
shared-household-chores/
├── .gitignore
├── README.md
├── _docs/
│   └── plan.md
├── backlog.md
├── chores/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates/
│   │   └── chores/
│   │       ├── base.html
│   │       ├── chore_form.html
│   │       ├── chore_list.html
│   │       └── completed_chores.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── household_chores/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pyproject.toml
└── uv.lock
```

## 19. How the PRD Requirements Were Covered

- Create household members: implemented with `HouseholdMember`, `HouseholdMemberForm`, and `member_create`.
- Create chores: implemented with `Chore`, `ChoreForm`, and `chore_create`.
- Assign chores: implemented with the `assignee` foreign key.
- Edit chores: implemented with `chore_edit`.
- Mark chores complete: implemented with `mark_complete` and `chore_complete`.
- Show pending chores: implemented with `chore_list`.
- Show completed chores: implemented with `completed_chores`.
- Include tests: implemented in `chores/tests.py`.
- Include homework files: `.gitignore`, `README.md`, `_docs/plan.md`, and `backlog.md` were created.

## 20. Main Commands

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
uv run python manage.py test
```

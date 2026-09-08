# Backlog

## Task 1: Project Skeleton

Create a Django project, a chores app, routing, templates, and a passing test setup.

Acceptance criteria:

- `manage.py` exists.
- The `chores` app is included in Django settings.
- The root URL renders the chores dashboard.
- Tests can run with `uv run python manage.py test`.

## Task 2: Household Members

Add household member records so chores can be assigned.

Acceptance criteria:

- Users can add a household member by name.
- Household members appear in chore assignment choices.

## Task 3: Chore CRUD

Create and edit chores with title, description, assignee, and due date.

Acceptance criteria:

- Users can create a chore with at least a title.
- Users can optionally assign a chore to a household member.
- Users can edit chore details.

## Task 4: Completion Tracking

Allow users to mark chores as complete and review completed chores.

Acceptance criteria:

- Pending chores are shown on the dashboard.
- Completing a chore removes it from the pending list.
- Completed chores are visible on the completed chores page.

## Task 5: Tests

Cover the implemented flows with Django tests.

Acceptance criteria:

- Tests cover creating household members.
- Tests cover creating chores.
- Tests cover assignment.
- Tests cover completion.
- Tests cover pending and completed views.

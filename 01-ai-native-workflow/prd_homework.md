# PRD: Shared Household Chores

## Overview

Shared Household Chores is a Django web application for managing chores in a shared household. The homework starts from the intentionally vague idea "a tool for managing shared household chores", so this PRD defines a conservative MVP that can be implemented with an AI coding agent in a small Django project.

The product should help household members see what needs to be done, who is responsible, and which chores are complete.

## Problem Statement

People living together often need a simple way to coordinate household chores. Without a shared tool, chores can be forgotten, duplicated, or assigned unclearly.

The MVP should provide a basic shared list of chores with ownership and completion status.

## Target Users

- People living in a shared household.
- Household members who need to create, assign, complete, and review chores.

## Assumptions

The homework does not define specific product behavior beyond the vague idea, so this PRD uses these conservative MVP assumptions:

- A household is a shared space with multiple members.
- A chore is a task that needs to be done by someone in the household.
- Each chore can have a title, optional description, assignee, due date, and status.
- The MVP can use simple Django-rendered pages rather than a separate frontend framework.
- The MVP can use Django's default local development database unless the implementation plan chooses otherwise.
- Authentication can be simple or omitted for the earliest version if the backlog starts with core chore management.
- The product should stay small enough for the homework requirement: first specify it, then build it in Django with a coding agent, then cover implemented behavior with tests.

## Goals

- Turn the vague homework idea into a clear, buildable product scope.
- Let users create and view household chores.
- Let users assign chores to household members.
- Let users mark chores as complete.
- Let users see pending and completed chores.
- Keep the MVP simple enough to implement as a Django homework project.

## Non-Goals

- No mobile app.
- No complex calendar integration.
- No email, push, or SMS notifications.
- No payment, billing, or subscription features.
- No AI-based chore recommendations.
- No advanced role or permission system.
- No complex recurrence engine unless added later by the student's own brainstormed spec.
- No production deployment requirement in the homework instructions.

## MVP Scope

The MVP includes:

- a Django project and app
- a homepage or dashboard showing chores
- household member records
- chore creation
- chore editing
- chore assignment to a household member
- chore completion
- basic pending and completed chore views
- tests for the implemented scenarios

The implementation should be driven by a short backlog in `backlog.md`.

## Required Repository Artifacts

The homework implementation should include:

- `.gitignore`
- `README.md`
- `_docs/plan.md`
- `backlog.md`
- a Django project
- a Django app added to the Django project settings
- tests for the implemented scenarios

The repository should be committed and pushed to GitHub for submission.

## User Roles

### Household Member

A household member can:

- view the shared chore list
- create a chore
- assign a chore to a household member
- update chore details
- mark a chore as complete
- view completed chores

### Maintainer / Student Developer

The student developer can:

- use a coding agent to implement the Django app
- run the Django development server
- ask the agent to identify test scenarios
- review and run tests

## Core User Flows

### Create a Chore

1. A household member opens the chore list.
2. The household member selects the option to add a chore.
3. The household member enters a chore title.
4. The household member optionally enters a description, assignee, and due date.
5. The system saves the chore as pending.
6. The chore appears in the shared chore list.

### Assign a Chore

1. A household member opens a chore.
2. The household member chooses or changes the assignee.
3. The system saves the assignee.
4. The chore list shows who is responsible.

### Complete a Chore

1. A household member opens the shared chore list.
2. The household member marks a pending chore as complete.
3. The system updates the chore status.
4. The chore no longer appears as pending.
5. The chore appears in the completed list or with completed status.

### Review Chores

1. A household member opens the dashboard.
2. The system shows pending chores.
3. The system provides access to completed chores.
4. The household member can identify which chores are due and who owns them.

## Functional Requirements

### Chores

- The system must support creating chores.
- A chore must have a title.
- A chore may have an optional description.
- A chore may have an assignee.
- A chore may have an optional due date.
- A chore must have a status, such as pending or complete.
- Users must be able to edit chore details.
- Users must be able to mark chores complete.

### Household Members

- The system must support household member records.
- A chore can be assigned to a household member.
- The chore list should show the assigned member when present.

### Chore Views

- The system must show a shared list of chores.
- Pending chores should be visible from the main page or dashboard.
- Completed chores should be visible separately or clearly marked.

### Django Project

- The application must be implemented in Django.
- The Django app must be added to the project configuration.
- The project should include a `README.md`.
- The project should include a `.gitignore`.
- The product plan should be stored in `_docs/plan.md`.
- A generated implementation backlog should be stored in `backlog.md`.

### Tests

- The implemented behavior should be covered by tests.
- The student should ask the coding agent which scenarios should be tested.
- The student should review the proposed test scenarios before implementation.
- Tests should be runnable from the terminal.

## Acceptance Criteria

- The repository contains `.gitignore`, `README.md`, and `_docs/plan.md`.
- The repository contains a Django project and at least one Django app.
- The Django app is included in the project settings.
- The repository contains a `backlog.md` generated from the product plan.
- The application can be started with the Django development server command.
- A user can open a page that lists chores.
- A user can create a chore with at least a title.
- A user can assign a chore to a household member.
- A user can mark a chore as complete.
- Pending and completed chores can be distinguished.
- Tests exist for the first implemented features.
- Tests can be run from the terminal.

## Data Entities

### HouseholdMember

Represents a person in the shared household.

Suggested fields:

- name
- optional display label or contact field if needed later

### Chore

Represents a household task.

Suggested fields:

- title
- description
- assignee
- due date
- status
- created timestamp
- completed timestamp

## Technical Constraints

- Use Django.
- Use Python.
- `uv` is recommended.
- The student does not need prior Python or Django knowledge.
- Use a coding agent that can edit files and run commands directly where possible.
- Pick one coding agent and stick with it for the whole homework.
- The homework expects the work to be committed and pushed to a GitHub repository.
- The homework asks for tests after implementing a few backlog items.

## Open Questions

- Should users log in, or is a simple local household member selector enough for the MVP?
- Should a household be modeled explicitly, or is one shared household enough for the homework version?
- Should chores support recurrence, or should recurring chores be post-MVP?
- Should due dates be required or optional?
- Should chores have priority?
- Should completed chores be archived or shown in the same list with completed status?
- Should assignment be required when creating a chore?
- Which coding agent will be used for the homework?
- What are the final 2-4 features selected during the student's brainstorming step?

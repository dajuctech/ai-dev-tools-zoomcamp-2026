# Module 1: AI-Native Developer Workflow

## Summary

This module shows how to keep control when using AI coding agents. The main workflow is to start with a vague product idea, turn it into a clear specification, choose an implementation approach, split the work into small tasks, give the agent durable project context, and use separate roles for product management, implementation, and QA.

The workshop uses a "weekly feedback for projects" idea to demonstrate the difference between one-shot prompting and a more disciplined AI-native development process. A vague prompt produced a working CLI, but it was not the intended product. The improved process turned the same idea into a scoped retrospective web application with clear roles, features, tasks, and checks.

The companion article describes the same workflow as a way to make requests specific so agents do not need to guess, decompose the request into tasks, assign those tasks to specialized agents, and use a loop to work through the backlog.

## Key Concepts

### AI-Native Development

AI-native development is not just asking an agent to write code. It is a workflow where humans guide product scope, architecture, task definition, and quality checks while agents help with implementation and verification.

The goal is to avoid "shoot and forget" coding, where the agent fills in too many unstated assumptions and produces something that may work but does not match the intended product.

In this module, the human acts as product manager and architect at the start: they decide what the product should do, what is out of scope, and which technologies are acceptable before asking the coding agent to implement.

### Spec-Driven Development

Spec-driven development means writing down what should be built before asking an agent to implement it.

The module distinguishes between:

- Project-level specification: what the overall product is, who it serves, and what is in or out of scope.
- Feature-level specification: what a specific task should do, including acceptance criteria and edge cases.

The specification should reduce ambiguity. If the prompt is vague, the agent must make assumptions. Those assumptions may not match what the user wanted.

### Context Engineering

Context engineering is the practice of giving the agent durable, reusable project context. Instead of explaining the same rules in every prompt, the project should contain files that agents can read.

Important context can include:

- project purpose
- tooling commands
- testing commands
- implementation constraints
- process rules
- links to documents
- team role descriptions

The workshop uses `AGENTS.md` as the main tool-agnostic context file. For Claude Code, a separate `CLAUDE.md` can point the agent to read `AGENTS.md`.

The advice is to keep `AGENTS.md` focused. Do not put every detail there. Instead, use it to point agents to other files such as `process.md`, testing guidelines, UI guidelines, or role instructions when those files are relevant.

The article uses `_docs/process.md` for workflow rules and `_docs/team/` for role descriptions. `AGENTS.md` links to those files so each agent can load only the context needed for its task.

### Loop Engineering

Loop engineering means designing a loop that keeps prompting the agent to continue through a larger goal or repeated workflow.

Instead of manually prompting the agent for every issue, the user can set a goal such as grooming all MVP issues. The loop keeps the agent moving until the broader goal is complete.

The workshop mentions:

- Claude Code goals
- Claude Code scheduled loops
- Codex goals
- custom loops using hooks and tmux if an agent does not support them directly

Loop engineering is useful when there is a pile of similar tasks, such as grooming many GitHub issues or working through a backlog.

Loop engineering answers the question of what happens when an agent stops. A goal or loop can keep the agent moving through a defined pile of work instead of requiring the user to manually restart every step.

### Graph Engineering

Graph engineering is organizing agent work as a workflow with multiple roles and possible paths.

The simplified graph shown in the workshop is:

1. Take an issue from the backlog.
2. If it is not groomed, send it to the product manager role.
3. Send the groomed issue to the software engineer role for implementation.
4. Send the result to the QA role.
5. If QA passes, the issue is done.
6. If QA fails, send it back to the engineer for fixes.

The graph separates responsibilities instead of letting one agent define the task, implement it, and judge its own work.

Graph engineering answers who does what when more than one agent is involved. The graph defines specialized agents as nodes and describes how work moves between them.

## Workshop Workflow

### 1. Start with a Vague Idea

The selected idea was a tool for weekly feedback for projects.

A one-shot prompt was tested:

```text
Implement tool for weekly feedback for projects
```

The agent created a Python CLI for tracking weekly project health. It was a working application, but it was not the intended product. This demonstrated why vague prompts are risky: the agent silently chooses the product shape, stack, and behavior.

The source notes that this one-shot `weekly-feedback` CLI included documentation and tests, but still missed the intended product direction. The lesson is that passing tests do not prove the agent built the right thing.

### 2. Brainstorm the Product Scope

The next step was to use ChatGPT as a brainstorming partner, asking it to help scope the product and ask one question at a time.

The product direction became a team retrospective tool where:

- all team members can submit weekly feedback
- feedback uses a start / stop / continue style
- feedback is attributed by default, but contributors can choose anonymous submission
- contributors can only see their own submissions before the retrospective
- a facilitator reveals and manages feedback
- feedback can be clustered
- team members vote on topics to discuss
- votes help prioritize discussion
- the retrospective produces actions and decisions
- recordings, audio, or transcripts may be processed after the meeting

The brainstorming ended with a Markdown plan for the MVP.

### 3. Define the MVP and Exclusions

The MVP scope included:

- project page
- current feedback cycle
- feedback form
- retrospective board
- media or transcript upload page
- retrospective summary
- team member and facilitator roles
- editable clustering
- voting
- action items with description, owner, and optional due date

Explicit exclusions were also important. The workshop emphasized that saying what is out of scope prevents agents from adding extra features too early.

### 4. Choose a Technology Stack

The agent was asked to read the plan and propose multiple technology options before writing code.

Options discussed included:

- Next.js full stack with Postgres
- Django
- FastAPI plus React
- Phoenix / Elixir

Django was selected because the presenter already knew it well and could read and review Python code more easily. The broader advice was to choose technologies that the human reviewer understands, because AI-generated code still needs review.

The stack was simplified for MVP:

- Python
- Django
- Postgres
- Docker Compose
- OpenAI Whisper for transcription
- no email for authentication
- no heavy background job system at the start
- no file storage for the MVP; process uploaded media and discard it

The presenter also recommended challenging every technology choice, especially versions and unnecessary complexity, because LLMs can suggest outdated or overbuilt options.

### 5. Create a Backlog

The plan and architecture were turned into a structured list of tasks.

Good tasks should be:

- independent
- small enough to finish in one agent session
- large enough to represent meaningful progress
- clear from a product point of view
- suitable for review and acceptance criteria

The generated backlog contained tasks such as:

- project skeleton with passing test
- Docker Compose environment
- base layout and frontend assets
- authentication without email
- project membership and join links
- permissions
- feedback cycles
- feedback cards

The tasks were pushed to GitHub as issues. The workshop treated GitHub issues as the working backlog.

### 6. Add Persistent Project Context

After bootstrapping the project, the workshop introduced context engineering.

Files created or discussed:

- `AGENTS.md`: shared instructions for all coding agents
- `CLAUDE.md`: Claude-specific file that can tell Claude Code to read `AGENTS.md`
- `_docs/process.md`: describes how work should move through the project
- `_docs/plan.md`: initial product plan
- `_docs/architecture.md`: technology and architecture decisions
- `_docs/tasks.md`: initial generated backlog
- `_docs/team/pm.md`: product manager role description
- `_docs/team/software-engineer.md`: software engineer role description
- `_docs/team/qa-engineer.md`: QA role description

The initial planning documents can become stale after the issues are created. They are useful as seed documents, but the GitHub issues become the main working source.

The process document can start small. In the workshop, it grows as the user corrects the agent and discovers rules that should be reused in future sessions.

### 7. Groom Issues with a Product Manager Role

The workshop created a `team` folder with role instructions. The first role was a product manager.

The PM role is responsible for grooming tasks before implementation. It reads an issue and rewrites it with a clearer template.

The groomed issue should include:

- goal
- description
- acceptance criteria
- edge cases
- out-of-scope items

Acceptance criteria should be checkable. Someone should be able to look at the result and say yes or no for each criterion.

The PM should not implement the task. Its job is to remove ambiguity so the engineer can implement without repeatedly asking what the user meant.

Example acceptance criteria for authentication included:

- registration page renders a form
- username, display name, and password are supported
- duplicate usernames show a visible error
- users can log in and log out
- no email, verification, mail backend, or password reset flow is included

The workshop also used labels such as `MVP` and `post-MVP` to separate required work from follow-up ideas.

### 8. Implement with a Software Engineer Role

A software engineer role was added after the PM role.

The engineer should:

- read the groomed issue
- follow project instructions
- implement against the acceptance criteria
- run the relevant checks
- commit changes
- avoid closing the issue before QA verifies it

The engineer should not be responsible for deciding whether its own work fully passes. That is handled by QA.

### 9. Verify with a QA Role

A QA engineer role was added to check implementation results against acceptance criteria.

The QA role should:

- read the issue and acceptance criteria
- inspect the implementation
- run the application and tests where relevant
- check each criterion
- return a binary pass or fail verdict
- avoid fixing the code directly

If QA fails the task, the work goes back to the engineer for fixes.

The workshop emphasized that this extra testing role improves quality but increases token usage. Each issue may require product grooming, implementation, QA, and follow-up fixes.

### 10. Use an Orchestrator

The orchestrator is the main agent session that coordinates the graph.

It should not groom, implement, or test directly. Instead, it launches the correct sub-agent:

- PM for grooming
- engineer for implementation
- QA for verification

The orchestrator can work through MVP issues and route each issue through the workflow. This combines loop engineering and graph engineering: the loop keeps progress moving, and the graph defines the roles and transitions.

The article describes the orchestrator lifecycle as:

1. Pick an issue.
2. If the issue is not groomed, launch the PM.
3. Launch the engineer.
4. Launch QA.
5. If QA fails, send the QA comment back to the engineer.
6. Close the issue only after QA passes.

## Important Tools and Files

Tools mentioned:

- ChatGPT for brainstorming and scoping
- Claude Code for coding-agent demos
- Codex as an alternative coding agent
- tmux for long-running or remote agent sessions
- VS Code for project editing
- Git and GitHub for commits, repository hosting, and issues
- Django for the selected web app framework
- Python
- Postgres
- Docker Compose
- OpenAI Whisper for transcription
- uv for Python dependency management
- pytest for tests
- ruff for linting

Files and folders mentioned:

- `_docs/plan.md`: product plan generated from brainstorming
- `_docs/architecture.md`: architecture and technology decisions
- `_docs/tasks.md`: generated backlog before creating GitHub issues
- `AGENTS.md`: reusable context for agents
- `CLAUDE.md`: Claude-specific pointer to shared context
- `_docs/process.md`: workflow and process rules
- `_docs/team/pm.md`: product manager role instructions
- `_docs/team/software-engineer.md`: software engineer role instructions
- `_docs/team/qa-engineer.md`: QA role instructions

## Practical Takeaways

- Do not start implementation from a vague prompt unless the exact outcome does not matter.
- Use a chat assistant to brainstorm and narrow product scope before coding.
- Ask the assistant to ask one question at a time and keep responses short during brainstorming.
- Decide what is in scope and what is explicitly out of scope.
- Review and challenge technology choices before accepting them.
- Prefer a stack that the human reviewer understands.
- Break the project into GitHub issues that are small, independent, and reviewable.
- Groom user-facing issues before implementation.
- Make acceptance criteria concrete and checkable.
- Keep agent context in files so every new session can understand the project.
- Keep `AGENTS.md` concise and link to more specific documents.
- Update process documentation when you have to manually correct the agent, so the correction becomes reusable context.
- Use separate PM, engineer, and QA roles to reduce blind spots.
- Use loops or goals for repeated work across many issues.
- Expect higher token usage when using PM, engineer, and QA agents, but expect better quality in return.
- Commit regularly so changes can be inspected and rolled forward cleanly.

## Homework and Next Steps

The module homework is to build a Django TODO app with the AI tool of your choice. Prior Django knowledge is not required.

Suggested process:

1. Write a short product specification.
2. Choose a simple stack.
3. Create a backlog of small tasks.
4. Store reusable agent context in `AGENTS.md`.
5. Groom tasks with acceptance criteria.
6. Implement tasks with an AI coding agent.
7. Use a separate QA or review step before considering the work done.

# PRD: RetroLoop

## Overview

RetroLoop is a Django web application for collecting weekly project feedback and running team retrospectives. Team members submit feedback before a retrospective, a facilitator reveals and organizes it during the meeting, the team votes on discussion topics, and the retrospective ends with captured decisions and action items.

The product comes from the workshop idea "weekly feedback for projects." The MVP focuses on one project retrospective workflow and avoids unnecessary platform features.

The workshop contrasted RetroLoop with a one-shot `weekly-feedback` CLI. That CLI tracked weekly project status, wins, issues, blockers, and next steps, but it was not the intended product. RetroLoop is the specified web product that emerged after brainstorming and scoping.

## Problem Statement

Teams need a structured way to collect project feedback, discuss the most important topics, and turn retrospective discussions into decisions and follow-up actions.

A vague "weekly feedback" tool can easily become a simple status tracker or CLI if the product is not specified. RetroLoop instead focuses on retrospective preparation, discussion, prioritization, and summary.

## Target Users

- Team members who submit weekly feedback.
- Facilitators, likely project owners, who reveal feedback, guide the retrospective, cluster topics, and confirm outputs.

## Goals

- Allow all team members to contribute weekly project feedback.
- Support start / stop / continue style feedback.
- Allow feedback to be attributed by default or submitted anonymously.
- Hide other teammates' feedback until the appropriate retrospective stage.
- Let a facilitator reveal, cluster, and manage feedback.
- Let team members vote on topics to prioritize discussion.
- Capture decisions and action items from the retrospective.
- Support processing an uploaded recording, audio file, or transcript to help extract actions and decisions.

## Non-Goals

- No full email-based authentication in the MVP.
- No email verification.
- No self-serve password reset.
- No built-in meeting recording in the MVP.
- No heavy background job system at the start.
- No long-term file storage for uploaded media in the MVP.
- No deployment setup beyond local Docker Compose.
- No command-line-only project status tracker as the target product.

## MVP Scope

The MVP includes:

- project page
- current feedback cycle page
- feedback submission form
- retrospective board
- feedback reveal flow
- editable clustering
- voting on discussion topics
- media, audio, or transcript upload page
- retrospective summary page
- action items with description, owner, and optional due date
- team member and facilitator roles

One retrospective belongs to one project.

## User Roles

### Team Member

Team members can:

- submit weekly feedback
- choose whether feedback is anonymous
- view their own submitted feedback before the retrospective
- vote on topics after feedback is revealed and clustered

### Facilitator

The facilitator can:

- create a feedback cycle
- reveal submitted feedback
- cluster feedback items
- edit automatic clusters
- guide voting and discussion
- review and confirm generated actions and decisions

## Core User Flows

### Submit Weekly Feedback

1. A team member opens the current feedback cycle.
2. The team member enters feedback using the start / stop / continue structure.
3. The team member leaves the submission attributed or selects anonymous submission.
4. The system saves the feedback.
5. The team member can see only their own submitted feedback before the retrospective reveal.

### Reveal and Cluster Feedback

1. The facilitator opens the retrospective board.
2. The facilitator reveals all submitted feedback at the same time.
3. The system groups feedback into clusters where possible.
4. The facilitator can edit the clusters during the meeting.
5. Anonymous feedback remains anonymous.

### Vote on Discussion Topics

1. After clustering, team members vote on topics they want to discuss.
2. Each team member gets three votes.
3. Team members may place multiple votes on the same topic.
4. Voting results are hidden until voting closes.
5. The board shows a prioritized list of topics for discussion.

### Run Retrospective and Capture Outputs

1. The team discusses prioritized topics.
2. Deferred items can remain on the board for later handling.
3. The facilitator captures decisions and action items.
4. Each action item has a description, owner, and optional due date.
5. The retrospective summary shows the outcome of the meeting.

### Process Meeting Media or Transcript

1. After the meeting, the facilitator uploads a video, audio file, or transcript.
2. The system processes the input.
3. The system extracts candidate decisions and action items.
4. The facilitator reviews and confirms the extracted outputs.
5. Uploaded media is not retained as long-term file storage in the MVP.

## Functional Requirements

### Projects

- Users can work within a project.
- A project can have team members.
- A project can have retrospectives or feedback cycles.
- One retrospective belongs to one project.

### Feedback Cycles

- The system supports a current feedback cycle for a project.
- Team members can submit feedback to the active cycle.
- Feedback is collected before the retrospective reveal.

### Feedback Submission

- Feedback uses start / stop / continue categories.
- Feedback is attributed by default.
- A team member can mark feedback as anonymous.
- Team members can see their own feedback after submission.
- Team members cannot see other teammates' feedback before reveal.

### Retrospective Board

- The facilitator can reveal all feedback.
- Feedback appears at the same time when revealed.
- Feedback can be clustered.
- Automatic clustering is editable.
- Anonymous feedback must stay anonymous.

### Voting

- Each team member gets three votes.
- A team member can place multiple votes on the same topic.
- Voting results are hidden until voting closes.
- After voting closes, the board shows a prioritized discussion list.

### Decisions and Action Items

- The retrospective can capture decisions.
- The retrospective can capture action items.
- Action items include description, owner, and optional due date.

### Media or Transcript Processing

- The facilitator can upload video, audio, or a transcript.
- The system can process the uploaded input to extract actions and decisions.
- The MVP does not include built-in recording.
- Uploaded media can be processed and discarded.

### Authentication

- Authentication is simple for the MVP.
- Users can create an account with username, display name, and password.
- Users can log in and log out.
- The authentication flow does not use email.
- There is no mail backend, email verification, or self-serve password reset in the MVP.

## Acceptance Criteria

- A user can register with username, display name, and password.
- A user can log in and log out.
- No email backend, email verification, or password reset flow is required.
- A project page exists.
- A current feedback cycle page exists.
- A team member can submit start / stop / continue feedback.
- A team member can choose anonymous submission.
- Submitted anonymous feedback does not reveal the submitter.
- Before reveal, a team member can only see their own submissions.
- A facilitator can reveal feedback for the retrospective.
- Revealed feedback appears together.
- Feedback can be clustered.
- Automatically created clusters can be edited.
- Team members can vote on discussion topics.
- Each team member has three votes.
- Multiple votes on the same topic are allowed.
- Voting results become visible after voting closes.
- The retrospective board prioritizes topics by votes.
- The retrospective can record decisions.
- The retrospective can record action items with description, owner, and optional due date.
- A facilitator can upload video, audio, or transcript input after the meeting.
- The system can use uploaded input to produce candidate actions and decisions for facilitator review.

## Data Entities

The source material implies these entities:

- User: account with username, display name, and password.
- Project: workspace for one team or project.
- Membership: association between users and projects, if needed by the implementation.
- Feedback Cycle: current period for collecting feedback.
- Feedback Item: submitted start / stop / continue feedback, with attributed or anonymous visibility.
- Retrospective: meeting or board associated with a project.
- Cluster: group of related feedback items.
- Vote: team member vote on a topic or cluster.
- Decision: recorded outcome from discussion.
- Action Item: follow-up task with description, owner, and optional due date.
- Uploaded Media or Transcript: temporary input for extracting decisions and actions.

## Technical Constraints

- Use Django for the web application.
- Use Python.
- Use Postgres.
- Use Docker Compose for the local environment.
- Use OpenAI Whisper for transcription.
- Keep the MVP simple.
- Do not add email authentication.
- Do not add a heavy background job system at the start.
- Do not add persistent file storage for uploaded media in the MVP.
- Prefer technologies the human reviewer can understand and review.
- The workshop used GitHub issues as the implementation backlog after the initial plan and architecture were drafted.

## Open Questions

- What exact project invitation or membership flow should be used beyond simple project access?
- What permissions distinguish a facilitator from a regular team member?
- When exactly does a feedback cycle close?
- Who can close voting?
- How should deferred discussion items be represented after the meeting?
- What exact review UI should the facilitator use for extracted actions and decisions?
- What happens if media or transcript processing fails?
- How much automatic clustering is required for the MVP versus manual clustering?

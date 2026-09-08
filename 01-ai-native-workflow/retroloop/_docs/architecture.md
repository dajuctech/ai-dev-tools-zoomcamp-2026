# Architecture

RetroLoop is a small Django application.

## Local Stack

- Python
- Django
- SQLite for simple local development and tests
- Postgres available through Docker Compose
- Django templates for UI

## Notes

The PRD mentions OpenAI Whisper for transcription. This MVP accepts pasted transcript text and extracts candidate decisions and actions with simple text rules. Built-in recording and persistent media storage are out of scope.

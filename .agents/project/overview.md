# Project overview

Goal: write the global rules that an AI agent follows when developing other projects.

## Layout

- `home/agents/agent.md`: entrypoint with the base instructions; points to the more specific files in the subfolders.
- `home/agents/coding/`, `home/agents/instructions/`, `home/agents/tasks/`: specific rules (language rules, role profiles, numbered tasks).
- `home/claude/CLAUDE.md`: entrypoint for Claude; tells it to read `~/.agents/agent.md` and treat it as an extension of `CLAUDE.md`.
- `scripts/deploy.py`: copies `home/` into the user's home directory (leading dot added); mirrors `~/.agents/` after confirmation.
- `README.md`: describes the project and the installation steps.
- `LICENSE`: MIT.

## Conventions

- Everything is written in English.
- Paths inside `home/` use the final installed names (`~/.agents/`, `~/.claude/`).
- Rules in `home/agents/agent.md` to preserve: repository-only file access (read-only exception for `~/.agents/`), Git read-only, no automatic tests, local `.agents/` with free-structure `project/` and `local/`, local overrides global.
- `deploy.py` must never delete files outside `~/.agents/` and must ask for confirmation before deleting.

# This repository is a meta-project

**Read this first.** This repository contains the *source* of the global agent rules. It does not apply them to itself.

- `home/` is the **product you are writing**. It is a copy of files that the user manually places in their home directory, adding a leading dot (`home/agents` → `~/.agents`, `home/claude` → `~/.claude`).
- Files under `home/` are **not instructions for you**. Do not follow the rules written there while working here; edit them as content.
- The files inside `home/` must always refer to the final paths (`~/.agents/...`, `~/.claude/CLAUDE.md`), never to `home/...`.
- Your own rules for this repository are in `.agents/project/` (committed) and `.agents/local/` (not committed). Read them before working.
- Never read from or write to the real `~/.agents` or `~/.claude`. Only edit files inside this repository.
- Write all rules and documentation in English.

# agents

Global rules for AI agents that develop other projects.

This repository is a meta-project: it holds the source of the rules, not a program. The rules are meant to be copied into the user's home directory and read by the agent in every project it works on.

## Structure

```
home/
├── agents/
│   ├── agent.md        # entrypoint with the base instructions
│   ├── coding/         # how to write code, per language
│   ├── instructions/   # role profiles (planner, developer, tester, reviewer)
│   └── tasks/          # numbered tasks (context, architecture, plan, develop, refactor, unit tests, bugfix)
└── claude/
    └── CLAUDE.md       # entrypoint for Claude Code
scripts/
└── deploy.py           # installs home/ into your home directory
```

## Installation

Requires Python 3.9 or later. From the repository root:

```
python scripts/deploy.py
```

The script copies each folder in `home/` into your home directory, adding a leading dot (`.`) to its name:

| In this repository  | In your home directory |
| ------------------- | ---------------------- |
| `home/agents/`      | `~/.agents/`           |
| `home/claude/`      | `~/.claude/`           |

- Existing files are **overwritten**, including `~/.claude/CLAUDE.md`: back it up first if it has your own content.
- `~/.agents/` is mirrored: files in it that are not in `home/agents/` are deleted. The script lists them and asks for confirmation (`y` or `Y`) before deleting; with any other answer the files are copied but nothing is deleted. Deletion is permanent, not sent to the recycle bin.
- Other files in `~/.claude/` are never deleted.

You can also install manually by copying the folders yourself, adding the leading dot.

All paths written inside the files in `home/` already use the final names (`~/.agents/...`), so they work once installed.

## Rules imposed on the agent

- Read, modify, create and delete files only inside the repository it works in; never follow links to external files. The only exception is `~/.agents/`, which is read-only.
- Never run Git commands that change the repository state; version control is left to the user.
- Do not run tests unless explicitly requested.
- Each repository gets a local `.agents/` folder, with `project/` (project specifications, committed) and `local/` (extra material, not committed). Their internal structure is free.
- On conflict, the local `.agents/` wins over the global one.
- Reply in the language the user wrote in.

## Working on this repository

An agent working here writes the global rules, so it must not confuse them with its own. See [CLAUDE.md](CLAUDE.md) and `.agents/project/`.

## License

[MIT](LICENSE)

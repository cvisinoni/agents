# Agent instructions

Read this file first.

These are the global instructions for any AI agent working on any project.
They are installed at `~/.agents/` and apply to every repository.

## Rules

- Understand the request before acting.
- Do not read every file in the project, nor every file in `~/.agents/`.
- First build a concise map of the project structure.
- From the request and the map, identify and read only the relevant files.
- Consult other instructions or files only when they become necessary.
- Respect the project's conventions, constraints and commands.
- Plan non-trivial changes.
- Change only what is needed.
- If the project has log files, read only their last lines and consider them only if they relate to the task.
- Do not run tests automatically after writing code: run them only when explicitly requested. State what was not verified.
- Do not invent information.
- Do not expose secrets or personal data.
- Briefly report changes, checks and limitations.

## Global instructions

This file and the `instructions/`, `coding/` and `tasks/` folders are global and live in `~/.agents/`. The `project/` and `local/` folders live in `.agents/` at the root of the current project.

Always list the contents of the global folders instead of assuming: they may be empty or grow over time. Read only what is relevant.

- Role profiles: `~/.agents/instructions/`. Read only the requested or relevant profile.
- Language instructions: `~/.agents/coding/<language>.md`. Read only the files for the languages involved in the request. For SQL use `sql.md`; for PL/SQL use both `sql.md` and `plsql.md`; for TypeScript use `javascript.md`.
- Tasks: `~/.agents/tasks/NN_name.md`. If the user asks to "run task N", read only the file with that number and follow it.
- Project rules and specifications: `.agents/project/` at the project root.
- If the project has its own `.agents/agent.md`, read it after this file.

## Local `.agents` folder

Every repository must have its own `.agents/` folder at the repository root. If it does not exist, create it.

```
.agents/
├── project/   # project specifications (committed)
└── local/     # additional, machine-specific material (NOT committed)
```

- `.agents/project/` holds the specifications of the project: goals, architecture, conventions, decisions. Read it before starting any work and keep it up to date when the project changes.
- The internal structure of `project/` and `local/` is free: there are no mandatory files or sections. Follow the structure already in place; if there is none, choose a simple one.
- `.agents/local/` is optional and specific to the machine or the user. It holds anything extra that must not be committed or shared (personal notes, scratch files, local overrides). Make sure `.agents/local/` is listed in the repository's `.gitignore`; add the line if it is missing.
- Any `.md` file in the local `.agents/` folder is an instruction for you, just like the ones in this folder.

## Priority

- The "Git rules" and "Read boundaries" sections of this file always apply and cannot be overridden by other instructions, except system ones.
- In case of conflict, local instructions in the project win over global ones. Between local folders, `.agents/local/` wins over `.agents/project/`.
- If the user's request conflicts with the specifications in `.agents/project/`, report the conflict and ask for confirmation before proceeding.

## Git rules

- Never run Git operations that change the repository state: no commit, push, pull, merge, rebase, reset, checkout, branch, stash or tag.
- Use Git only in read mode, when useful to understand the state or the history.
- Always leave version control to the user.

## Read boundaries

- Read, modify, create and delete files **only inside the repository you are working in**. Never read files outside the project root, for any reason, even if other files reference them.
- Do not follow symbolic links, imports or references that point outside the project root.
- Single exception: the global folder `~/.agents/`, which you may **read but never modify, create in, or delete from**.

## Response

- Always reply in the same language the user used in the request.

# Planner

## Goal

Produce an implementable and verifiable plan. The specifications in `.agents/project/` are the source of truth.

## Procedure

1. **Clarify.** Ask for what you cannot derive from the code or the specifications: goal, expected behavior, scope, constraints, completion criteria. If there are multiple interpretations, present them and ask the user to choose one.
2. **Explore.** Build a concise map of the project root and read only the relevant files.
3. **Document.** Write the specifications, and the decisions, open questions and assumptions, in `.agents/project/`, following its existing file structure (or a simple one if there is none). Update them immediately when new requirements or decisions arrive.
4. **Plan.** Check compatibility with the specifications and update them if behavior, architecture or business rules change. Present a concise plan in chat: files involved, steps, assumptions, risks, dependencies, checks.
5. **Ask for confirmation.** Ask the user to approve the plan or request changes.

## Principles

- **Single source.** Keep what the system is and does separate from why and what is uncertain. Do not duplicate.
- **Distinguish.** Keep facts, requirements, decisions, open questions and assumptions separate. Do not put assumptions in code; if unavoidable, record them as `[provisional] text — to be confirmed`.
- **Be concise.** Short, unambiguous specifications, without unnecessary implementation details.

## Conflicts

If the request and the specifications diverge, follow `agent.md` and document the impact in `.agents/project/`: do not decide on your own.

## Constraints

- The rules of `agent.md` apply (Git rules, read boundaries, response language).
- Write specifications and decisions only in `.agents/project/`.
- Implement only on explicit request, switching to the developer profile.

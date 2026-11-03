# Developer

## Goal

Implement the requested changes simply and correctly.

## Language

- Write code, names, comments and error messages in English, unless explicitly requested otherwise.
- Exception: the rules in `~/.agents/coding/` may set a different language for comments (e.g. PL/SQL); they take precedence over this section.

## Principles

- Prefer simple, readable and maintainable solutions.
- Keep the implementation focused on the requirement.
- Modify existing code before introducing new structures.
- Avoid unnecessary abstractions, patterns and indirection.

## Clean Code

- Use clear and consistent names.
- Keep functions and methods short and focused.
- Remove dead code and unused variables.
- Remove duplication when doing so improves readability.
- Prefer explicit code to clever code.

## Comments

- Write self-explanatory code.
- Add comments only for non-obvious information.
- Do not comment every function, variable or statement.

## Validation

- Validate inputs when required by requirements, security, external interfaces or known errors.
- Avoid defensive checks, guard clauses, wrappers and error handling with no practical value.
- Trust well-defined internal contracts, unless there are concrete reasons not to.
- The error handling and file safety rules in `~/.agents/coding/` take precedence over this section.

## Implementation

- Implement only the necessary logic.
- Do not anticipate future requirements without justification.
- Avoid over-engineering.
- Prefer clarity and simplicity to flexibility and configurability.

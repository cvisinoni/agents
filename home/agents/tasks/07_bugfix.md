# Task 07 — Bugfix

Profile: developer (`~/.agents/instructions/developer.md`) and the `~/.agents/coding/` files for the languages involved.

## Goal

Find the cause of an error and fix it.

## Steps

1. Start from the description, message or stack trace provided by the user. If relevant logs exist, read their last lines; if there are none, proceed without.
2. Reconstruct the sequence: first error, context and component; distinguish cause from symptoms.
3. Read only the code involved and form a hypothesis about the cause; if the data is not enough, ask for more information.
4. Present the cause and the proposed fix; apply the fix if it is clear and limited, otherwise ask for confirmation.

## Output

Cause identified (with references to files and any logs), fix and residual risks.

## Limits

Do not expose secrets or personal data found in logs. Do not run tests unless explicitly requested.

# JavaScript

Also applies to TypeScript, unless the project has specific rules.
The project rules in `.agents/project/` take precedence over this file.

## Version and tools

- Respect the target Node/browser version and the package manager in use (npm, pnpm, yarn): do not mix them.
- Use the formatter and linter configured in the project (e.g. Prettier, ESLint) and run the related scripts.
- If the project uses TypeScript, keep typing strict and avoid `any`.

## Style and formatting

- Use `const` by default, `let` only if the variable is reassigned; do not use `var`.
- Use strict equality (`===`, `!==`).
- Prefer `async`/`await` over `then` chains.
- Use ES modules (`import`/`export`) if the project does not adopt CommonJS.

## Naming

- camelCase for variables and functions, PascalCase for classes and components, UPPER_SNAKE_CASE for global constants.
- File names consistent with the project's convention (e.g. kebab-case, or PascalCase for components).

## Code structure

- One module, one responsibility; avoid files that export unrelated elements.
- Prefer pure functions and immutable data where it does not complicate the code.
- Separate domain logic, data access and presentation.

## Error handling

- Always handle rejected Promises; do not leave Promises without `await` or `catch`.
- Throw `Error` objects (or subclasses), not strings.
- Do not silence exceptions with empty `catch` blocks.

## Tests

- Use the project's framework (e.g. Vitest, Jest, Playwright) and its location and naming conventions.
- Isolate network, time and randomness with mocks or fakes.

## Security

- Do not use `eval`, `new Function` or `innerHTML` with untrusted data.
- Validate and sanitize inputs coming from the user, the network or other external sources.
- Do not put secrets in client code or in the bundle.
- Add dependencies only if necessary and maintained.

## Avoid

- Modifications to the prototypes of native objects.
- Implicit global variables.
- Debug `console.log` in delivered code.

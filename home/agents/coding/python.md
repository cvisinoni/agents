# Python

The project rules in `.agents/project/` take precedence over this file.

## Version and tools

- Respect the project's Python version and environment/dependency manager (e.g. venv, Poetry, uv, pip-tools).
- Use the configured formatter, linter and type checker (e.g. Black or Ruff, mypy or pyright).

## Style and formatting

- Follow PEP 8, delegating formatting to the formatter.
- Add type hints to public functions and non-obvious signatures.
- Prefer single quotes for constant strings, for example `return 'ok'`.
- Write function documentation with triple double quotes; put a line break after the opening quotes:
  ```python
  def function(...):
      """
      Doc
      """
      return
  ```
- Use f-strings for string formatting.
- Use `pathlib` for paths and context managers (`with`) for resources.

## Naming

- snake_case for modules, functions and variables; PascalCase for classes; UPPER_SNAKE_CASE for constants.
- `_` prefix for module-internal elements.

## Code structure

- Keep imports at the top of the file, grouped: standard library, third party, local.
- Protect executable code with `if __name__ == "__main__":`.
- Prefer `dataclass` or explicit types over dictionaries with implicit keys for structured data.

## Error handling

- Catch specific exceptions; do not use `except:` or `except Exception:` without re-raising or a concrete reason.
- Use `raise ... from err` to preserve the cause.
- Use the `logging` module instead of `print` for diagnostics and errors.

## Security

- Do not use `eval`, `exec` or `pickle` on untrusted data.
- Use parameterized queries for databases; do not build SQL with f-strings.
- Avoid `subprocess` with `shell=True` and external input.
- Read secrets from environment variables or a secret manager, never from the code.

## Avoid

- Mutable default arguments (`def f(x=[])`).
- `import *`.
- Installing global packages or changing the environment without need.

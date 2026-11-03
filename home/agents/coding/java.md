# Java

The project rules in `.agents/project/` take precedence over this file.

## Version and tools

- Respect the project's JDK version and build tool (Maven or Gradle); use the wrapper if present (`mvnw`, `gradlew`).
- Use the configured formatter and static analysis (e.g. Spotless, Checkstyle, SpotBugs).
- Use the language features available in the target version (e.g. `record`, `var`, switch expressions).

## Style and formatting

- Follow the style already present in the project; if there is none, use Google Java Style.
- One public class per file.
- Prefer immutability: `final` fields, unmodifiable collections, `record` for data.

## Naming

- PascalCase for classes and interfaces, camelCase for methods and variables, UPPER_SNAKE_CASE for constants.
- Lowercase packages, consistent with the existing structure.

## Code structure

- Separate the layers (controller, service, repository, domain) according to the project's architecture.
- Use the dependency injection of the framework in use (e.g. Spring) via constructor.
- Avoid generic utility classes that accumulate unrelated responsibilities.

## Error handling

- Use specific exceptions; do not catch `Exception` or `Throwable` without a concrete reason.
- Do not ignore exceptions: handle them, enrich them with context or propagate them.
- Use `try-with-resources` for closeable resources.
- Use `Optional` for absent return values, not for fields or parameters.

## Tests

- Use the project's framework (usually JUnit 5, with Mockito or AssertJ).
- Respect the `src/test/java` structure and the naming of existing tests.
- Distinguish unit tests and integration tests according to the build configuration.

## Security

- Use `PreparedStatement` or the ORM framework's parameters; do not concatenate SQL.
- Validate inputs at the system boundaries (APIs, files, messages).
- Do not write secrets or personal data to logs.
- Avoid native Java deserialization of untrusted data.

## Avoid

- `System.out.println` and `printStackTrace` instead of the logger.
- Mutable static state.
- Adding dependencies without a verified need.
